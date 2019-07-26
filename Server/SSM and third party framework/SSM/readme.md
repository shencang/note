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
 
 补充还没有搞完：
 
 # mybatis-generator
 
 [使用Maven插件mybatis-generator生成代码配置](https://www.jianshu.com/p/310c299846fc)
 
 [[06] 利用mybatis-generator自动生成代码](https://www.cnblogs.com/deng-cc/p/9340748.html)
 
 [idea-mybatis-generator](http://plugins.jetbrains.com/plugin/10196-idea-mybatis-generator)
 
 [随笔分类 - Java框架 MyBatis](https://www.cnblogs.com/deng-cc/category/1256755.html)
 
 ----
 [数据库表反向生成(一) MyBatis-generator与IDEA的集成](https://www.cnblogs.com/kangoroo/p/7495873.html)
 
 [Idea+Mybatis Generator+Mysql8.0.13自动生成sql文件（搭建微服务系列）](https://blog.csdn.net/duck0730/article/details/83790228)
 
 ----
 
 # Tomcat 
 
 ### tomcat日志打印乱码 
    打开cd到tomcat/conf/目录下
    修改logging.properties
    找到
    java.util.logging.ConsoleHandler.encoding = utf-8这行
    更改为
    java.util.logging.ConsoleHandler.encoding = GBK
    =====》上下五个均修改才可以
    
 ### BUG解决
 
 * 1-错误：
    
    
    No converter found for return value of type: class java.util.ArrayList
     
 解决：
 
    原因：这是因为springmvc默认是没有对象转换成json的转换器的，需要手动添加jackson依赖。
    
    
 解决步骤：
　　　　

   手动添加jackson依赖到pom.xml文件中
    
```xml
  <properties>
    <jackson.version>2.5.4</jackson.version>
  </properties> 

  <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-core</artifactId>
      <version>${jackson.version}</version>
    </dependency>
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId>
      <artifactId>jackson-databind</artifactId>
      <version>${jackson.version}</version>
    </dependency>
    
```
如果还是没有解决，则进行以下步骤


在springmvc配置文件中进行如下配置
```xml
<mvc:annotation-driven>
     <mvc:message-converters>
            <bean class="org.springframework.http.converter.StringHttpMessageConverter"/>
            <bean class="org.springframework.http.converter.json.MappingJackson2HttpMessageConverter"/>
   </mvc:message-converters>
</mvc:annotation-driven>
```
即可


----
 
 
* 2-错误：
    
    
     [ERROR] Failed to execute goal org.mybatis.generator:mybatis-generator-maven-plugin:1.3.5:generate (default-cli) on project nailQuartzProject: Execution default-cli of goal org.mybatis.generator:mybatis-generator-maven-plugin:1.3.5:generate failed: Cannot resolve classpath entry: D:\study\nailQuartzProject\src\main\resource -> [Help 1]

     
 解决：
 
    确认在main目录下有resources文件夹，并有正确的配置信息xml文件，没有则新建。
    
 ----

* 3-错误：
    
    
     Public Key Retrieval is not allowed -> [Help 1]
     
 解决：
 
    1.mysql5及之前的版本使用的是旧版驱动"com.mysql.jdbc.Driver"，mysql6以及之后的版本需要更新到新版驱动，对应的Driver是"com.mysql.cj.jdbc.Driver"，但是这个驱动错误的信息是"Loading class `com.mysql.jdbc.Driver'. This is deprecated. The new driver class is `com.mysql.cj.jdbc.Driver'. The driver is automatically registered via the SPI and manual loading of the driver class is generally unnecessary."，排除这个原因。

    2.连接数据库的url中，加上allowPublicKeyRetrieval=true参数，经过验证解决该问题。

    3.网上看到另外的解决 办法，修改default_authentication_plugin设置，在my.ini中增加[mysqld]default_authentication_plugin=mysql_native_password，然后mysql命令行执行ALTER USER 'username'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';最后在url中添加时区参数serverTimezone=Asia/Shanghai。
    
    
  ----
    
 * 4-错误：
    
    
     org.springframework.web.util.NestedServletException: Handler dispatch failed; nested exception is java.lang.AbstractMethodError: Method com/mchange/v2/c3p0/impl/NewProxyResultSet.isClosed()Z is abstract

     
 解决：
 
   在pom.xml文件中修改C3P0的依赖包：
   
   之前是
   ```xml
   <dependency>
	<groupId>c3p0</groupId>
	<artifactId>c3p0</artifactId>
	<version>0.9.1.2</version>
</dependency> 
```
   修改成
   ```xml
<dependency>
	<groupId>com.mchange</groupId>
	<artifactId>c3p0</artifactId>
	<version>0.9.5.2</version>
</dependency>
```

* 5-错误：
    
    
     java.lang.ClassNotFoundException: javax.xml.bind.JAXBException
     
 解决：
 解决方案一：

    降低JDK版本到 JDK 6/7/8

解决方案二:（亲测可行）

    手动加入这些依赖Jar包

    要解决这个问题，导入了下面这四个Jar包修复成功。

[javax.activation-1.2.0.jar](http://search.maven.org/remotecontent?filepath=com/sun/activation/javax.activation/1.2.0/javax.activation-1.2.0.jar)

[jaxb-api-2.3.0.jar](http://search.maven.org/remotecontent?filepath=javax/xml/bind/jaxb-api/2.3.0/jaxb-api-2.3.0.jar)

[jaxb-core-2.3.0.jar](http://search.maven.org/remotecontent?filepath=com/sun/xml/bind/jaxb-core/2.3.0/jaxb-core-2.3.0.jar)

[jaxb-impl-2.3.0.jar](http://search.maven.org/remotecontent?filepath=com/sun/xml/bind/jaxb-impl/2.3.0/jaxb-impl-2.3.0.jar)

    下载上面这些文件和复制他们到libs文件夹下，
    添加他们导入到Build Path中
    重新运行即可

解决方案三：

    Maven项目可添加如下依赖：

```xml
<!-- Java 6 = JAX-B Version 2.0   -->
<!-- Java 7 = JAX-B Version 2.2.3 -->
<!-- Java 8 = JAX-B Version 2.2.8 -->
<dependencies>
    <dependency>
        <groupId>javax.xml.bind</groupId>
        <artifactId>jaxb-api</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-impl</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>com.sun.xml.bind</groupId>
        <artifactId>jaxb-core</artifactId>
        <version>2.3.0</version>
    </dependency>
    <dependency>
        <groupId>javax.activation</groupId>
        <artifactId>activation</artifactId>
        <version>1.1.1</version>
    </dependency>
</dependencies>
```
    Tips:
    建议使用中心仓库，否则可能某些jar找不到：

    HTTP: http://repo1.maven.org/maven2
    HTTPS:https://repo1.maven.org/maven2
    
[参考](https://blog.csdn.net/hadues/article/details/79188793)