# CentOS

## mysql的安装与配置

配置：
登录MYSQL

```t
 mysql -u root -p
 密码
```

创建用户

```mysql
GRANT USAGE ON *.* TO 'jiyue'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;
```

刷新系统权限表

```mysql
flush privileges;
```

这样就创建了一个名为：user01 密码 123456 的用户。
退出后登录一下

```t
@>exit;
@>mysql -u user01 -p
@>输入密码 123456
mysql>登录成功
```

登录MYSQL（有ROOT权限）。我里我以ROOT身份登录。

```t
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

## python的安装与配置

```t
yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
```

安装可能用到的依赖

```t
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
```

下载Python3.6.5源码

```t
tar -xzvf Python-3.6.5.tgz
```

解压到当前目录

```t
cd Python-3.6.5
```

进入解压后的目录

 ```t
 gcc -v
 ```

 查看 gcc 版本

```t
yum install gcc-c++
```

若无安装，则运行

```t
./configure --prefix=/usr/local/python
```

安装到/usr/local/python目录，不用事先创建python目录

```t
make
```

编译

```t
make install
```

安装

```t
yum -y install epel-release
```

首先安装epel扩展源

```t
yum install python-pip
```

安装pip

```t
cd /usr/bin
```

进入/usr/bin目录

```t
mv python python.bak
mv pip pip.bak
```

重命名python2的快捷方式

```t
ln -s /usr/local/python/bin/python3.6 /usr/bin/python
ln -s /usr/local/python/bin/pip3.6 /usr/bin/pip
```

创建python3与pip3软连接

```t
ll yum*
```

查看/usr/bin目录下有哪些yum文件
把这些文件的第一行

```t
#!/usr/bin/python
```

改为

```t
#!/usr/bin/python2
```

因为yum是依赖python的，所以我们修改了默认的python,就要修改yum，让其运行指向python2

修改urlgrabber配置文件

```t
vim /usr/libexec/urlgrabber-ext-down
```

把第一行

```t
#!/usr/bin/python
```

改为

```t
#!/usr/bin/python2
```

![image](https://images2018.cnblogs.com/blog/1321829/201807/1321829-20180710155353100-1996539343.png)

### VIM

#### 一、vim进入编辑模式

编辑模式：一般模式下不可以修改某个字符，若要修改字符，只能进入编辑模式。从一般模式进编辑模式，只需按i、I、a、A、o、O、r和R中某个键即可。当进入编辑模式时，在屏幕尾部会显示INSERT或REPLACE字样（若你的centos支持中文，则会显示“插入”）。从编辑模式回到一般模式，按esc即可。

i：在当前字符前插入。

I：在光标所在行的行首插入。

a：在当前字符后插入。

A：在光标所在行的行尾插入。

o：在当前行的下一行插入新的一行。

O：在当前行的上一行插入新的 一行。

#### 二、vim命令模式

命令模式：输入：或者/即可进入命令模式。该模式下，可以搜索字符或字符串，可以保存、替换、退出、显示行号等操作。

```t
/word
```

:在光标之后查找一个字符串word，按n向后继续搜索，shift+n向上搜索。

```t
?word
```

:在光标之前查找一个字符串word，按n向后继续搜索。

搜索出来的字符串都会高亮显示，若想不高亮，输入:

```t
nohl
```

```t
:n1,n2s/word1/word2/g
```

：在n1和n2行之间查找word1并替换为word2，不加g则只替换每行的第一个word1。（先起点然后逗号分隔，再终点s表示替换/需替换的/替换后的/g表示全部。$表示到最末端）

```t
:1,$s/word1/word2/g
```

：将文档中所有的word1替换为word2，不加g则只替换每行的第一个word1。

## **特殊情况**

```t
:1,$s//etc/hosts/aminglinux.com/g
```

；将

```t
/etc/hosts
```

替换为，

```t
aminglinux.com
```

由于有多个斜杠，所以无法识别，因此要推一下，系统就会将/etc/hosts的斜杠视为普通的字符，

```t
:1,$s/\/etc\/hosts/aminglinux.com/g
```

，加两个右斜杠。

也可将原来的斜杠改为#或@，

```t
:1,$s#/etc/hosts#aminglinux.com#g，
```

如此以#或@作为它的语法组成字符。

## **其他功能**

```t
:w
```

 保存文本。

```t
:q
```

  退出vim。

```t
:w!
```

  强制保存，在root用户下，即使文本只读也可以完成保存。
  
```t
:q!
```

 强制退出，所有改动不生效。

```t
:wq
```

 保存退出。

```t
:x
```

 类似于wq，更改了文件以后，wq和x的作用是一样的，若没有更改文件，使用wq，文件的mtime会改变，而x不会。

```t
:set nu
```

 显示行号。

```t
:set nonu
```

  不显示行号。

## 三、vim实践

若没有/etc/dnsmasq.conf这个文件，需安装软件包

```t
yum install dnsmasq -y
```

重启dnsmasq服务：

```t
# service dnsmasq start
```

## 扩展

[vim的特殊用法](http://www.apelearn.com/bbs/thread-9334-1-1.html)

[vim常用快捷键总结](http://www.apelearn.com/bbs/thread-407-1-1.html)

[vim快速删除一段字符](http://www.apelearn.com/bbs/thread-842-1-1.html)

[vim乱码](http://www.apelearn.com/bbs/thread-6753-1-1.html)

[小键盘问题](http://www.apelearn.com/bbs/thread-7215-1-1.html)

[vim加密](http://www.apelearn.com/bbs/thread-7750-1-1.html)  

## 腾讯服务器相关

### 可视化

[腾讯云Centos7搭建图形界面详解](https://blog.csdn.net/nsu406096612/article/details/78062230)

[腾讯云CentOS7实现可视化！！！](https://blog.csdn.net/xiaokanshijie/article/details/84397052)

[腾讯云centos7.2X64安装图形界面](https://blog.csdn.net/weixin_34001430/article/details/88251994)

## 部署uwsgi和nginx

[django+uwsgi+nginx部署](https://www.cnblogs.com/wdliu/p/8932816.html)

[MySQL之权限管理](https://www.cnblogs.com/Richardzhu/p/3318595.html)

[MySQL缺失mysql_config文件](https://www.cnblogs.com/php-linux/p/6121370.html)

[Centos7+nginx1.12+uwsgi2.0+django2.0+python3.6个人配置记录(概要)](https://blog.csdn.net/qq_25532699/article/details/80988869)
