# 数据库相关

## MySQL

### 一、mysql服务的启动和停止
```mysql
mysql> net stop mysql

mysql> net start mysql
```

### 二、登陆mysql
```mysql

mysql> 语法如下：mysql -u用户名 -p用户密码

mysql> 键入命令mysql -uroot -p， 回车后提示你输入密码，输入12345，然后回车即可进入到mysql中了，mysql的提示符是：

mysql>
```


注意，如果是连接到另外的机器上，则需要加入一个参数-h机器IP

### 三、增加新用户

```mysql

mysql> 格式：grant 权限 on 数据库.* to 用户名@登录主机 identified by "密码"

mysql> 如，增加一个用户user1密码为password1，让其可以在本机上登录， 并对所有数? 据库有查询、插入、修改、删除的权限。首先用以root用户连入mysql，然后键入以下命令：

mysql> grant select,insert,update,delete on *.* to user1@localhost Identified by "password1";

```

如果希望该用户能够在任何机器上登陆mysql，则将localhost改为"%"。

如果你不想user1有密码，可以再打一个命令将密码去掉。

```mysql
grant select,insert,update,delete on mydb.* to user1@localhost identified by "";
```

### 四： 操作数据库及常见错误

mysql> 登录到mysql中，然后在mysql的提示符下运行下列命令，每个命令以分号结束。

#### 1、 显示数据库列表。
```mysql
show databases;
```

缺省有两个数据库：mysql和test。 mysql库存放着mysql的系统和用户权限信息，我们改密码和新增用户，实际上就是对这个库进行操作。

#### 2、 插入数据错误提示：
```mysql
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ':05:23)' at line
```

数据不合法
```mysql
Unknown column 'time' in 'field list'
```

看看是不是字段名输入错误

#### 3、 显示数据表的结构：
```mysql
mysql>? describe 表名;

mysql>? (或者)desc 表名;
```
#### 4、 建库与删库：
```mysql
mysql> create database 库名;

mysql> drop database 库名;
```
#### 5、 建表：
```mysql
mysql> use 库名;
```
? create table 表名(字段列表);
```mysql
drop table 表名;
```
#### 6、 清空表中记录：
```mysql
delete from 表名;
```
#### 7、 显示表中的记录：
```mysql
select * from 表名;
```

### 五、导出和导入数据

#### 1. 导出数据：

mysql> mysqldump --opt test > mysql.test

即将数据库test数据库导出到mysql.test文件，后者是一个文本文件
如：
```mysql
mysqldump -u root -p123456 --databases dbname > mysql.dbname
```

就是把数据库dbname导出到文件mysql.dbname中。

#### 2. 导入数据:
```mysql
mysql> mysqlimport -u root -p123456 < mysql.dbname。
```

#### 3. 将文本数据导入数据库:

文本数据的字段数据之间用tab键隔开。
```mysql
mysql> use test;

mysql> load data local infile "文件名" into table 表名;
```
#### 1:使用SHOW语句找出在服务器上当前存在什么数据库：
```mysql
mysql> mysql> SHOW DATABASES;
```
#### 2:2、创建一个数据库MYSQLDATA
```mysql
? mysql> CREATE DATABASE MYSQLDATA;
```
