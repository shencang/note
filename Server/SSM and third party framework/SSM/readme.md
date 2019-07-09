# SSM

## ssm原理和入门：
 
 [手把手教你整合最优雅SSM框架：SpringMVC + Spring + MyBatis](https://blog.csdn.net/qq598535550/article/details/51703190)
 
 
[SSM框架——详细整合教程（Spring+SpringMVC+MyBatis）](https://www.cnblogs.com/zyw-205520/p/4771253.html)

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
 
 
 # Tomcat 
 
 ### tomcat日志打印乱码 
    打开cd到tomcat/conf/目录下
    修改logging.properties
    找到
    java.util.logging.ConsoleHandler.encoding = utf-8这行
    更改为
    java.util.logging.ConsoleHandler.encoding = GBK