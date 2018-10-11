import utils
import math


def kran(a, b):
    if a == b:
        return 1
    return 0


class Interpolation3D:

    def __init__(self, file_name, err):
        self.data = utils.load(file_name, dem=3)
        self.err = err
        self.z = None
        self.n = 0
        self.min_x = min(utils.unpack_3d(self.data).x)
        self.max_x = max(utils.unpack_3d(self.data).x)
        self.min_y = min(utils.unpack_3d(self.data).y)
        self.max_y = max(utils.unpack_3d(self.data).y)
        self.n = int(math.sqrt(len(self.data)))
        print(self.n)
        self.calculate()
        self.plot()

    def understand(self):
        pass

    def calculate(self):
        c_xs = [[] for i in range(self.n)]
        for k in range(self.n):
            i = 0
            print(f'{int(i*1000/self.n)/10}%')
            for j in range(self.n):
                c_j_i = 0
                for p in self.data[i*self.n + j: i*self.n + j*2]:
                    print(';')
                    c_j_i += utils.T(j, p.x)*p.z/((1 + kran(j, 0)) * self.n / 2)
                c_xs[i].append(c_j_i)
                print('.')

        def z_0(x, i, n):
            res = 0
            for k in range(n):
                a = c_xs[i][k]*utils.T(k, x)
                res += a
            return res

        self.z = z_0

    def plot(self):

        data = []
        for _ in range(self.n):
            i = 0
            data_i = []
            for x in utils.float_range(self.min_x, self.max_x, 50):
                data_i.append(utils.p_3d(x, utils.unpack_3d(self.data).y[i*self.n], self.z(x, i, self.n)))

            data += data_i

        utils.plot_3d(data)
        # data = []
        # for x in utils.float_range(self.min_x, self.max_x, 1000):
        #
        #     data.append(utils.p_2d(x, self.z_fs[0](x, self.n)))
        # utils.plot_2d(data)
