# 描述
# 对于给定的算术表达式，按规则输出计算结果，仅包含加法和大小判断。
# 输入
#
# 一行字符串，为加号、大于、小于( + < > ) 连接的两个不限大小的非负整数。
#
# 输出
#
# 当符号为 + 时, 计算两个数相加的和, 并以字符串格式返回； 当符号为 < 时, 如果左数小于右数, 返回大写字母字符 Y, 否则返回大写字母字符 N； 当符号为 > 时, 如果左数大于右数, 返回大写字母字符 Y, 否则返回大写字母字符 N。
# !!!请同学们尽量使用算法来解决这个问题
#
# 输入样例
# 972919822976663297>74058
# 875098336507333719633571722631534917759993913379786689>53558270653237768027942884431075534537929401567824882097903948774409200
# 7625022925148127196027859399571498914361+790786706794530
#  复制样例
# 输出样例
# Y
# N
# 7625022925148127196027860190358205708891

import sys


def solution(line):
    if line.count('+') > 0:

        a, b = line.split('+')
        #      print(a," ",b)

        result = 0

        a_r = a[::-1]

        b_r = b[::-1]
        #      print(a_r," ",b_r)
        sum_digit = min(len(a_r), len(b_r))
        #     print(sum_digit)
        level = 1

        for i in range(sum_digit):
            x = int(a_r[i])

            y = int(b_r[i])

            result = result + (x + y) * level

            level *= 10

        if len(a_r) > sum_digit:

            for d in a_r[sum_digit:]:
                result = result + int(d) * level

                level *= 10

        else:

            for d in b_r[sum_digit:]:
                result = result + int(d) * level

                level *= 10

        return result

    elif line.count('<') > 0:

        small, big = line.split('<')

    elif line.count('>') > 0:

        big, small = line.split('>')

    if len(big) > len(small):
        return 'Y'

    if len(big) < len(small):
        return 'N'

    for i in range(len(big)):

        if big[i] > small[i]:
            return 'Y'

        if big[i] < small[i]:
            return 'N'

    return 'N'


if __name__ == '__main__':
    for line in sys.stdin:
        lines = line.split('\n')
        print(solution(lines[0]))
