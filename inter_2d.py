import utils


class Interpolation:
    def __init__(self, file_name):
        self.data = utils.load(file_name, dem=2)
        self.y = None
        self.calculate()
        self.plot()


    def calculate(self):
        c = []
        for k in range(len(self.data)):
            c_k = 0
            for p in self.data:
                c_k += utils.T(k, p.x)*p.y
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
