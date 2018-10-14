from utils import *
import inter_2d as i2d
import inter_3d as i3d

poly = lambda x, y: x**3+4*y**2
ratio = lambda x, y: (x**2+y**2)/(x*(x+1))
expo = lambda x, y: math.exp(x+y) + 1
harm = lambda x, y: math.cos(2*x-3*y)


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

    interpolate(poly)
    interpolate(ratio)
    interpolate(expo)
    interpolate(harm)