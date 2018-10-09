from utils import *
import inter_2d as i2d


def main():
    save(generate_2d_data(cos, -0.8, 0.8, 50, rand=True, cheb=True), 'data/sin_exp')
    plot_2d(load('data/sin_exp'))
    i2d.Interpolation('data/sin_exp')
    while True:
        req = input('> ').split()
        try:
            if req[0] == '2d':
                file_name = req[1]
                i2d.Interpolation(file_name)
            elif req[0] == '3d':
                file_name = req[1]
            else:
                msg('write \'2d\' or \'3d\' and file name')

        except IndexError:
            msg('write \'2d\' or \'3d\' and file name')


if __name__ == '__main__':
    main()