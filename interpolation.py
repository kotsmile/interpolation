from utils import *
import inter_2d as i2d
import inter_3d as i3d


def main():

    while True:
        req = input('> ').split()
        try:
            if req[0] == '2d':
                file_name = req[1]
                i2d.Interpolation2D(file_name)
            elif req[0] == '3d':
                file_name = req[1]
            else:
                msg('write \'2d\' or \'3d\' and file name')

        except IndexError:
            msg('write \'2d\' or \'3d\' and file name')


if __name__ == '__main__':
    # save(generate_2d_data(lambda x: x**2, 30, -5, 5, rand=True), 'data/test')
    #
    # plot_2d(load('data/test'))
    # intr = i2d.Interpolation2D('data/test')
    # intr.plot()
    f = 'data/3d_test'
    save(generate_3d_data(lambda x, y: sin(x+y), 10, -2, 2, -2, 2, rand=False), f)
    plot_3d(load(f, dem=3))
    g = i3d.Interpolation3D(f)
    g.plot()