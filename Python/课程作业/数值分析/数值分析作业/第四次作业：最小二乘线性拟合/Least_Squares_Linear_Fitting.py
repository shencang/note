import random as rand

import matplotlib.pyplot as plots
import numpy as np
from numpy.linalg import *

# 用来正常显示负号
plots.rcParams['axes.unicode_minus'] = False
# 用来正常显示中文标签
plots.rcParams['font.sans-serif'] = ['SimHei']

lists_x = []
lists_y = []


def book_5_1():
    """课本例题条件"""
    global lists_x, lists_y
    # 例题5-1的给出条件
    lists_x = [0.0, 0.2, 0.4, 0.6, 0.8]
    lists_y = [0.9, 1.9, 2.8, 3.3, 4.2]


def random_fx():
    """随机数模拟函数"""
    global lists_x, lists_y
    x = np.arange(-10, 10, 0.2)
    s = 6
    y = [8 * r + s for r in x]
    num = 0
    x_random = []
    y_random = []
    for x_r in x:
        y_r = y[num]
        random = float(rand.randint(30, 120)) / 100
        num = num + 1
        x_random.append(x_r * random)
        y_random.append(y_r * random)
    lists_x = x_random
    lists_y = y_random


# 例题5-1的求解
def result():
    """例题5.1的求解"""
    # Σx的二次累计结果
    resultxx = 0
    # Σxy的相乘累计结果
    resultyx = 0
    # Σx的结果
    resultx = sum(lists_x)
    # Σy的结果
    resulty = sum(lists_y)
    # 计数器
    num = 0
    for x in lists_x:
        # 累计获得Σx*y
        resultyx = resultyx + x * lists_y[num]
        # 累计获得Σx^2
        resultxx = resultxx + x * x
        num = num + 1

    # 令偏导等于0，列出的系数矩阵 ： 由化简的方程组 n*a0+a1*Σxi = Σyi  a0Σxi a1*Σxi^2 = Σxi*yi 得到。
    a = np.array([[num, resultx],
                  [resultx, resultxx]])
    # 对应的 Σyi 和 Σxi*yi
    b = np.array([[resulty],
                  [resultyx]])

    # 获得运算结果，取得系数。使用的是不带权值的计算方式。
    a0, a1 = solve(a, b)
    display('re', round(a0[0], 3), a1[0])
    draw_ls(lists_x, lists_y, a0, a1, "例题5.1的求解")


def display(flag, a, b):
    if flag == 'result' or flag == 're':
        print("拟合的直线为", 'y=', a, '+', b, 'x')


def draw_ls(list_x, list_y, la, lb, tag):
    """绘制函数和寻找过程的路径"""
    plots.title(tag)
    plots.xlabel("x")
    plots.ylabel("y")
    x = np.linspace(min(lists_x), max(lists_x), 99)
    # 绘制函数的图像
    y = la + lb * x
    plots.plot(x, y, color='Orange', linewidth=1.0)
    for v in range(len(list_x)):
        plots.scatter(list_x[v], list_y[v], c='r')  # 每次迭代的点
    plots.show()


def input_estimation_and_conditions():
    """输入初始估计"""
    print('请选择数据:1为课本例题5.1的题设 2.为随机生成数目模拟y = 8*x+6')
    result = int(input("请输入选择"))
    return result


if __name__ == '__main__':
    choose = input_estimation_and_conditions()
    if choose == 1:
        book_5_1()
    if choose == 2:
        random_fx()
    elif choose != 1 and choose != 2:
        print("输入错误")
        exit(1)
    result()
