import utils


class Interpolation2D:
    def __init__(self, file_name=None, data=None):
        if file_name:
            self.data = utils.load(file_name, dem=2)
        if data:
            self.data = data
        self.y = None
        self.min = min(utils.unpack_2d(self.data).x)
        self.max = max(utils.unpack_2d(self.data).x)


    def calculate(self, x):
        ps_old = []
        ps_new = []
        for d in self.data:
            ps_old.append(d.y)
        for n in range(len(self.data)-2, 0, -1):
            for j in range(n):
                i = j
                k = len(self.data) - 1 - n + j
                try:
                    p = (ps_old[j]*(self.data[k].x - x) + ps_old[j+1]*(x - self.data[i].x))/(self.data[k].x - self.data[i].x)
                except ZeroDivisionError:
                    # print(self.data[k].x, self.data[i].x, k, i)
                    pass

                ps_new.append(p)
            ps_old = ps_new
            ps_new = []
        return ps_old[0]

    def plot(self):
        data = [utils.p_2d(x, self.calculate(x)) for x in utils.float_range(self.min, self.max, 1000)]
        utils.plot_2d(data)
