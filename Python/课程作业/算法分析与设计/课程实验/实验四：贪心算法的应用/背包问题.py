# -*- coding:utf-8 -*-
class goods:
    def __init__(self, id, weight=0, value=0):
        self.id = id
        self.weight = weight
        self.value = value


def knapsack(capacity=0, goods_set=[]):
    # 按单位价值量排序
    goods_set.sort(key=lambda obj: obj.value / obj.weight, reverse=True)
    result = []
    for a_goods in goods_set:
        if capacity < a_goods.weight:
            break
        result.append(a_goods)
        capacity -= a_goods.weight
    if len(result) < len(goods_set) and capacity != 0:
        result.append(goods(a_goods.id, capacity, a_goods.value * capacity / a_goods.weight))
    return result


def display(flag, a):
    if flag == 'result' or flag == 're':
        for obj in a:
            print('物品编号:' + str(obj.id) + ' ,放入重量:' + str(obj.weight) + ',放入的价值:' + str(obj.value), end=',')
            print('单位价值量为:' + str(obj.value / obj.weight))
    if flag == 'choose' or flag == 'ch':
        for obj in a:
            print('物品编号:' + str(obj.id) + ' ,重量:' + str(obj.weight) + ',价值:' + str(obj.value), end=',')
            print('单位价值量为:' + str(obj.value / obj.weight))


def max_value(res):
    number = 0
    for obj in res:
        number = number + obj.value
    return number


def get_save():
    all_good = [goods(1, 2, 4), goods(2, 8, 6), goods(3, 5, 3), goods(4, 1, 2)
        , goods(5, 3, 7), goods(6, 4, 9), goods(7, 2, 8), goods(8, 9, 13)]
    return all_good


if __name__ == '__main__':
    all_goods = get_save()
    print("可选物品有：")
    display('ch', all_goods)
    capacity = 10
    res = knapsack(capacity, all_goods)
    print("装填中")
    display('re', res)
    print("最大价值为", max_value(res))
