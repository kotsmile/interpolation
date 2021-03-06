from collections import namedtuple
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import matplotlib.pyplot as plt
import time
from inter_3d import Interpolation3D


p_2d = namedtuple('P2D', ['x', 'y'])
p_3d = namedtuple('P3D', ['x', 'y', 'z'])


def interpolate(func):

    data1 = generate_3d_data(func, 10, -1, 1, -1, 1, rand=False)
    s_data1 = generate_3d_data(func, 30, -0.9, 0.9, -0.9, 0.9, rand=False)

    data2 = generate_3d_data(func, 5, 0, 2, 0, 2, rand=False)
    s_data2 = generate_3d_data(func, 30, 0.1, 1.9, 0.1, 1.9, rand=False)

    i1 = Interpolation3D(data=data1, real_data=s_data1)
    i1.plot()

    i2 = Interpolation3D(data=data2, real_data=s_data2)
    i2.plot()

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


def generate_2d_data(y, steps, start=0, end=0, rand=False):
    data = []
    for x in float_range(start, end, steps, rand=rand):
        try:
            data.append(p_2d(x, y(x)))
        except ZeroDivisionError:
            pass
    return data


def generate_3d_data(z, steps, start_x=0, end_x=0, start_y=0, end_y=0, rand=False):
    data = []
    xs = float_range(start_x, end_x, steps, rand=rand)
    for x in xs:
        ys = float_range(start_y, end_y, steps, rand=rand)
        random.shuffle(ys)
        for y in ys:
            try:
                data.append(p_3d(x, y, z(x, y)))
            except ZeroDivisionError:
                pass

    return data


def plot_2d(data):
    plt.scatter(unpack_2d(data).x, unpack_2d(data).y)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def plot_3d(data, data_in=None, data_sub=None):

    if data_sub:
        fig = plt.figure(figsize=plt.figaspect(0.5))
        ax = fig.add_subplot(1, 2, 1, projection='3d')
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    ax.scatter(unpack_3d(data).x, unpack_3d(data).y, unpack_3d(data).z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    if data_sub:
        ax2 = fig.add_subplot(1, 2, 2, projection='3d')
        ax2.scatter(unpack_3d(data_sub).x, unpack_3d(data_sub).y, unpack_3d(data_sub).z)
        ax2.set_xlabel('x')
        ax2.set_ylabel('y')

    if data_in:
        ax.scatter(unpack_3d(data_in).x, unpack_3d(data_in).y, unpack_3d(data_in).z, c='r', marker='o')


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


def get_func(data, err=10000000000):
    d = {int(p.x*err)/err: p.y for p in data}
    return lambda x: d[x], unpack_2d(data).x


if __name__ == '__main__':
    plot_3d(load('data/3d_test', dem=3))


