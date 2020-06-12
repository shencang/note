def maxSun(list_a):
    res = 0
    b = 0
    for i in range(len(list_a)):
        b = max(b + list_a[i], list_a[i])
        if b > res:
            res = b
    return res


def display(flag, a):
    if flag == 'result' or flag == 're':
        print('结果是', a)
    if flag == 'choose' or flag == 'ch':
        print("选择结果是：", a, '(1代表选择，0代表未选择)')


VALUE = [([0] * 20) for i in range(20)]
if __name__ == '__main__':
    a = [1, 2, 4, 5, 6, 7, 8, 9, 11, 11, 23, 45, -1]

    sums = maxSun(a)
    display('re', sums)
