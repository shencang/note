class Point:
    def __init__(self, x, y, flag):
        self.x = x
        self.y = y
        self.flag = flag


def convexhull(n):
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            a = point[j].y - point[i].y
            b = point[j].x - point[i].x
            c = (point[i].x * point[j].y) - (point[i].y * point[j].x)
            sign1 = 0
            sign2 = 0
            for k in range(n):
                if k == j or k == i:
                    continue
                if a * point[k].x + b * point[k].y >= c:
                    sign1 = sign1 + 1
                if a * point[k].x + b * point[k].y <= c:
                    sign2 = sign2 - 1
            if sign1 == (n - 2) or sign2 == (2 - n):
                point[i].flag = 1
                point[j].flag = 1
            j = j + 1
        i = i + 1


# point = [Point(1, 10, 0), Point(2, 9, 0), Point(3, 8, 0), Point(4, 7, 0), Point(5, 6, 0),
#          Point(6, 5, 0), Point(7, 4, 0), Point(8, 3, 0), Point(9, 2, 0), Point(10, 1, 0),
#          Point(1, 2, 0), Point(1, 6, 0), Point(4, 3, 0), Point(5, 0, 0), Point(5, 11, 0),
#          Point(1, 5, 0), Point(0, 4, 0), Point(0, 3, 0), Point(0, 2, 0), Point(9, 1, 0)]
point = [Point(-22.5, 19.0, 0), Point(20.5, 19.0, 0), Point(27.0, 7.0, 0), Point(9.0, -16.0, 0), Point(-36.0, -10.0, 0),
         Point(-14.0, 8.0, 0), Point(9.5, 13.0, 0), Point(-8.5, -5.5, 0)]
n = len(point)
convexhull(n)

for i in range(len(point)):
    print('x', i, ':', point[i].x, ' ', point[i].y, ' ', point[i].flag)
