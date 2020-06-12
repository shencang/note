import matplotlib.pyplot as plt
import numpy as np


# 修恩法修改自我的欧拉法。我将欧拉法的无关步骤和欧拉法计算分离，使其独立不随方法修改而变动，故在修恩法中，我只修改对应的部分。
# 所以在欧拉法和修恩法中，除去必要步骤外大部分代码来自欧拉法。

def exact_solution(x):
    """
    求函数的精确值
    :param x: 要求函数值的x的值
    :return: 对应函数值
    """
    fc = -0.5 * pow(x, 4) + 4 * pow(x, 3) - 10 * pow(x, 2) + 8.5 * x + 1
    return fc


def estimated_results(x):
    """
    求函数的导数值
    :param x:要求导数值的x的值
    :return:对应导数值
    """
    fc = -2 * pow(x, 3) + 12 * pow(x, 2) - 20 * pow(x, 1) + 8.5
    return fc


def input_estimation_and_conditions():
    """
    入口方法
    :return:输入的起始点和结束点与步长
    """
    print("步长输入0退出系统")
    x_begin = float(input("==============================\n请输入起始点"))
    x_end = float(input("==============================\n请输入终点"))
    h = float(input("==============================\n请输入步长"))
    # 整理出真正的起始和终点,和正整数步长
    return min(x_begin, x_end), max(x_begin, x_end), abs(h)


def swap(cha, chb):
    """
    交换两个数的值
    :param cha: 系数矩阵
    :param chb: 结果矩阵
    :return:两个交换的值
    """
    return chb, cha


def exact_value(x_h_add):
    """
    计算函数对应x的精确值
    :param x_h_add: x的每次取值
    :return: 精确的函数值集合
    """
    # 精确点结果集
    result_n = []
    # 直到长度到达末尾
    for i in x_h_add:
        # 记录当前x的精确解
        result_n.append(exact_solution(i))
    return result_n


def xien_method(x_begin, x_end, h):
    """
    修恩法计算对应的估计点：yi+1=yi+Φh
    :param x_begin:起始点
    :param x_end:结束点
    :param h:步长
    :return:估计值和x的取值集合
    """
    # 估计点结果集
    results = []
    # 每次步长计算后的点集
    x_h_add = []
    # 初始点的值由精确值导出，作为修恩法的开始，也就是y0
    results.append(exact_solution(x_begin))
    # 起始点加入结果集合
    i = x_begin
    # 直到长度到达末尾
    while i <= x_end:
        # 分别记录当前x的值，估计解
        x_h_add.append(i)
        temp_fx = estimated_results(i + h)
        # yi+1=yi+Φh
        results.append(results[-1] + (estimated_results(i) + temp_fx / 2) * h)
        # 步进
        i = i + h

    return results, x_h_add


def draw(results, result_n, x_h_add):
    """
    修恩法绘图步骤
    :param results: 估计函数值集合
    :param result_n: 精确函数值集合
    :param x_h_add: x的取值集合
    :return: 无
    """
    plt.title("修恩法")
    # 确定x轴的范围，建议不要太大
    x = np.linspace(min(x_h_add), max(x_h_add))
    # 绘制原始函数曲线
    plt.plot(x, -0.5 * (x ** 4) + 4 * (x ** 3) - 10 * (x ** 2) + 8.5 * x + 1, label="原始函数曲线", color="red")
    # 绘制函数点包括估计点和精确点
    for i in range(len(result_n) - 1):
        plt.scatter(x_h_add[i], result_n[i], color="blue")
        plt.scatter(x_h_add[i], results[i], color="green")
    # 最后两个点单独绘制，用于显示注解信息
    plt.scatter(x_h_add[len(result_n) - 1],
                result_n[len(result_n) - 1],
                label="步进点的精确值",
                color="blue")
    plt.scatter(x_h_add[len(result_n) - 1],
                results[len(result_n) - 1],
                label="步进点的估计值（" + str(x_h_add[1] - x_h_add[0]) + "步长）",
                color="green")
    # 绘制函数估计曲线
    for i in range(len(result_n) - 1):
        plt.plot([x_h_add[i], x_h_add[i + 1]], [results[i], results[i + 1]], color="black")
    # 最后两个点单独绘制短线，用于显示注解信息
    plt.plot([x_h_add[len(result_n) - 2], x_h_add[len(result_n) - 1]],
             [results[len(result_n) - 2], results[len(result_n) - 1]], label="估计曲线", color="black")
    # 输入中文和正确负号
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    plt.grid(True)
    # 设置网格线
    plt.show()


def student():
    """
    显示学号= =
    :return: 1607094239 金浩
    """
    print('made by 1607094239 金浩')


def begin():
    """
    启动方法
    :return: 没有
    """
    # 得到系数和结果矩阵
    x_begin, x_end, h = input_estimation_and_conditions()
    # 错误输入时推出
    if h == 0:
        exit(0)
    # 修恩法计算各个点的估计值
    results, x_h_add = xien_method(x_begin, x_end, h)
    # 计算对应的精确函数值
    result_n = exact_value(x_h_add)
    # 画图
    draw(results, result_n, x_h_add)
    # 学号输出
    student()


if __name__ == '__main__':
    begin()
