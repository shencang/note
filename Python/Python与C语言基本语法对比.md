# Python与C语言基本语法对比

Python使用空格来限制代码的作用域，相当于C语言的 {}。

第一个程序 Hello,World!
C语言

```c
#include<stdio.h>
int main(){
    printf("Hello,World!");
return 0;
}
```

Python

```python
print("Hello,World!")
```

怎么样，是不是已经感受到Python的精巧了呢。

输入输出
C语言

```c
#include<stdio.h>
int main(){
int number;  
float decimal;
char string[20];
    scanf("%d",&number);

    scanf("%f",&decimal);
    scanf("%s", string);


    printf("%d\n", number);
    printf("%f\n",=decimal);

    printf("%s\n", String);

return 0;
}
```

Python

```py

number =int(input())
decimal=float(input())
string=input()
print(number)
print(decimal)
print(string)
```

如果你尝试自己写一个Python循环输出语句，你肯定会发现Python的输出默认的换行的，如果不想让它换行，可给 end参数复制 ""，例如

连续输出不换行

```py
for i in range(0, 10):
   print(i, end="")
```

C语言

```c
#include<stdio.h>

int main()
{

//    printf("注释一行");

    /**
    printf("注释多行");
    printf("注释多行");
    printf("注释多行");
    printf("注释多行");
    **/
}

```

Python

```py
# print("注释一行")
1.
2.# 三个单引号
3.'''
4.print("单引号注释多行")
5.print("单引号注释多行")
6.print("单引号注释多行")
7.rint("单引号注释多行")
8.'''
9.# 三个双引号
10."""
11.print("双引号注释多行")
12.print("双引号注释多行")
13.print("双引号注释多行")
14.print("双引号注释多行")
15."""
```

基本运算
C语言

```c
#include<stdio.h>
int main()
{
    int Result;
    int a = 10, b = 20;

    // 加法
    Result = a + b;
    printf("%d\n", Result);

    // 自加
    Result++;
    ++Result ;
    printf("%d\n", Result);

    // 减法
    Result = b - a;
    printf("%d\n", Result);

    // 自减
    Result--;
    --Result;
    printf("%d\n", Result);

    // 乘法
    Result = a * b;
    printf("%d\n", Result);
    Result *= a;
    printf("%d\n", Result);

    // 除法
    Result = b / a;
    printf("%d\n", Result);
    Result /= a;
    printf("%d\n", Result);

}
```

Python

```py
a = 10
b = 20

#  加法
result = a + b
print(result)

# 减法
result = a - b
print(result)

# 乘法
result = a * b
print(result)
result *= a

# 除法
result = b / a
print(result)
result /= a
print(result)


```

注意：Python没有自加，自减运算符，即 i++、 ++i、 i--、 --i，其他运算符基本与C语言相同。

判断语句
C语言

```c
#include<stdio.h>

int main()
{
    int a = 1, b = 2, c = 1;

    if(a == b)
    {
        printf("a == b");
    }
    else if(a == c)
    {
        printf("a == c");
    }
    else
    {
        printf("error");
    }
}
```

Python

```py
a = 1
b = 2
c = 1

if a == b:
    print("a == b")
elif a == c:
    print("a == c")
else:
    print("error")


```

elif相当于 elseif，其他用法与C语言相同。

循环语句
while循环
C语言

```c
#include<stdio.h>
int main()
{
    int a = 0, b = 10;
    while(a < b)
    {
        a++;
    }
    printf("%d", a);
}
```

Python

```py
a = 0
b = 10
while a < b:  a+=1
else:
print(a)
```

(未完待续)
