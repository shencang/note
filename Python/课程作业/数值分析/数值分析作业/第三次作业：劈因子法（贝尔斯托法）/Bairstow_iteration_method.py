# Bairstow_iteration_method:贝尔斯托迭代法
# 要求根的函数 ：x^5+3*x^4-23*x^3-51*x^2+94*x+120
# 因式分解的结果为：(x+1)(x-2)(x+3)(x-4)(x+5)
import cmath as cm
import sys

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
sys.setrecursionlimit(1000000)


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


def quadratic_equation():
    fac = 4 * save_coeff[2] * save_coeff[0]
    if (fac >= 0):
        # 是二次方程的情况下求解。
        xf1 = 2 * save_coeff[3] / (-save_coeff[1] - np.sqrt(fac))
        xf2 = 2 * save_coeff[3] / (-save_coeff[1] + np.sqrt(fac))
        display(1 / xf1, 'ev')
        display(1 / xf2, 'ev')
    else:
        # 复数仍然使用正常的正除
        shi, xu = cm.polar(cm.sqrt(fac))
        xf_s = (-save_coeff[1] / (2 * save_coeff[0])) + shi / (2 * save_coeff[0])
        xf_x = xu / (2 * save_coeff[0])
        xf3 = cm.rect(xf_s, -xf_x)
        xf4 = cm.rect(xf_s, xf_x)
        display(xf3, 'cev')
        display(xf4, 'cev')


def rs_analysis():
    """计算当前r,s存入r_s"""
    # 指定为float型会在值较大时导致栈溢出
    # 每次修改r和s用于下次消减级数
    rsz = (save_b[0] * save_c[3] - save_b[1] * save_c[2])
    rsm = (save_c[2] * save_c[2] - save_c[1] * save_c[3])
    r = rsz / rsm + r_s[0]
    rsz = (save_b[0] * save_c[2] - save_b[1] * save_c[1])
    rsm = (save_c[3] * save_c[1] - save_c[2] * save_c[2])
    s = rsz / rsm + r_s[1]
    r_s[2] = round(r, 4)
    r_s[3] = round(s, 4)


def error_analysis():
    """误差分析"""
    r_s_error_analysis[0] = round((r_s[2] - r_s[0]) / r_s[2], 5)
    r_s_error_analysis[1] = round((r_s[3] - r_s[1]) / r_s[3], 5)
    r_s[0] = r_s[2]
    r_s[1] = r_s[3]


def result_b(r, s):
    """求b的值"""
    num = 3
    save_b[5] = round(save_coeff[5], 5)
    save_b[4] = round(save_coeff[4] + r * save_b[5], 5)
    while num != -1:
        save_b[num] = round(save_coeff[num] + r * save_b[num + 1] + s * save_b[num + 2], 5)
        num = num - 1


def result_c(r, s):
    """求c的值"""
    num = 3
    save_c[5] = round(save_b[5], 4)
    save_c[4] = round(save_b[4] + r * save_c[5], 4)
    while num != -1:
        save_c[num] = round(save_b[num] + r * save_c[num + 1] + s * save_c[num + 2], 5)
        num = num - 1


# 标记解的下标
lessons = 0
# 存放答案的下标
root = 0
# 标记迭代次数
count = 0
# 表示根的剩余数量
# 例子用不到，但是二次方程的求法也要写.
# 控制级次变化。
n_less = [3, 1]


def result_bairstow(r, s, acc):
    """贝尔斯托法求解"""
    global n, lessons, root, count
    count = count + 1
    result_b(r, s)
    result_c(r, s)
    rs_analysis()
    error_analysis()
    if (abs(r_s_error_analysis[0]) < acc) | (abs(r_s_error_analysis[1]) < acc):  # 误差满足条件
        display(count, 'nu')
        save_x[root] = (r_s[2] + (r_s[2] ** 2 + 4 * r_s[3]) ** (1 / 2)) / 2  # 4
        display(root, 'ro')
        root = root + 1
        save_x[root] = (r_s[2] - (r_s[2] ** 2 + 4 * r_s[3]) ** (1 / 2)) / 2  # 3
        display(root, 'ro')
        root = root + 1
        n = n_less[lessons]  # n当前计算多项式项数
        lessons = lessons + 1
        if n == 1:
            print(r_s)
            print(r_s_error_analysis)
            print(save_coeff, '= - =')
            save_x[4] = round(-(r_s[2]) / (r_s[3]), 5)  # 单项式求解 #rs的初始取值对其影响较大。
            display(4, 'ro')
            display(0, 'ar')
        elif (n == 2):
            quadratic_equation()
        elif (n > 2):  # 传入修正的r,s值  商作为因式迭代
            count = 0
            number = 0
            while number < 4:
                save_coeff[number] = save_b[number + 2]
                number = number + 1
            save_coeff[4] = 0
            save_coeff[5] = 0
            result_bairstow(r_s[2], r_s[3], acc)
    else:
        # 不满足近似条件acc
        result_bairstow(r_s[2], r_s[3], acc)
        # 用修正的值继续迭代,直到与acc匹配


def display(output, flags):
    """打印测试结果"""
    if flags == 'estimated_value' or flags == 'ev':
        print('函数的一个根为' + str(round(output, 10)))

    if flags == 'unsolvable ' or flags == 'un':
        print("以该点递归无法获得根。")

    if flags == 'number' or flags == 'nu':
        print("迭代" + str(output) + "次得到根：")

    if flags == 'root' or flags == 'ro':
        print('x', output, '=', save_x[output])

    if flags == 'all_root' or flags == 'ar':
        print('多项式的根:', save_x)

    if flags == 'complex_estimated_value' or flags == 'cev':
        print('函数的一个根为', output)


def input_estimation_and_conditions():
    """输入初始估计"""
    a = float(input("请输入估计r的值："))
    b = float(input("请输入估计s的值："))
    acc = float(input("请输入迭代满足条件的值：（小数表示的百分数）"))
    result = [a, b, acc]
    return result


def main():
    """主驱动"""
    print("贝尔斯托迭代法：f（x）=x^5+3*x^4-23*x^3-51*x^2+94*x+120")

    result_bairstow(result[0], result[1], result[2])


def draw():
    """绘制函数和寻找过程的路径"""
    plt.title('贝尔斯托迭代法图像（仅绘制实数根）')
    plt.xlabel("x")
    plt.ylabel("y")
    x = np.linspace(-10, 10, 99)
    # 绘制函数的图像
    y = x ** 5 + 3 * x ** 4 - 23 * x ** 3 - 51 * x ** 2 + 94 * x + 120
    plt.plot(x, y)
    y2 = x * 0

    plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
    for v in save_x:
        plt.scatter(v, 0, c='r')  # 每次迭代的点
    plt.show()


# 开始
num = 0
result = input_estimation_and_conditions()
# 存放系数，正序a0到a5
save_coeff = [120, 94, -51, -23, 3, 1]
save_b = ['b0', 'b1', 'b2', 'b3', 'b4', 'b5']
save_c = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5']
# 存放rs和误差
r_s = [result[0], result[1], 'r', 's']
r_s_error_analysis = ['%r', '%s']
coeff_num = len(save_coeff) - 1
save_x = ['x0', 'x1', 'x2', 'x3', 'x4']
main()
draw()
