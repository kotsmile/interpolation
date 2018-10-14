import utils
import math
import inter_2d


class Interpolation3D:

    def __init__(self, file_name=None, data=None, real_data=None):
        if file_name:
            self.data = utils.load(file_name, dem=3)
        if data:
            self.data = data
        if real_data:
            self.real_data = real_data
        self.z = None
        self.n = 0
        self.min_x = min(utils.unpack_3d(self.data).x)
        self.max_x = max(utils.unpack_3d(self.data).x)
        self.min_y = min(utils.unpack_3d(self.data).y)
        self.max_y = max(utils.unpack_3d(self.data).y)


    def calculate(self, x, y):

        datas = []
        d_y = []
        self.data.append(utils.p_3d('1', 1, 1))

        x_0 = self.data[0].x
        for d in self.data:
            if d.x != x_0:
                datas.append(d_y)
                x_0 = d.x
                d_y = [utils.p_2d(d.y, d.z)]
            else:
                d_y.append(utils.p_2d(d.y, d.z))

        self.data.pop()

        zs = []
        for d in datas:
            i = inter_2d.Interpolation2D(data=d)
            yr = i.calculate(y)
            zs.append(yr)

        xs = list(set(utils.unpack_3d(self.data).x))
        xs.sort()

        last_data = []
        for x_, z_ in zip(xs, zs):
            last_data.append(utils.p_2d(x_, z_))

        inter = inter_2d.Interpolation2D(data=last_data)
        z = inter.calculate(x)
        return z

    def plot(self):
        data = []
        for x in utils.float_range(self.min_x, self.max_x, 30):
            for y in utils.float_range(self.min_y, self.max_y, 30):
                data.append(utils.p_3d(x, y, self.calculate(x, y)))

        error_data = []
        for r in self.real_data:
            error_data.append(utils.p_3d(r.x, r.y, self.calculate(r.x, r.y)-r.z))

        utils.plot_3d(data, data_in=self.data, data_sub=error_data)
