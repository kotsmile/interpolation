import utils


def kran(a, b):
    if a == b:
        return 1
    return 0


class Interpolation:
    def __init__(self, file_name):
        self.data = utils.load(file_name, dem=2)
        self.y = None
        self.n = 0
        self.understand()
        self.calculate()
        self.plot()

    def understand(self):
        e = 1000
        d_x_a = list(map(lambda x: int(x*e)/e, utils.unpack_2d(self.data).x))
        m = 0

        for i in range(len(d_x_a)):
            r_a = list(map(lambda x: int(x*e)/e, utils.roots_T(i)))
            l = len(list(set(d_x_a) & set(r_a)))
            print(i, l)
            if m <= l:
                m = l

        self.n = m
        
        print(m)

    def calculate(self):
        c = []
        for k in range(self.n):
            c_k = 0
            for p in self.data:
                c_k += utils.T(k, p.x)*p.y/((1 + kran(k, 0)) * self.n / 2)
            c.append(c_k)

        def y_0(x):
            res = 0
            for i in range(len(self.data)):
                res += c[i]*utils.T(i, x)
            return res

        self.y = y_0

    def plot(self):
        data = []
        for x in utils.float_range(min(utils.unpack_2d(self.data).x), max(utils.unpack_2d(self.data).x), 10000):
            data.append(utils.p_2d(x, self.y(x)))
        utils.plot_2d(data)
