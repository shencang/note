def knapsack(value, weight, capacity, n, choose):
    global VALUE
    for i in range(n + 1):
        VALUE[i][0] = 0
    for j in range(capacity + 1):
        VALUE[0][j] = 0
    for i in range(n):
        for j in range(capacity + 1):
            if j < weight[i]:
                VALUE[i][j] = VALUE[i - 1][j]
            else:
                VALUE[i][j] = max(VALUE[i - 1][j], (VALUE[i - 1][j - weight[i]] + value[i]))
    j = capacity
    i = n - 1
    while i >= 0:
        if VALUE[i][j] > VALUE[i - 1][j]:
            choose[i] = 1
            j = j - weight[i]
        else:
            choose[i] = 0
        i = i - 1

    display('ch', choose)
    for i in range(n):
        for j in range(capacity + 1):
            print(VALUE[i][j], '\t', end='')
            if j == capacity:
                print()

    return VALUE[n - 1][capacity]


def display(flag, a):
    if flag == 'result' or flag == 're':
        print('最佳的价值和是', a)
    if flag == 'choose' or flag == 'ch':
        print("选择结果是：", a, '(1代表选择，0代表未选择)')


VALUE = [([0] * 20) for i in range(20)]
if __name__ == '__main__':
    s_weight = [2, 2, 6, 5, 4, 3, 5, 6, 4]
    s_valve = [3, 6, 5, 4, 6, 4, 5, 7, 9]
    s_choose = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    s_n = len(s_weight)
    s_capacity = 10
    sums = knapsack(s_valve, s_weight, s_capacity, s_n, s_choose)
    display('re', sums)
