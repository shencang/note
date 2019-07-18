# SSM

## ssm原理和入门：
 
[手把手教你整合最优雅SSM框架：SpringMVC + Spring + MyBatis](https://blog.csdn.net/qq598535550/article/details/51703190)
 
[SSM框架——详细整合教程（Spring+SpringMVC+MyBatis）](https://www.cnblogs.com/zyw-205520/p/4771253.html)

[java优雅的SSM框架（一）：Spring框架（由浅入深，深度解读）](https://baijiahao.baidu.com/s?id=1623472794079496219&wfr=spider&for=pc)

[Spring MVC框架](https://www.cnblogs.com/jxtx92/p/8022154.html)

## idea的搭建和环境：

亲测可用：

[ssm整合 idea+maven版](https://www.cnblogs.com/lflying/p/10997473.html)
 
 不过要记得缩进问题
 
还没经过测试，等待之后分类：

 [详解intellij idea搭建SSM框架(spring+maven+mybatis+mysql+junit)(上)](https://www.cnblogs.com/toutou/p/ssm_spring.html)
 
 [手把手教你使用idea建SSM工程(一)——创建maven+web项目](https://blog.csdn.net/daxia_2016/article/details/81265282)
 
 [IntelliJ IDEA 搭建SSM框架并实现用户登录功能](https://www.javazhiyin.com/40095.html)
 
 [idea使用mybatis generator自动生成代码mapper+pojo+xml](https://blog.csdn.net/i168wintop/article/details/94972991)
 
 [DEA实现SSM分布式编程实现用户登录、增删改查](https://blog.csdn.net/Franks_Wan/article/details/94432149)
 
 [SSM框架整合（IntelliJ IDEA + maven + Spring + SpringMVC + MyBatis）](https://blog.csdn.net/GallenZhang/article/details/51932152)
 
 [IDEA 整合 SSM 框架学习](https://www.cnblogs.com/wmyskxz/p/8916365.html)
 
 一个系列：
 
 [【SSM框架从零开始1】IntelliJ IDEA搭建最简单的Spring MVC项目](https://www.jianshu.com/p/23e58ca14f1c)
 
 [【SSM框架从零开始2】IntelliJ IDEA下Spring MVC数据库配置与增删改查开发](https://www.jianshu.com/p/61d16f8ad23a)
 
 [【SSM框架从零开始3】使用Mybatis-Generator自动生成Dao、Model层相关代码](https://www.jianshu.com/p/ad8fb997e4c8)
 
 [【SSM框架从零开始4】IntelliJ IDEA搭建SSM框架](https://www.jianshu.com/p/c01f0f499715?utm_campaign=haruki&utm_content=note&utm_medium=reader_share&utm_source=weixin)
 
 # Tomcat 
 
 ### tomcat日志打印乱码 
    打开cd到tomcat/conf/目录下
    修改logging.properties
    找到
    java.util.logging.ConsoleHandler.encoding = utf-8这行
    更改为
    java.util.logging.ConsoleHandler.encoding = GBK