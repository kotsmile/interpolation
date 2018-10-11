import utils


def kran(a, b):
    if a == b:
        return 1
    return 0


class Interpolation2D:
    def __init__(self, file_name, err):
        self.err = err
        self.data = utils.load(file_name, dem=2)
        self.y = None
        self.n = len(self.data)
        self.min = min(utils.unpack_2d(self.data).x)
        self.max = max(utils.unpack_2d(self.data).x)
        self.understand()
        self.calculate()
        self.plot()

    def understand(self):
        data_x_ap = list(map(lambda x: int(x*self.err)/self.err, utils.unpack_2d(self.data).x))
        max_same = 0
        new_xs = []
        best_n = 0
        for i in range(self.n + 1):
            roots_ap = list(map(lambda x: int(x*self.err)/self.err, utils.roots_T(i)))
            same = len(list(set(data_x_ap) & set(roots_ap)))
            if max_same < same:
                max_same = same
                best_n = i
                new_xs = list(set(data_x_ap) & set(roots_ap))
                if same == len(self.data):
                    break

        self.n = best_n
        print(best_n)
        f = utils.get_func(self.data, err=self.err)[0]
        self.data = [utils.p_2d(x, f(x)) for x in new_xs]

    def calculate(self):
        c = []
        for k in range(self.n):
            c_k = 0
            for p in self.data:
                c_k += utils.T(k, p.x)*p.y/((1 + kran(k, 0)) * self.n / 2)
            c.append(c_k)

        def y_0(x, n):
            res = 0
            for i in range(n):
                res += c[i]*utils.T(i, x)
            return res

        self.y = y_0

    def plot(self):
        data = []
        for x in utils.float_range(self.min, self.max, 10000):
            data.append(utils.p_2d(x, self.y(x, self.n)))
        utils.plot_2d(data)
