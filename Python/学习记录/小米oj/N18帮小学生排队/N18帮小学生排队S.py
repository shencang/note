# 描述
# 用一个数组表示一群正在排队的小学生，每个小学生用一对整数 H, K 来表示：H 表示这个小学生的身高，K 表示这个小学生前面应该有 K 个人的身高 >= 他。
# 写一个算法，对给出的一组小学生计算出符合描述的正确排序。
# 输入
#
# 输入为一组整数，以空格分隔：
# 第 1 个数字表示小学生的数量 n；
# 从第 2 个数字起，后续的数字两两一组，分别代表每个小学生的 H 和 K 的值：
# H1 K1 H2 K2⋯Hn KnH_1\text{ }K_1\text{ }H_2\text{ }K_2 \cdots H_n\text{ }K_n
# H
# 1
# ​
#
#  K
# 1
# ​
#
#  H
# 2
# ​
#
#  K
# 2
# ​
#
# ⋯H
# n
# ​
#
#  K
# n
# ​
#
# .
#
# 输出
#
# 根据输入，按照题目要求对小学生进行排序，每个小学生对应的 H 和 K 值为一组，按组输出，数字间使用空格分隔。比如
# H1′ K1′ H2′ K2′⋯Hn′ Kn′H_1&#x27;\text{ }K_1&#x27;\text{ }H_2&#x27;\text{ }K_2&#x27; \cdots H_n&#x27; \text{ }K_n&#x27;
# H
# 1
# ′
# ​
#
#  K
# 1
# ′
# ​
#
#  H
# 2
# ′
# ​
#
#  K
# 2
# ′
# ​
#
# ⋯H
# n
# ′
# ​
#
#  K
# n
# ′
# ​
import sys
import sys


def solution(line):
    number_array = list(map(int, line.split()))
    child_num = number_array.pop(0)
    children = [(H, K) for H, K in zip(number_array[::2], number_array[1::2])]

    children_dict = {}
    height_list = []
    for i in range(child_num):
        child = children[i]
        if child[0] in children_dict:
            children_dict[child[0]] += [(child[1], i)]
        else:
            children_dict[child[0]] = [(child[1], i)]
            height_list.append(child[0])
    res = []
    height_list.sort(reverse=True)
    for height in height_list:
        children_dict[height].sort()
        for item in children_dict[height]:
            res.insert(item[0], children[item[1]])
    res = [str(i) for k in res for i in k]
    return " ".join(res)


for line in sys.stdin:
    line = line.strip()
    print(solution(line))
