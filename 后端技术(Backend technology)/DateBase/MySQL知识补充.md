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

* group by

* having ：

having和where的区别和联系：用法相同使用时机不同，where子句是把磁盘上的数据筛选到内存上，而having子句是把内存中的数据再次进行筛选

* order by& limit

* union（前提select后面的字段要匹配才能使用）

* join

`join in`（`inner join` ，`left join` `right join`）

* 子查询

* 视图

试图用途：查询、更新视图、在视图上定义新的试图，`不可以基于视图定义新的表的`

* 事务

commit(mysql默认自动提交)
rollback
原子性，一致性，隔离性，持久性，数据定义语言（DDL），事务不能被嵌套

* 权限

grant 权限列表 on 和revoke 权限列表 on

* 函数常用

日期函数：WEEkDay（当前是周几）,dayofmouth(一个月的第几天)

* 执行计划

explain ：
explain select Name,Cont From county where code ="cn"

select_type:描述正在使用的select的类型
table:显示在访问策略中使用的表的名称
type:描述优化程序使用的访问方法
possible——keyS:提供MYsql在评估访问策略时可选择的可用索引
key：实际用到的索引
rows：为了得到相应数据扫描的行数
filtered：由表条件过滤的行的百分比

* 储存引擎

|特性|MyISAM|innoDB|备注|
|--|--|--|--|--|
|事务支持|n|y|前者性能高|
|外键支持|n|y||
|聚集索引|非聚集索引|聚集索引|innoDB的b+数主键索引的叶子节点就是数据文件，辅助索引的叶子节点是主键的值|
|表的具体行数|存|不存||
|行级锁|不支持|支持||
|必须有主键|否|是||
|全文索引|支持|不支持（低版本）||
