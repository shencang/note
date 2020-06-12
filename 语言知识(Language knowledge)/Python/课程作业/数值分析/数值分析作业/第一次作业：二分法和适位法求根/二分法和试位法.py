import math

import matplotlib.pyplot as plt
import numpy as np


# 要求根的函数 ：目前是 f（x）=x^2+30x+15
def function_composition(x):
    """函数表示和结果求值"""
    fc = math.pow(x, 2) + x * 30 + 15
    return fc


def display(output, flag):
    """打印测试结果"""
    # 两种可能性
    if flag == 'true_value'or flag == 'tv':
        print("零点的准确坐标为：" + str(output))

    if flag == 'estimated_value'or flag == 'ev':
        print("零点的估计坐标为：" + str(output))

    if flag == 'unsolvable ' or flag == 'un':
        print("该区间内无解。")


def bisection_method(a, b, acc):
    """二分法"""
    tag = True
    if function_composition(a)*function_composition(b) > 0:
        display(0,'un')
    else:
        while tag:
            if function_composition(a)*function_composition(b) == 0.0:
                if function_composition(a) == 0.0:
                    display(a, 'tv')
                    tag = False
                else:
                    display(b, 'tv')
                    tag = False
                break
            else:
                mid = (a+b)/2
                lists.append(mid)
                if abs(b-a) < acc:
                    display(mid, 'ev')
                    tag = False
                    break
                else:
                    if function_composition(a)*function_composition(mid) > 0:
                        a = mid
                    else:
                        b = mid
    print("Bisection method 二分法结束。")


def false_position(a, b, acc):
    """试位法"""
    tag = True
    if function_composition(a) * function_composition(b) > 0:
        display(0,'un')
    else:
        # 直接写一个表达式太长，不符合规范
        fa = float(function_composition(a))
        fb = float(function_composition(b))
        intersection = float((fb * a + fa * b) / (fa + fb))
        while tag:
            if function_composition(intersection) == 0:
                display(intersection, 'ev')
            if function_composition(intersection) * function_composition(a) < 0:
                b = intersection
            else:
                a = intersection
            lists.append(intersection)
            old_intersection = intersection
            # 同上，直接写一个表达式太长，不符合规范
            fa = float(function_composition(a))
            fb = float(function_composition(b))
            intersection = float((fb * a + fa * b) / (fa + fb))
            if abs((intersection - old_intersection) / intersection) < acc:
                display(intersection, 'ev')
                tag = False

    print("False Position 适位法结束。")


def input_limit():
    """输入左右端点"""
    a = float(input("请输入左端点的值："))
    b = float(input("请输入右端点的值："))
    acc = float(input("请输入精确度："))
    back = [a, b, acc]
    return back


def main():
    """驱动与选择"""
    choose = int(input("请输入执行二分法还是适位法，1选择二分法 2选择试位法,0退出"+'\n 输入：'))
    if int(choose) == 1:
        print("二分法")
        limit=input_limit()
        bisection_method(limit[0], limit[1], limit[2])

    if int(choose) == 0:
        exit()

    if int(choose) == 2:
        print("试位法")
        limit = input_limit()
        false_position(limit[0], limit[1], limit[2])


def draw():
    """绘制函数和寻找的路径"""
    plt.title('Function image')
    plt.xlabel("x")
    plt.ylabel("y")
    x = np.linspace(-10, 10, 99)
    # 绘制函数的图像
    y = x ** 2 - 30 * x + 15
    plt.plot(x, y)
    y2 = x*0

    plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
    for v in lists:
        plt.scatter(v, 0, c='r')  # 每次迭代的点
    plt.show()


# 这样不安全，仅在此处为循环入口使用
    # 开始的入口
lists = []
main()
draw()


# 一些总结：二分法通用性较好，试位法在我测试三次方程时，由于平滑曲线的问题
# 总是出现试位法无法获得正确结果的问题。
# 图像是反应每次的取点和对应区间的函数图像。

