# -*- coding:utf-8 -*-


def greedy_selector(s, f, a):
    n = len(s) - 1
    a[1] = True
    j = 1
    count = 1
    i = 2
    while i <= n:
        if s[i] > f[j]:
            a[i] = True
            j = i
            count = count + 1
        else:
            a[i] = False
        i = i + 1
    return count


def get_save():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 9, 10, 11]
    f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    return s, f


if __name__ == '__main__':
    s, f = get_save()
    a = [False, False, False, False, False,
         False, False, False, False, False,
         False, False]
    print(greedy_selector(s, f, a))
