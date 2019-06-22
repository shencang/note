# CentOS

### mysql的安装与配置：
配置：
登录MYSQL
```
 mysql -u root -p
 密码
```
创建用户
```mysql
GRANT USAGE ON *.* TO 'user01'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
```
刷新系统权限表
```mysql
flush privileges;
```
这样就创建了一个名为：user01 密码 123456 的用户。
退出后登录一下
```
@>exit;
@>mysql -u user01 -p
@>输入密码 123456
mysql>登录成功
```
登录MYSQL（有ROOT权限）。我里我以ROOT身份登录。
```
@>mysql -u root -p
@>密码
```
首先为用户创建一个数据库（fe）
```mysql
create database fe;
```
授权fe_group用户拥有fe数据库的所有权限
```mysql
grant all privileges on fe.* to fe_group@localhost identified by '123456';
```
localhost是本地访问，其他地址访问不了，%是所有
```mysql
grant all privileges on fe.* to fe_group@'%' identified by '123456';
```
刷新系统权限表
```mysql
flush privileges;
```




### python的安装与配置：

```
yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
```
安装可能用到的依赖

```
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
```

下载Python3.6.5源码

```
tar -xzvf Python-3.6.5.tgz
```

解压到当前目录

```
cd Python-3.6.5
```

进入解压后的目录


 ```
 gcc -v
 ```
 查看 gcc 版本

```
yum install gcc-c++
```
若无安装，则运行

```
./configure --prefix=/usr/local/python
```

安装到/usr/local/python目录，不用事先创建python目录

```
make
```

编译

```
make install
```

安装

```
cd /usr/bin
```

进入/usr/bin目录

```
mv python python.bak
mv pip pip.bak
```

重命名python2的快捷方式

```
ln -s /usr/local/python/bin/python3.6 /usr/bin/python
ln -s /usr/local/python/bin/pip3.6 /usr/bin/pip
```

创建python3与pip3软连接

```
ll yum*
```
查看/usr/bin目录下有哪些yum文件
把这些文件的第一行
```
#!/usr/bin/python
```
改为
```
#!/usr/bin/python2
```
因为yum是依赖python的，所以我们修改了默认的python,就要修改yum，让其运行指向python2

修改urlgrabber配置文件

```
vim /usr/libexec/urlgrabber-ext-down
```

把第一行
```
#!/usr/bin/python
```
改为 
```
#!/usr/bin/python2
``` 
![image](https://images2018.cnblogs.com/blog/1321829/201807/1321829-20180710155353100-1996539343.png)

