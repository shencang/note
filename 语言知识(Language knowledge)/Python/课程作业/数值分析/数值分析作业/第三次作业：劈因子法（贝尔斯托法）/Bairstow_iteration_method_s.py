# Bairstow_iteration_method:贝尔斯托迭代法
# 要求根的函数 ：x^5+3*x^4-23*x^3-51*x^2+94*x+120
# 因式分解的结果为：(x+1)(x-2)(x+3)(x-4)(x+5)
import cmath as cm

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签


# 提示
def welcome():
    print("贝尔斯托迭代法：f（x）=x^5+3*x^4-23*x^3-51*x^2+94*x+120")


# 要求根的函数 ：x^5+3*x^4-23*x^3-51*x^2+94*x+120
def function_composition(x):
    """函数表示和结果求值"""
    fc_5 = np.power(x, 5)
    fc_4 = 3 * np.power(x, 4)
    fc_3 = -21 * np.power(x, 3)
    fc_2 = -51 * np.power(x, 2)
    fc_1 = 94 * x
    fc_0 = 120
    return fc_5 + fc_4 + fc_3 + fc_2 + fc_1 + fc_0


def bairstow(a, r, s, num, acc):
    global count
    count = count + 1
    """贝尔斯托法"""
    # 没有次方计算，退出
    if num < 1:
        return None
    # 单根的情况
    if (num == 1) and (a[1] != 0):
        save_x.append(float(-a[0]) / float(a[1]))
        count = count + 1
        return None
    # 两个根的情况
    if num == 2:
        D = (a[1] ** 2.0) - (4.0) * (a[2]) * (a[0])
        X1 = (-a[1] - cm.sqrt(D)) / (2.0 * a[2])
        X2 = (-a[1] + cm.sqrt(D)) / (2.0 * a[2])
        count = count + 1
        save_x.append(X1)
        save_x.append(X2)
        return None
    # 计算bc
    n = len(a)
    b = [0] * len(a)
    c = [0] * len(a)
    b[n - 1] = a[n - 1]
    b[n - 2] = a[n - 2] + r * b[n - 1]
    i = n - 3
    while i >= 0:
        b[i] = a[i] + r * b[i + 1] + s * b[i + 2]
        i = i - 1
    c[n - 1] = b[n - 1]
    c[n - 2] = b[n - 2] + r * c[n - 1]
    i = n - 3
    while i >= 0:
        c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
        i = i - 1
    dins = ((c[2] * c[2]) - (c[3] * c[1])) ** (-1.0)
    # 计算rs
    r = r + (dins) * ((c[2]) * (-b[1]) + (-c[3]) * (-b[0]))
    s = s + (dins) * ((-c[1]) * (-b[1]) + (c[2]) * (-b[0]))
    # 和预设精确度进行比较
    if abs(b[0]) > acc or abs(b[1]) > acc:
        return bairstow(a, r, s, num, acc)
    # 多根的情况
    if num >= 3:
        diss = ((-r) ** (2.0)) - ((4.0) * (1.0) * (-s))
        X1 = (r - (cm.sqrt(diss))) / (2.0)
        X2 = (r + (cm.sqrt(diss))) / (2.0)
        count = count + 1
        save_x.append(X1)
        save_x.append(X2)
        return bairstow(b[2:], r, s, num - 2, acc)


def display(output, flags):
    """打印测试结果"""
    if flags == 'estimated_value' or flags == 'ev':
        print('函数的一个根为' + str(round(output, 10)))

    if flags == 'unsolvable ' or flags == 'un':
        print("以该点递归无法获得根。")

    if flags == 'number' or flags == 'nu':
        print("共计迭代" + str(output) + "次得到根：")

    if flags == 'root' or flags == 'ro':
        print('x', output, '=', save_x[output])

    if flags == 'all_root' or flags == 'ar':
        n = 0
        display(count, 'nu')
        while n <= coeff_num - 1:
            print('x', n, ':=', str(save_x[n]))
            n = n + 1

    if flags == 'complex_estimated_value' or flags == 'cev':
        print('函数的一个根为', output)


def input_estimation_and_conditions():
    """输入初始估计"""
    welcome()
    a = float(input("请输入估计r的值："))
    b = float(input("请输入估计s的值："))
    acc = float(input("请输入迭代满足条件的值：（小数表示的百分数）"))
    result = [a, b, acc]
    return result


def main():
    """主驱动"""
    # print("贝尔斯托迭代法：f（x）=x^5+3*x^4-23*x^3-51*x^2+94*x+120")
    bairstow(save_coeff, result[0], result[1], coeff_num, result[2])
    display(0, 'ar')


def draw():
    """绘制函数和寻找过程的路径"""
    plt.title('贝尔斯托迭代法图像（仅绘制实数根）')
    plt.xlabel("x")
    plt.ylabel("y")
    x = np.linspace(-5, 5, 99)
    # 绘制函数的图像
    y = x ** 5 + 3 * x ** 4 - 23 * x ** 3 - 51 * x ** 2 + 94 * x + 120
    plt.plot(x, y)
    y2 = x * 0
    plt.plot(x, y2, color='Orange', linewidth=1.0, linestyle='--')
    for v in save_x:
        plt.scatter(v, 0, c='r')  # 每次迭代的点
    plt.show()


# 开始
# 标记迭代次数
count = 0
result = input_estimation_and_conditions()
# 存放系数，正序a0到a5
save_coeff = [120, 94, -51, -23, 3, 1]
coeff_num = len(save_coeff) - 1

save_x = []
main()
draw()
