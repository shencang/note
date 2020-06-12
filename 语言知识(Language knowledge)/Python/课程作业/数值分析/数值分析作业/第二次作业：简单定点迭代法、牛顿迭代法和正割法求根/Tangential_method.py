import matplotlib.pyplot as plt
import numpy as np

# 简单定点迭代法使用递归来做出现了一部分问题。
# 在正割（弦截）法中，使用循环来完成。
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 要求根的函数 ：目标是 f（x）=x^3-2x-3
def function_composition(x):
    """函数结果求值"""
    fc = pow(x, 3) - 2 * x - 3
    return fc


# 要求根的导数 ：3x^2-2
def derivative_solution(x):
    """导数结果求值"""
    ds = 3 * pow(x, 2) - 2
    return ds


def iterations_number(nums):
    print('逐次逼近第', nums, '后求得：')


def display(output, flags):
    """打印测试结果"""
    if flags == 'estimated_value' or flags == 'ev':
        print('函数的一个根为' + str(round(output, 10)))

    if flags == 'unsolvable ' or flags == 'un':
        print("以该点递归无法获得根。")


def tangential_method(x,x_old, acc):
    """正割（弦截）法"""
    global num
    tag = True
    # 每次开始的x的值
    lists_save_x = []
    # 每次迭代之后的新值即，x+1
    lists_savex_new = []
    # 该点的函数计算值
    lists_fc = []

    lists_save_x.append(x_old)
    lists_fc.append(function_composition(x_old))
    # lists_save_x.append(x)
    # lists_fc.append(function_composition(x))
    while tag:
        xi = x
        if num != 0:
            x_old = lists_save_x[-1]
        fxi = function_composition(xi)
        fx_old = function_composition(x_old)
        xii = xi - ((fxi*(x_old-xi)) / (fx_old-fxi))
        lists_save_x.append(xi)
        lists_fc.append(function_composition(xi))
        # 误差限度：新-旧/新
        if (abs(xii - xi) / xii) < acc:
            iterations_number(num)
            display(xi, 'ev')
            tag = False
        else:
            x = xii
            lists_savex_new.append(xii)
            num = num + 1
    draw(lists_save_x, lists_savex_new, lists_fc)


def input_limit():
    """输入定点"""
    a = float(input("请输入定点a的值："))
    b = float(input("请输入定点b的值："))
    acc = float(input("请输入误差限的值："))
    result = [a, b, acc]
    return result


def main():
    """主驱动"""
    print("正割（弦截）法：f（x）=x^3-2x-3（根在1.8-2.0左右，唯一。）")
    result = input_limit()
    flag = result[0]
    tangential_method(result[0], result[1], result[2])


def draw(lists_x, lists_new, lists_fc):
    """绘制函数和寻找过程的路径"""
    plt.title("tangential_method")
    plt.plot([lists_x[1],lists_x[1]],[0,function_composition(lists_x[1])],c='r')
    x = np.arange(0, max(lists_x), 0.01)
    y = np.power(x, 3) - 2 * x - 3
    plt.plot(x, y)
    plt.axis([0, max(lists_x), 0, max(lists_fc)])
    plt.plot([lists_x[0], lists_x[0]], [[lists_x[0]], [lists_fc[0]]])
    for i in range(len(lists_x)):
        plt.scatter(lists_x[i], 0, c='r')
    for i in range(len(lists_new)):
        plt.plot([lists_x[i], lists_new[i], lists_new[i]], [lists_fc[i], 0, lists_fc[i+2]], c='r')
    # 设置网格线
    plt.grid(True)
    plt.show()


# 开始
num = 0
flag = 0
main()
# draw()


