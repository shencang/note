import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl


def secondary_spline_method(x):
    """
    二次样条插值法
    :return:
    """
    # num_height表示未知数和方程数量
    num_weight = 3 * (len(x) - 1)
    parameter = []
    i = 1
    # 计算方程内点两边相邻节点处函数值相等的方程 方程数量2n-2
    while i < len(x) - 1:
        coefficient = init(num_weight)
        # 计算a b c放入系数coefficient列表里，原计划打算直接填充矩阵，遇到点问题。
        coefficient[(i - 1) * 3] = x[i] * x[i]
        coefficient[(i - 1) * 3 + 1] = x[i]
        coefficient[(i - 1) * 3 + 2] = 1
        # coefficient 里的数据取出后后移
        movement_coefficient = init(num_weight)
        movement_coefficient[i * 3] = x[i] * x[i]
        movement_coefficient[i * 3 + 1] = x[i]
        movement_coefficient[i * 3 + 2] = 1
        # 因为a1(a0)= 0,去除矩阵中a0对应的行列
        parameter.append(coefficient[1:])
        parameter.append(movement_coefficient[1:])
        i = i + 1
    # 输入端点处两个方程的函数值 方程数量2
    coefficient = init(num_weight - 1)
    coefficient[0] = x[0]
    coefficient[1] = 1
    parameter.append(coefficient)
    coefficient = init(num_weight)
    coefficient[((len(x) - 1) - 1) * 3 + 0] = x[-1] * x[-1]
    coefficient[((len(x) - 1) - 1) * 3 + 1] = x[-1]
    coefficient[((len(x) - 1) - 1) * 3 + 2] = 1
    parameter.append(coefficient[1:])
    # 导数内点相等列出的方程。方程数量n-1
    # 人为规定a1=0  方程数量1
    i = 1
    while i < len(x) - 1:
        coefficient = init(num_weight)
        coefficient[(i - 1) * 3] = 2 * x[i]
        coefficient[(i - 1) * 3 + 1] = 1
        coefficient[i * 3] = -2 * x[i]
        coefficient[i * 3 + 1] = -1
        temp = coefficient[1:]
        parameter.append(temp)
        i = i + 1
        # 返回结果矩阵
    return parameter


def init(size):
    """
    初始化数组
    :param size:
    :return:
    """
    j = 0
    data = []
    while j < size:
        data.append(0)
        j += 1
    return data


def solutions(parametes, y):
    """

    :param parametes: 计算函数系数
    :param y: parametes是系数矩阵，y结果列
    :return: 二次插值系数
    """
    num = len(x) - 1
    result = init(num * 3 - 1)
    i = 1
    while i < num:
        result[(i - 1) * 2] = y[i]
        result[(i - 1) * 2 + 1] = y[i]
        i += 1
    result[(num - 1) * 2] = y[0]
    result[(num - 1) * 2 + 1] = y[-1]
    a = np.array(secondary_spline_method(x))
    b = np.array(result)
    return np.linalg.solve(a, b)


def calculate(paremeters, x):
    """

    :param paremeters: 计算函数值
    :param x: parameters为二次函数的系数，x为自变量
    :return: 因变量
    """
    result = []
    for data_x in x:
        result.append(paremeters[0] * data_x * data_x + paremeters[1] * data_x + paremeters[2])
    return result


def draw(data_x, data_y, new_data_x, new_data_y):
    """

    :param data_x: 为离散的点x坐标
    :param data_y: 为离散的点y坐标
    :param new_data_x: 为由拉格朗日插值函数计算的值
    :param new_data_y: 为由拉格朗日插值函数计算的值
    :return: null
    """
    plt.plot(new_data_x, new_data_y, label="拟合曲线", color="black")
    plt.scatter(data_x, data_y, label="离散数据", color="red")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("二次样条函数")
    plt.legend(loc="upper left")
    plt.show()


def get_result(x, y, result):
    """
    计算并绘制
    :return:
    """
    data_x1 = np.arange(2, 4.5, 0.1)
    data_y1 = calculate([0, result[0], result[1]], data_x1)
    data_x2 = np.arange(4.5, 7, 0.1)
    data_y2 = calculate([result[2], result[3], result[4]], data_x2)
    data_x3 = np.arange(7, 9.5, 0.1)
    data_y3 = calculate([result[5], result[6], result[7]], data_x3)
    data_x = []
    data_y = []
    data_x.extend(data_x1)
    data_x.extend(data_x2)
    data_x.extend(data_x3)
    data_y.extend(data_y1)
    data_y.extend(data_y2)
    data_y.extend(data_y3)
    draw(x, y, data_x, data_y)


def spline_method(xs, ys):
    """
    启动整个计算过程
    """
    result = solutions(secondary_spline_method(xs), ys)
    get_result(xs, ys, result)
    student()


def student():
    """
    显示学号= =
    :return: 1607094239 金浩
    """
    print('made by 1607094239 金浩')


if __name__ == '__main__':
    x = [2, 4.5, 7, 8.5]
    y = [2.5, 1, 2.5, 0.4]
    spline_method(x, y)
