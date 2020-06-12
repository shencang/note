# 4.1 遍历整个列表

magicians = ['qq','aiai','cc','ee','adse','xxz','xcd']
for magician in magicians:
    print(magician)
    print("--------")
print("=======================")

# 4.1.2 在for循环中执行更多的操作

magicians = ['qq','aiai','cc','ee','adse','xxz','xcd']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick ,"+magician.title()+'.\n')
    print("--------")
print("=======================")

# 4.2 主要是试错，就不复现了

# 4.3 创建数值列表

for value in range(0,10):
    print(value)

number = list(range(0,10))
print(number)

even_number = list(range(2,11,1))
print(even_number)

# 乘方符号
squares =[]
for values in range(0,10):
    square=values**2
    squares.append(square)

print(squares)

# 4.3.3 对数字列表执行简单的统计计算

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


# 4.3.4 列表解析
squaress =[valuess**2 for valuess in range(0,12)]
print(squaress)


# 4.4.1 切片
players = [1,2,3,4,5]
print(players[1:3])
print(players[:3])
print(players[1:])
# [:] 可以用来复制的列表
# 但是直接列表赋值是地址传值

# 元组
sd =(100,20)
print()