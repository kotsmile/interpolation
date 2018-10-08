import utils
import inter_2d as i2d


def main():
    i2d.Interpolation('data/plot')
    while True:
        req = input('> ').split()
        try:
            if req[0] == '2d':
                file_name = req[1]
                i2d.Interpolation(file_name)
            elif req[0] == '3d':
                file_name = req[1]
            else:
                utils.msg('write \'2d\' or \'3d\' and file name')

        except IndexError:
            utils.msg('write \'2d\' or \'3d\' and file name')


if __name__ == '__main__':
    main()