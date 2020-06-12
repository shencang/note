# 数据库相关

## MySQL

### 链接

* [MySQL子查询 嵌套查询](https://blog.csdn.net/m0_38061639/article/details/82872705)

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

mysql> grant select,insert,update,delete on *.* to iwps@localhost Identified by "passwordiwps";

```

如果希望该用户能够在任何机器上登陆mysql，则将localhost改为"%"。

如果你不想user1有密码，可以再打一个命令将密码去掉。

```mysql
grant select,insert,update,delete on mydb.* to user1@localhost identified by "";
```

### 四： 操作数据库及常见错误

mysql> 登录到mysql中，然后在mysql的提示符下运行下列命令，每个命令以分号结束。

#### 1、 显示数据库列表

```mysql
show databases;
```

缺省有两个数据库：mysql和test。 mysql库存放着mysql的系统和用户权限信息，我们改密码和新增用户，实际上就是对这个库进行操作。

#### 2、 插入数据错误提示

```mysql
You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ':05:23)' at line
```

数据不合法

```mysql
Unknown column 'time' in 'field list'
```

看看是不是字段名输入错误

#### 3、 显示数据表的结构

```mysql
mysql>? describe 表名;

mysql>? (或者)desc 表名;
```

#### 4、 建库与删库

```mysql
mysql> create database 库名;

mysql> drop database 库名;
```

#### 5、 建表

```mysql
mysql> use 库名;
```

? create table 表名(字段列表);

```mysql
drop table 表名;
```

#### 6、 清空表中记录

```mysql
delete from 表名;
```

#### 7、 显示表中的记录

```mysql

select * from 表名;
```

### 五、导出和导入数据

#### 1. 导出数据

mysql> mysqldump --opt test > mysql.test

即将数据库test数据库导出到mysql.test文件，后者是一个文本文件
如

```mysql

mysqldump -u root -p123456 --databases dbname > mysql.dbname
```

就是把数据库dbname导出到文件mysql.dbname中。

#### 2. 导入数据

```mysql
mysql> mysqlimport -u root -p123456 < mysql.dbname。
```

#### 3. 将文本数据导入数据库

文本数据的字段数据之间用tab键隔开。

```mysql
mysql> use test;

mysql> load data local infile "文件名" into table 表名;
```

#### 1:使用SHOW语句找出在服务器上当前存在什么数据库

```mysql
mysql> mysql> SHOW DATABASES;
```

#### 2:2、创建一个数据库MYSQLDATA

```mysql
? mysql> CREATE DATABASE MYSQLDATA;
```

### MySql 外键约束 之CASCADE、SET NULL、RESTRICT、NO ACTION分析和作用

MySQL有两种常用的引擎类型：MyISAM和InnoDB。目前只有InnoDB引擎类型支持外键约束。InnoDB中外键约束定义的语法如下

```mysql
ALTER TABLE tbl_name
    ADD [CONSTRAINT [symbol]] FOREIGN KEY
    [index_name] (index_col_name, ...)
    REFERENCES tbl_name (index_col_name,...)
    [ON DELETE reference_option]
    [ON UPDATE reference_option]
```

例如：

```mysql
ALTER TABLE `user_resource` CONSTRAINT `FKEEAF1E02D82D57F9` FOREIGN KEY (`user_Id`) REFERENCES `sys_user` (`Id`)

```

InnoDB也支持使用ALTER TABLE来删除外键：

```mysql
ALTER TABLE `user_resource` DROP FOREIGN KEY `FKEEAF1E02D82D57F9`;

```

* CASCADE

在父表上update/delete记录时，同步update/delete掉子表的匹配记录

* SET NULL

在父表上update/delete记录时，将子表上匹配记录的列设为null (要注意子表的外键列不能为not null)  

* NO ACTION

如果子表中有匹配的记录,则不允许对父表对应候选键进行update/delete操作  

* RESTRICT

同no action, 都是立即检查外键约束

* SET NULL

父表有变更时,子表将外键列设置成一个默认的值 但Innodb不能识别

* NULL、RESTRICT、NO ACTION
删除：从表记录不存在时，主表才可以删除。删除从表，主表不变

更新：从表记录不存在时，主表才可以更新。更新从表，主表不变

* CASCADE
删除：删除主表时自动删除从表。删除从表，主表不变
更新：更新主表时自动更新从表。更新从表，主表不变

* SET NULL

删除：删除主表时自动更新从表值为NULL。删除从表，主表不变

更新：更新主表时自动更新从表值为NULL。更新从表，主表不变

外键约束属性： RESTRICT | CASCADE | SET NULL | NO ACTION

 外键的使用需要满足下列的条件：

  1. 两张表必须都是InnoDB表，并且它们没有临时表。
  2. 建立外键关系的对应列必须具有相似的InnoDB内部数据类型。
  3. 建立外键关系的对应列必须建立了索引。
  4. 假如显式的给出了CONSTRAINT symbol，那symbol在数据库中必须是唯一的。假如没有显式的给出，InnoDB会自动的创建。
  
  如果子表试图创建一个在父表中不存在的外键值，InnoDB会拒绝任何INSERT或UPDATE操作。如果父表试图UPDATE或者DELETE任何子 表中存在或匹配的外键值，最终动作取决于外键约束定义中的ON UPDATE和ON DELETE选项。InnoDB支持5种不同的动作，如果没有指定ON DELETE或者ON UPDATE，默认的动作为RESTRICT:
  
  1. CASCADE: 从父表中删除或更新对应的行，同时自动的删除或更新自表中匹配的行。ON DELETE CANSCADE和ON UPDATE CANSCADE都被InnoDB所支持。
  2. SET NULL: 从父表中删除或更新对应的行，同时将子表中的外键列设为空。注意，这些在外键列没有被设为NOT NULL时才有效。ON DELETE SET NULL和ON UPDATE SET SET NULL都被InnoDB所支持。
  3. NO ACTION: InnoDB拒绝删除或者更新父表。
  4. RESTRICT: 拒绝删除或者更新父表。指定RESTRICT（或者NO ACTION）和忽略ON DELETE或者ON UPDATE选项的效果是一样的。
  5. SET DEFAULT: InnoDB目前不支持。
  
  外键约束使用最多的两种情况无外乎：
  
  1）父表更新时子表也更新，父表删除时如果子表有匹配的项，删除失败；
  2）父表更新时子表也更新，父表删除时子表匹配的项也删除。
  前一种情况，在外键定义中，我们使用ON UPDATE CASCADE ON DELETE RESTRICT；后一种情况，可以使用ON UPDATE CASCADE ON DELETE CASCADE。
  
当执行外键检查之时，InnoDB对它照看着的子或父记录设置共享的行级锁。InnoDB立即检查外键约束，检查不对事务提交延迟。
要使得对有外键关系的表重新载入转储文件变得更容易，mysqldump自动在转储输出中包括一个语句设置FOREIGN_KEY_CHECKS为0。这避免在转储被重新装载之时，与不得不被以特别顺序重新装载的表相关的问题。也可以手动设置这个变量：

```mysql
mysql> SET FOREIGN_KEY_CHECKS = 0;
mysql> SOURCE dump_file_name;
mysql> SET FOREIGN_KEY_CHECKS = 1;
```

　　如果转储文件包含对外键是不正确顺序的表，这就以任何顺序导入该表。这样也加快导入操作。设置FOREIGN_KEY_CHECKS为0，对于在LOAD DATA和ALTER TABLE操作中忽略外键限制也是非常有用的。
InnoDB不允许你删除一个被FOREIGN KEY表约束引用的表，除非你做设置SET FOREIGN_KEY_CHECKS=0。当你移除一个表的时候，在它的创建语句里定义的约束也被移除。
　　如果你重新创建一个被移除的表，它必须有一个遵从于也引用它的外键约束的定义。它必须有正确的列名和类型，并且如前所述，它必须对被引用的键有索引。如果这些不被满足，MySQL返回错误号1005 并在错误信息字符串中指向errno 150。

### MySQL 记录不存在时插入 记录存在则更新的实现方法

```mysql
INSERT INTO table (a,b,c) VALUES (1,2,3)
  ON DUPLICATE KEY UPDATE c=c+1;
```

INSERT 中 ON DUPLICATE KEY UPDATE的使用

如果指定了ON DUPLICATE KEY UPDATE，并且插入行后会导致在一个UNIQUE索引或PRIMARY KEY中出现重复值，则执行旧行UPDATE。例如，如果列a被定义为UNIQUE，并且包含值1，则以下两个语句具有相同的效果：

```mysql
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3) ON DUPLICATE KEY UPDATE c=c+1;
mysql> UPDATE table SET c=c+1 WHERE a=1;
```

如果行作为新记录被插入，则受影响行的值为1；如果原有的记录被更新，则受影响行的值为2。

注释：如果列b也是唯一列，则INSERT与此UPDATE语句相当：

```mysql
mysql> UPDATE table SET c=c+1 WHERE a=1 OR b=2 LIMIT 1;
```

如果a=1 OR b=2与多个行向匹配，则只有一个行被更新。通常，您应该尽量避免对带有多个唯一关键字的表使用ON DUPLICATE KEY子句。

可以在UPDATE子句中使用VALUES(col_name)函数从INSERT...UPDATE语句的INSERT部分引用列值。换句话说，如果没有发生重复关键字冲突，则UPDATE子句中的VALUES(col_name)可以引用被插入的col_name的值。本函数特别适用于多行插入。

VALUES()函数只在INSERT...UPDATE语句中有意义，其它时候会返回NULL。
示例：

```mysql
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3),(4,5,6) ON DUPLICATE KEY UPDATE c=VALUES(a)+VALUES(b);
```

本语句与以下两个语句作用相同：

```mysql
mysql> INSERT INTO table (a,b,c) VALUES (1,2,3)
         -> ON DUPLICATE KEY UPDATE c=3;
mysql> INSERT INTO table (a,b,c) VALUES (4,5,6)
         -> ON DUPLICATE KEY UPDATE c=9;
```

```mysql
INSERT ... SELECT
INSERT ... ON DUPLICATE KEY UPDATE
INSERT ... ON DUPLICATE REPLACE
```
