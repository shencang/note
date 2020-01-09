import numpy as np


def get_parameters(choose):
    """
        选择课本的三组数据中的一组。
        1.自拟
        2.ppt数据
        3.课本3-8数据，也是课上用的数据
    """
    if choose == 1:
        inpa = [[6, 15, 55],
                [15, 55, 225],
                [55, 225, 979]]
        inpb = [152.6, 585.6, 2488.8]
        return inpa, inpb

    elif choose == 2:
        inpa = [[1, 2, -3],
                [0, 5, 2],
                [-2, 0, -3]]
        inpb = [8, -4, 2]
        return inpa, inpb
    elif choose == 3:
        inpa = [[2, 2, 3],
                [4, 7, 7],
                [-2, 4, 5]]
        inpb = [3, 1, -7]
        return inpa, inpb
    else:
        print("输入有误。请重新输入")
        begin()
        return 0, 0


def input_estimation_and_conditions():
    """
    选择参数
    :return:选择的结果
    """
    print('请选择数据:\n---------->1,自拟数据:'
          '\na = \n[ 6,  15,  55]\n'
          '[15,  55, 225]\n'
          '[55, 225, 979]\n'
          'b = \n[152.6, 585.6, 2488.8]'
          '\n---------->2,ppt的数据:'
          '\na = \n[ 1, 2,-3]\n'
          '[ 0, 5, 2]\n'
          '[-2, 0,-3]\n'
          'b = \n[ 8,-4, 2]',
          '\n---------->3,例题3-8的数据:'
          '\na = \n[ 2, 2,3]\n'
          '[ 4, 7, 7]\n'
          '[-2, 4,5]\n'
          'b = \n[ 3,1, -7]')
    result = int(input("==============================\n请输入选择"))
    return result


def swap(cha, chb):
    """
    交换两个数的值
    :param cha: 系数矩阵
    :param chb: 结果矩阵
    :return:两个交换的值
    """
    return chb, cha


def exchange_principal(a, b):
    """
    对ab进行交互主元
    :param a: 系数矩阵
    :param b: 结果矩阵
    :return: 交换主元后的a和b
    """
    maxs = a[1][1]
    j = 0
    # 找出最大元素
    for i in range(2, len(a)):
        if abs(a[i][1]) > maxs:
            maxs = abs(a[i][1])
            j = i
    # 交换主要元素后，其他元素相应变换
    for n in range(1, len(a)):
        a[1][n], a[j][n] = swap(a[1][n], a[j][n])
    b[1][0], b[j][0] = swap(b[1][0], b[j][0])
    return a, b


def count_LU(a, l, u):
    """
    计算L和U方阵,优化于原始高斯消去，不同于原来的添加0行0列，直接计算
    :param a: 系数矩阵
    :param l: 经过初始化的L方阵
    :param u: 经过初始化的U方阵
    :return: 填充完毕的L,U方阵
    """
    n = len(a)
    for i in range(n):
        # 计算L的第一列和U的第一行：U1i=A1i, Li1=Ai1 / U11
        u[0][i] = a[0][i]
        l[i][0] = a[i][0] / u[0][0]
    # 计算U的第r行，L的第r列元素
    # uri=ari-Σ(k=1->r-1)Lrk_Uki
    # lir=air-Σ(k=1->r-1)Lik_Ukr
    for r in range(n):
        for i in range(r, n):
            u[r][i] = a[r][i] - sum_Lr_Ui(l, u, r, i)
            if i == r:
                l[r][r] = 1
            elif r == n:
                l[n][n] = 1
            else:
                l[i][r] = (a[i][r] - sum_Li_Ur(l, u, r, i)) / u[r][r]
    return l, u


def sum_Lr_Ui(l, u, r, i):
    """
    求和:Lrk*Uki
    :param l:计算中的L矩阵
    :param u:计算中的U矩阵
    :param r:控制行列
    :param i:控制行列
    :return:计算结果
    """
    result = 0.0
    for k in range(r):
        result = result + l[r][k] * u[k][i]
    return result


def sum_Li_Ur(l, u, r, i):
    """
    求和:Lrk*Uki
    :param l:计算中的L矩阵
    :param u:计算中的U矩阵
    :param r:控制行列
    :param i:控制行列
    :return:计算结果
    """
    result = 0.0
    for k in range(r):
        result = result + l[i][k] * u[k][r]
    return result


def result_of_d_x(l, u, b):
    """
    处理L，U计算D并根据B算出结果值
    :param l: 计算完毕的L矩阵
    :param u: 计算完毕的U矩阵
    :param b: 方程的右边集合
    :return: 解出的x的解集
    """
    # 规范化L
    lss = np.array(l)
    # 规范化U
    us = np.array(u)
    # 规范化B
    bb = [b[0]], [b[1]], [b[2]]
    bsa = np.array(bb)
    # 计算D,[L]{D}={B}
    # d= np.dot(lss.T,bsa)
    d = np.linalg.solve(l, bsa)
    # 计算X,[U]{X}={D}
    # x= np.dot(us.T,d)
    x = np.linalg.solve(us, d)
    return x


def get_new_LU(inpas):
    """
    初始化L和U阵。
    :param inpas:系数矩阵
    :return: 初始化的L和U阵
    """
    l_n = []
    u_n = []
    # 确定初始化的宽度
    for i in range(len(inpas)):
        temp = []
        # 确定初始化的行数
        for j in range(len(inpas)):
            # 为这一列添加0值。不用append()避免复制错误
            temp.insert(-1, 0)
        # 注入每一行。在这里原来没有重复两个循环，直接temp给l和u赋值，导致构成地址引用而不是值覆盖，导致错误
        l_n.insert(-1, temp)
    # 重复上述操作
    for i in range(len(inpas)):
        temp = []
        for j in range(len(inpas)):
            temp.insert(-1, 0)
        u_n.insert(-1, temp)

    return l_n, u_n


def draw(lr, ur):
    """
    画图画图
    :param a:
    :param b:
    :return:
    """
    # 不会画·····
    # image = Image.fromarray(lr)
    # img = imread(image)


def student():
    """
    显示学号= =
    :return: 1607094239 金浩
    """
    print('made by 1607094239 金浩')


def result(x):
    """
    输出结果
    :param x:
    :return:
    """
    print("解集为：")
    for i in range(len(x)):
        print('x', i, '=', x[i])


def begin():
    """
    启动方法
    :return: 没有
    """
    # 得到系数和结果矩阵
    inp_a, inp_b = get_parameters(input_estimation_and_conditions())
    # 错误输入时推出
    if inp_a == inp_b and inp_a == 0:
        exit(0)

    # 初始化L和U阵
    l_n, u_n = get_new_LU(inp_a)
    # 拆分L和U阵
    l_r, u_r = count_LU(inp_a, l_n, u_n)
    # 根据L和U计算D，从而计算X
    xr = result_of_d_x(l_r, u_r, inp_b)
    # 画图
    draw(l_r, u_r)
    # 学号输出
    student()
    # 结果输出
    result(xr)


if __name__ == '__main__':
    begin()
