from collections import namedtuple
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import matplotlib.pyplot as plt
import time


poly = lambda x: 1 / x
expo = math.exp
cos = math.cos
sin = math.sin

p_2d = namedtuple('P2D', ['x', 'y'])
p_3d = namedtuple('P3D', ['x', 'y', 'z'])


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


def save(data, file_name):
    with open(file_name, 'w') as f:
        for p in data:
            if p.__repr__()[1] == '2':
                f.write(f'{p.x} {p.y}\n')
            elif p.__repr__()[1] == '3':
                f.write(f'{p.x} {p.y} {p.z}\n')


def float_range(start, end, steps, rand=False):
    step = (end - start)/steps
    r = []
    for i in range(steps):
        if rand:
            r.append(random.uniform(start, end))
        else:
            r.append(start + i*step)
    return r


def generate_2d_data(y, start, end, steps, rand=False, cheb=False):
    data = []
    if not cheb:
        for x in float_range(start, end, steps, rand=rand):
            try:
                data.append(p_2d(x, y(x)))
            except ZeroDivisionError:
                pass
        return data
    else:
        roots = set()
        while len(roots) < steps:
            roots.add(random.choice(roots_T(steps)))
        return [p_2d(x, y(x)) for x in roots]


def generate_3d_data(z, start_x, end_x, start_y, end_y, steps, rand=False):
    data = []
    xs = float_range(start_x, end_x, steps, rand=rand)
    random.shuffle(xs)
    ys = float_range(start_y, end_y, steps, rand=rand)
    random.shuffle(ys)
    for x, y in zip(xs, ys):
        try:
            data.append(p_3d(x, y, z(x, y)))
        except ZeroDivisionError:
            pass
    return data


def plot_2d(data):
    plt.scatter(unpack_2d(data).x, unpack_2d(data).y)
    plt.grid(True)
    plt.show()


def plot_3d(data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(unpack_3d(data).x, unpack_3d(data).y, unpack_3d(data).z)
    plt.show()


def unpack_2d(points):
    x = []
    y = []
    for p in points:
        x.append(p.x)
        y.append(p.y)
    return p_2d(x, y)


def unpack_3d(points):
    x = []
    y = []
    z = []
    for p in points:
        x.append(p.x)
        y.append(p.y)
        z.append(p.z)
    return p_3d(x, y, z)


def T(n, x):
    return math.cos(n*math.acos(x))


def roots_T(n):
    try:
        return [math.cos(math.pi*(i + 1/2)/n) for i in range(n)]
    except ZeroDivisionError:
        return None


def get_func(data):
    d = {p.x: p.y for p in data}
    return lambda x: d[x], unpack_2d(data).x


# save(generate_2d_data(expo, -0.8, 0.8, 5, rand=True), 'data/expo_exp')
# plot_2d(load('data/expo_exp'))

