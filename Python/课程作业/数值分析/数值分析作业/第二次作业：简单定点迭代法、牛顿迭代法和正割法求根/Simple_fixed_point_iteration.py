import matplotlib.pyplot as plt
import numpy as np
# 存在的一些问题，使用递归完成了对单方向的简单定点求根。
# 比如该方法中我使用的函数f（x）=x^3-2x-3的根位于1.8-2.0之间，在迭代为收敛的情况下，
# 可以得出正确值，在发散的前提下只能顺利跳出，而不能扭转。
# 我试图通过一种比较蛮力的方式实现近似扭转，详情见代码注释。


# 要求根的函数 ：目标是 f（x）=x^3-2x-3
def function_composition(x):
    """函数表示和结果求值"""
    fc = (2 * x + 3)**(1/3)
    return fc


def iterations_number(nums):
    print('逐次逼近第', nums, '后求得：')


def display(output, flags):
    """打印测试结果"""
    if flags == 'estimated_value'or flags == 'ev':
        print('函数的一个根为'+str(round(output, 10)))

    if flags == 'unsolvable ' or flags == 'un':
        print("以该点迭代结果发散，无法获得根。")


def simple_fixed_point(x, acc):
    """简单定点迭代法"""
    global num
    num = num + 1
    fx = function_composition(x)
    lists.append(fx)
    draw_allways([[x, x], [x, fx]], [[x, fx], [fx, fx]])
    if num != 1 and lists[0] < fx:
        del lists[0]
        display(0, 'un')
        # ----------一种特别的解决方式，即如果不在能收敛的区间，就每次让他的
        # 绝对值扩大两倍，来使得迭代方向间接发生改变
        x = abs(2*x)
        print("改变原值"+str(x/2)+"为绝对值的两倍，即为："+str(x))
        num = 0
        simple_fixed_point(x, acc)
        # 这种方法可以在不影响不改变原先的收敛区域的情况下，用一部分效率换取更多求根区间。
        # ---------------------删除划线区域就可接触该操作。
    else:
        if (x-fx) < acc and function_composition(fx) < fx:
            iterations_number(num)
            display(x, 'ev')
        else:
            simple_fixed_point(function_composition(x), acc)


def input_limit():
    """输入定点"""
    a = float(input("请输入定点的值："))
    acc = float(input("请输入误差限的值："))
    result = [a, acc]
    return result


def main():
    """主驱动"""
    print("简单定点迭代法：f（x）=x^3-2x-3（根在1.8-2.0左右，唯一。）")
    result = input_limit()
    flag = result[0]
    simple_fixed_point(result[0],result[1])


def draw():
    """绘制函数和寻找的路径"""
    plt.title("fixed point iteration method")
    x = np.linspace(0, 10)
    y = np.linspace(0, 10)
    plt.plot(x, x)
    plt.plot(x, (2 * x + 3) ** (1 / 3), "r-")
    plt.grid(True)  # 设置网格线
    plt.show()


def draw_allways(dot1,dot2):
    """负责完成函数变换路径"""
    plt.plot(dot1[0], dot1[1])
    plt.plot(dot2[0], dot2[1])


# 开始
num = 0
flag = 0
lists = []
main()
draw()


