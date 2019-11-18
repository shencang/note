# C/C++

## 未分类

### 1.下面程序段的输出结果是

```c
char *p1 = ”123”, *p2 = ”ABC”, str[50] = “xyz”;
strcpy(str + 2, strcat(p1, p2));
printf(“%s\n”, str);
```

* 出错

```t
原代码有错：p1和p2都指向常量字符串，在常量区，所以不能对其进行操作；改为数组即可，但是用字符串初始化数组时要记得将数组长度加1，因为字符串默认的末尾有一个‘\0’；第二点要注意的是，strcat函数的p1要有足够的空间来容纳p1和p2连接后的串长。

修改为以下代码将可以：
char p1[7] = "123";
char p2[] = "ABC";
char str[50] = "xyz";
strcpy(str + 2, strcat(p1, p2));
printf("%s\n", str);
结果：xy123ABC
```
