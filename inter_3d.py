import utils


def kran(a, b):
    if a == b:
        return 1
    return 0


class Interpolation3D:


    # TRANSFORM TO 3-D lets go!!!!!
    def __init__(self, file_name):
        self.data = utils.load(file_name, dem=2)
        print(self.data)
        self.y = None
        self.n = 0
        self.min = min(utils.unpack_2d(self.data).x)
        self.max = max(utils.unpack_2d(self.data).x)
        self.understand()
        self.calculate()
        self.plot()

    def understand(self):
        err = 100000
        data_x_ap = list(map(lambda x: int(x*err)/err, utils.unpack_2d(self.data).x))
        max_same = 0
        new_xs = []
        best_n = 0
        for i in range(1000):
            roots_ap = list(map(lambda x: int(x*err)/err, utils.roots_T(i)))
            same = len(list(set(data_x_ap) & set(roots_ap)))
            if max_same < same:
                max_same = same
                best_n = i
                new_xs = list(set(data_x_ap) & set(roots_ap))
                if same == len(self.data):
                    break

        self.n = best_n
        f = utils.get_func(self.data, err=err)[0]
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
