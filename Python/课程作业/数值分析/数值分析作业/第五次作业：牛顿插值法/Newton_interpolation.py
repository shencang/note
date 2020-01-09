import matplotlib.pyplot as plt
from pylab import mpl


def get_parameters(choose):
    """
        选择课本的三组数据中的一组。
        4.12 二次牛顿插值多项式，参数见下。求f（1.5）
        4.13 三次牛顿插值多项式，参数见下。求f（0.5）
        4.14 五次牛顿插值多项式，参数见下。求f（0.596）（求得是四阶可以取前五个节点，在这里取6个，效果类似，取最优）
    """
    global x, y, x_c
    if choose == 1:
        x_c = 1.5
        x = [1, 3, 2]
        y = [1, 2, -1]

    elif choose == 2:
        x_c = 0.5
        x = [0, 1, 2, 4]
        y = [3, 6, 11, 51]

    elif choose == 3:
        x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
        y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
        x_c = 0.596
    else:
        print("输入有误。请重新输入")
        newton_interpolation()
        # 可以直接计算n阶
        # 但是没有数据，不保留键入入口。 保留程序入口


def din_quotient():
    """
    存放差商值的临时空间
    """
    for i in range(len(x) + 1):
        quotient.append(0)


def n_difference_quotient():
    """
    通过递归计算差商，可求n阶
    """
    global quotient
    # i记录计算差商的次数
    i = 0
    while i < len(x) - 1:
        j = len(x) - 1
        while j > i:
            if i == 0:
                quotient[j] = ((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
            else:
                quotient[j] = (quotient[j] - quotient[j - 1]) / (x[j] - x[j - 1 - i])
            j -= 1
        i += 1
    return quotient


def functions(parameters, data, order):
    """
    计算函数值
    经过改进可以计算n阶！
    注释内容为之前的写法。用于是直观理解。
    """
    result = 0
    sums = 1
    for i in range(order):
        for j in range(i + 1):
            sums = sums * (data - x[j])
        sums = sums * parameters[i + 1]
        result = result + sums
        sums = 1
    result = result + y[0]
    return result
    # if order == 2:
    #     return (y[0] +
    #             parameters[1] * (data - x[0]) +
    #             parameters[2] * (data - x[0]) * (data - x[1]))

    #     return (y[0] +
    #             parameters[1] * (data - x[0]) +
    #             parameters[2] * (data - x[0]) * (data - x[1]) +
    #             parameters[3] * (data - x[0]) * (data - x[1]) * (data - x[2]))
    # if order == 5:
    #         parameters[1] * (data - x[0]) +
    #         parameters[2] * (data - x[0]) * (data - x[1]) +
    #         parameters[3] * (data - x[0]) * (data - x[1]) * (data - x[2]) +
    #         parameters[4] * (data - x[0]) * (data - x[1]) * (data - x[2]) * (data - x[3])+
    #         parameters[5] * (data - x[0]) * (data - x[1]) * (data - x[2]) * (data - x[3])*(data - x[4]))


def calculate_data(parameters):
    """通过拟合曲线计算近似解"""
    return_data = []
    for data in x:
        return_data.append(functions(parameters, data, len(x) - 1))
    return return_data


def draw(parameters, new_data):
    """画通过差商计算出来的函数的图像
       new_data是曲线拟合后的曲线
       （二阶情况下比较失准····）
    """
    plt.scatter(x, y, label="离散数据", color="red")
    plt.plot(x, new_data, label="牛顿插值拟合曲线", color="black")
    plt.scatter(x_c, functions(parameters, x_c, len(x) - 1), label="预测函数点", color="blue")
    plt.title("牛顿插值法（newton interpolation）")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    plt.show()


def input_estimation_and_conditions():
    """输入初始选择"""
    print('请选择数据:1,为课本例题4-12的数据\n 2,为课本例题4-13的数据\n 3,为课本例题4-14的数据')
    result = int(input("请输入选择"))
    return result


def newton_interpolation():
    """
    启动整个计算过程
    """
    # 获得x y 的取值和要计算的值
    get_parameters(input_estimation_and_conditions())
    # 计算差商
    din_quotient()
    parameters = n_difference_quotient()
    # 以差商算出的公式计算大致对应点，用于绘图
    predictive_value = calculate_data(parameters)
    # 绘图
    draw(parameters, predictive_value)
    # 输出估计值
    student()
    print('计算得在x=', x_c, '时，函数值近似为：', functions(parameters, x_c, len(x) - 1))


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
    x_c = 0
    newton_interpolation()
