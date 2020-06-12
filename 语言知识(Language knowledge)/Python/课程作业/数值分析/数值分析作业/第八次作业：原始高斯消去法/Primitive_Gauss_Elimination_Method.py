import numpy as np


def get_parameters(choose):
    """
        选择课本的三组数据中的一组。
        1.自拟
        2.ppt数据
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
          'b = \n[ 8,-4, 2]')
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


def obtain_the_standard_of_ab(a, b):
    """
    对初始矩阵进行处理添加0行0列
    :param a: 系数矩阵
    :param b: 结果矩阵
    :return: 修改后的系数和结果矩阵
    """
    add_h = []
    add_w = []
    # 在结果矩阵第一个位置插入一个0，代表新行
    b.insert(0, 0)
    bs = np.array([b])
    # 转置
    bs = bs.T
    # 表中元素转换为浮点型
    bs = bs.astype('float')
    # 生成新的行和列，对应到矩阵的第0行0列
    for nu in range(len(a)):
        add_h.append(0)
    for nu in range(len(a) + 1):
        add_w.append([0])
    # 插入操作
    ins = np.array([add_h])
    a = np.r_[ins, a]
    a = np.hstack((add_w, a))
    # 表中元素转换为浮点型
    a = a.astype('float')
    return a, bs


def gauss_elimination_method(inp, b):
    """
    原始高斯消去法
    :param inp: 系数矩阵
    :param b: 结果矩阵
    :return: 解集
    """
    # 判断是否需要交换主元
    if inp[1][1] == 0:
        a, b = exchange_principal(inp, b)
    n = len(inp) - 1
    x = []
    # 控制行的移动
    for k in range(1, n):
        # 消去主元对应的其他行的对应变量
        for i in range(k + 1, n + 1):
            factor = inp[i][k] / inp[k][k]
            # 处理列，计算一行内消去主元对应变量后面排列的其他变量的系数和等号右边的常数
            for j in range(k + 1, n + 1):
                inp[i][j] = inp[i][j] - factor * inp[k][j]
            b[i] = b[i] - factor * b[k]
    # 为解集开辟位置
    for ns in range(n + 1):
        x.append(0)
    x[n] = (b[n] / inp[n][n])
    i = n - 1
    # 开始储存解集
    while i > 0:
        sums = b[i]
        j = i + 1
        while j < n + 1:
            sums = sums - inp[i][j] * x[j]
            j = j + 1
        # 保存解集
        x[i] = sums / inp[i][i]
        i = i - 1
    return x


def draw(a, b):
    """
    画图画图
    :param a:
    :param b:
    :return:
    """
    # 不会画·····


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
    for i in range(1, len(x)):
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
    # 格式化ab
    a, b = obtain_the_standard_of_ab(inp_a, inp_b)
    # 高斯消元
    x = gauss_elimination_method(a, b)
    # 画图
    draw(a, b)
    # 学号输出
    student()
    result(x)


if __name__ == '__main__':
    begin()