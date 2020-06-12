import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签\


def closest_points(n, lists_x, list_y, index1, index2):
    minDist = 999999
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            dout = (lists_x[i] - lists_x[j]) ** 2 + (list_y[i] - list_y[j]) ** 2
            if dout < minDist:
                minDist = dout
                index1 = i
                index2 = j
            j = j + 1
        i = i + 1
    return np.sqrt(minDist), index1, index2


lists_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 4, 5, 5, 3, 4, 3, 6, 9]
lists_y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 6, 3, 0, 11, 1, 0, 0, 0, 9]

result = closest_points(len(lists_x), lists_x, lists_y, 0, 0)
print('最近对为：第', int(result[1]) + 1, '和第', int(result[2]) + 1, '号点。他们之间的距离为：', result[0])

fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
l = ax.plot(x, y)
dot, = ax.plot([], [], 'ro')
line, = ax.plot(x, y)


def init():
    ax.set_xlim(min(lists_x), max(lists_x))
    ax.set_ylim(min(lists_y), max(lists_y))
    return l


def gen_dot():
    for i in range(len(lists_x)):
        newdot = [lists_x[i], lists_y[i]]
        yield newdot


def update_dot(newd):
    dot.set_data(newd[0], newd[1])
    return dot,


def gen_line():
    for i in range(len(lists_x) - 1):
        newline = [[lists_x[i], lists_y[i]], [lists_x[i + 1], lists_y[i + 1]]]
        yield newline


def update_line(newl):
    line.set_data(newl[0], newl[1])
    return line


ani = animation.FuncAnimation(fig, update_dot, frames=gen_dot, interval=1000, init_func=init)
# ani = animation.FuncAnimation(fig, update_line, frames = gen_line, interval = 1000, init_func=init)
plt.title('蛮力法：最近对问题')
plt.xlabel("x")
plt.ylabel("y")
# plt.xlim(min(lists_x),max(lists_x))# 设置x轴范围
# plt.ylim(min(lists_y),max(lists_y))# 设置y轴范围
s = 0
while s < len(lists_x):
    plt.scatter(lists_x[s], lists_y[s], c='b')
    s = s + 1

plt.show()
