# MySQL知识学习

参考：[万字精华总结](https://www.jianshu.com/p/c189439fb32e)

![title]( https://upload-images.jianshu.io/upload_images/20012016-117cc7d60756169d?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)

[数据库表设计的问题](https://bbs.csdn.net/topics/110162451)

## Mysql

* 基础语法

连接数据库方式：socket/tcp&ip（后者远程和本地均可）

* 关键字：
``create database`` 创建数据库

``show/drop(也是有选项的）/``

``mysqldump`` 备份数据库

``create table``

``insert into（） values （）``

``not null``\ ``default``\  ``unique key``\ ``primary key``\ ``auto_increment``\ ``comment（说明）``

* 索引

优点和缺点：加快检索保证唯一性，缺点是消耗时间和资源，表操作会降低索引效率下降

*（0或多） +（1或多） ？（0或1）

where筛选到内存上，having拿到内存再做筛选

asc升序 desc降序

join in（inner join ，left join right join）

子查询