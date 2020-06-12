import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl


def get_parameters(choose):
    """
        选择课本的三组数据中的一组。
        4.1 一次拉格朗日插值法多项式，参数见下。求f（1.5）
        4.3 二次拉格朗日插值法多项式，参数见下。求f（1.5）
        4.14 五次拉格朗日插值法多项式，参数见下。求f（0.596）（求得是四阶可以取前五个节点，在这里取6个，效果类似，取最优）(牛顿法的值)
        4.14 五次拉格朗日插值法多项式，自测数据
    """
    global num, x, y, x_c
    if choose == 1:
        x = [1, 3]
        y = [1, 2]
        x_c = 1.5

    elif choose == 2:
        x = [1, 3, 2]
        y = [3, 6, 11]
        x_c = 1.5

    elif choose == 3:
        x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
        y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
        x_c = 0.596
    elif choose == 4:
        x = [1, 3, 5, 9, 11, 13]
        y = [1, 6, 8, 22, 7, 11]
        x_c = 2
        print('x:', x)
        print('y:', y)
        print('预测点', x_c)
    else:
        print("输入有误。请重新输入")
        lagrange_polynomial()
    num = len(x) - 1


def function_l(xs, x_f):
    """
    计算L的值，参与fx的运算
    """
    global num
    # 组合系数
    lx = [1 for num in range(len(xs))]
    i = 0
    while i < num + 1:
        j = 0
        while j < num + 1:
            if i != j:
                # 结论式：L[i]=∏(x-x[j])/(x[i]-x[j])
                lx[i] = lx[i] * ((x_f - xs[j]) / (xs[i] - xs[j]))
            j = j + 1
        i = i + 1

    return lx


def functions(xs, ys, x_f):
    """
    计算函数值
    fx= ∏lx*fx
    """
    global num
    result = 0
    i = 0
    l = function_l(xs, x_f)
    while i <= num:
        result = result + l[i] * ys[i]
        i = 1 + i
    return result


def draw(xs, ys):
    """
    画通过差商计算出来的函数的图像
       协同求点和划线
    """
    x = np.linspace(min(xs), max(xs), 99)
    plt.scatter(xs, ys, label="离散数据", color="red")
    plt.plot(x, functions(xs, ys, x), label="拉格朗日插值拟合曲线", color="black")
    plt.scatter(x_c, functions(xs, ys, x_c), label="预测函数点", color="blue")
    plt.title("拉格朗日插值法（Lagrange_polynomial）")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    plt.show()
    return functions(xs, ys, x_c)


def input_estimation_and_conditions():
    """输入初始选择"""
    print('请选择数据:\n1,为课本例题4-1的数据\n 2,为课本例题4-3的数据\n 3,为课本例题4-14的数据\n 4,为自拟数据')
    result = int(input("请输入选择"))
    return result


def lagrange_polynomial():
    """
    启动整个计算过程
    """
    # 获得x y 的取值和要计算的值
    get_parameters(input_estimation_and_conditions())
    # 计算差商+绘图
    result = draw(x, y)
    # 输出估计值和学号
    student()
    print('计算得在x=', x_c, '时，函数值近似为：', result)


def student():
    """
    显示学号= =
    :return: 1607094239 金浩
    """
    print('made by 1607094239 金浩')


if __name__ == '__main__':
    x = []
    y = []
    quotient = []
    num = 0
    lagrange_polynomial()
