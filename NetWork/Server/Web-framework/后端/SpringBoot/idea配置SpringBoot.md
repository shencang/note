# SpringBoot -idea的创建

## 一、SpringBoot简介

　　开发团队：Pivotal团队

　　主要目的：简化新Spring应用的初始搭建以及开发过程。

　　秉持理念：约定优于配置。（该框架使用了特定的方式来进行配置，从而使开发人员不再需要定义样板化的配置）

## 二、SpringBoot的特点

　　1、快速创建独立的Spring应用程序。

　　　　Spring Boot 并不是对 Spring 功能上的增强，而是提供了一种快速使用 Spring 的方式

　　2、嵌入的Tomcat，不需要部署war文件

　　3、简化了Maven的配置

　　4、自动装配Spring

　　5、开箱即用，没有代码生成、也不需要XML的配置

　　6、是微服务的入门级框架，SpringBoot是SpringCloud的基础　　

　　7、提供生产就绪功能：如指标、健康检查、外部配置等

## 三、测试环境

　　Maven 3.3.9 + JDK1.8 + IDEA (Ultimate - 2018.3)

## 四、创建首个SpringBoot项目

　　新建Sring Initalizr项目

![newSB](https://i.loli.net/2019/12/18/JDKdv3jTBsxn2gm.png)

选择下一步

![newSB2](https://i.loli.net/2019/12/18/vTIFpn2e9VG6OP8.png)

注意工程名需要小写，package配置的是包名，可以根据自己的偏好设置，然后下一步

![newSB3](https://i.loli.net/2019/12/18/pbEJgMzjHIN3Aui.png)

选择web项目

![newSB4](https://i.loli.net/2019/12/18/gpRI8qlZ4soac6f.png)

默认生成的项目目录：

![first1](https://i.loli.net/2019/12/18/372tsrVJURBmv9P.png)

我使用的SpringBoot版本：

![first2](https://i.loli.net/2019/12/18/kN1WlDxRZuPIUd5.png)

和SSM相似，配置都在pom.xml中。

![first3](https://i.loli.net/2019/12/18/32bUzZi8euOyKFw.png)

首次构建会消耗一定时间，当构建完成时就可以准备运行了。

但是首先需要新建一个Controller来提供入口：

```java
package com.shencangblue.start;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class StartController  {
    @RequestMapping(value = "hello",method = RequestMethod.GET)
    public String helloController(){
        return "hello world";
    }
}

```

我们点击IDEA的运行按钮，然后在控制台会看到SpringBoot内置的Tomcat访问的默认端口号8080

然后在网址中输入 `http://127.0.0.1:8080/hello`页面会展示

![run1](https://i.loli.net/2019/12/18/SGQz1bsYhCdZErI.png)

这里需要说明一下，SpringBoot的启动类 Application

```java
package com.shencangblue.start;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class StartApplication {

    public static void main(String[] args) {
    SpringApplication.run(StartApplication.class, args);
    }

}

```
