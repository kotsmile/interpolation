from collections import namedtuple
import math

poly = lambda x: 1 / x
expo = math.exp
cos = math.cos
sin = math.sin

p_2d = namedtuple('Point', ['x', 'y'])
p_3d = namedtuple('Point', ['x', 'y', 'z'])


def msg(text):
    print('=' * (len(text) + 4) + f'\n  {text}\n' + '=' * (len(text) + 4))


def load(file_name, dem=2):
    try:
        if dem == 2:
            with open(file_name, 'r') as file:
                data = [p_2d(float(line.strip().split()[0]), float(line.strip().split()[1])) for line in file]
            return data
        elif dem == 3:
            with open(file_name, 'r') as file:
                data = [p_3d(float(line.strip().split()[0]), float(line.strip().split()[1]),
                             float(line.strip().split()[2])) for line in file]
            return data

    except (FileNotFoundError, IndexError):
        msg('wrong input file')


def float_range(start, end, step):
    r = []
    x = start
    while x <= end:
        r.append(x)
        x += step
    return r


def generate_2d_data(start, end, func, step):
    data = []
    for x in float_range(start, end, step):
        try:
            data.append(p_2d(x, func(x)))
        except ZeroDivisionError:
            pass
    return data
