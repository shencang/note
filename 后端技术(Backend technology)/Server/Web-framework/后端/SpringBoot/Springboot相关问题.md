# Springboot相关问题

## 静态资源相关

### 静态资源目录

```t

其中默认配置的 /** 映射到 /static （或/public、/resources、/META-INF/resources）

其中默认配置的 /webjars/** 映射到 classpath:/META-INF/resources/webjars/

PS：上面的 static、public、resources 等目录都在 classpath: 下面（如 src/main/resources/static）。

优先级顺序为：META/resources > resources > static > public

```

## JPA相关

### JPA相关问题

#### SpringBoot2.0 (Spring-Data-Jpa) findById(findOne())和Optional的使用

#### 1、findOne()方法的替代方法findById()

2.0版本，Spring-Data-Jpa修改findOne()。

* 1）2.0版本之前

```java
T findOne(ID primaryKey);
```

* 2）2.0版本

```java
  Optional<T> findById(ID id);
```

#### 2、Optional Optional的使用

文档：Optional

container对象，可能包含也可能不包含非null值。如果存在值，则isPresent()将返回true，get()将返回该值。提供依赖于是否存在包含值的其他方法，例如orElse()（如果值不存在则返回默认值）和ifPresent()（如果值存在则执行代码块）。

```java
Optional<T> findById(ID id)
```

中Optional的一些用法：

* 1）如果没找到指定实体，则返回一个默认值。

```java

Foo foo = repository.findById(id).orElse(new Foo());

```

或者

```java
Foo foo = repository.findById(id).orElse(null);

```

* 2）如果找到实体返回它，否则抛出异常

```java
return repository.findById(id)
        .orElseThrow(() -> new EntityNotFoundException(id));
```

* 3）假设希望根据是否找到实体来应用不同的处理（无需抛出异常）

```java
Optional<Foo> fooOptional = fooRepository.findById(id);
if (fooOptional.isPresent()){
    Foo foo = fooOptional.get();
   // 处理 foo ...
}
else{
   //另一种情况....
}
```

#### Spring-Data-Jpa的Sort排序时遇到的问题 has private access in 'org.springframework.data.domain.Sort'

springboot2.2.1（含）以上的版本Sort已经不能再实例化了，构造方法已经私有

![image.png](https://i.loli.net/2020/03/06/o36CiPeL517fWlQ.png)

![image.png](https://i.loli.net/2020/03/06/sm1e2lghd35IOn8.png)

改用Sort.by获得Sort对象

![image.png](https://i.loli.net/2020/03/06/vPjKirqOkAd1zCp.png)

```java
@GetMapping("/test2")
    public String find3() {
        List<Book> book = bookDao.findAll(Sort.by(Sort.Direction.DESC, "bookId"));
        for (Book book1 : book) {
            System.out.println(book1);
        }
        return "success";
    }

```

```t
Sort.by()可以一个或多个字段排序
```

## bean 相关

### idea-使用@Autowired注解警告Field injection is not recommended

[参考文章](https://blog.csdn.net/zhangjingao/article/details/81094529)

```t
在使用spring框架中的依赖注入注解@Autowired时，idea报了一个警告
```

``被警告的代码如下：``

```java
    @Autowired
    UserDao userDao;
```

```警告内容是```

```t

Field injection is not recommended

```

``意思就是使用变量依赖注入的方式是不被推荐的。
使用idea解决策略是这样的：``

```t
Always use constructor based dependency injection in your beans. Always use assertions for mandatory dependencies
```

```t
意思就是总是使用构造器的方式强制注入。
```

``依赖注入有三种方式：``

* 变量（filed）注入
* 构造器注入
* set方法注入

```先各自看一下实现方式```

* 变量（filed）注入

```java
    @Autowired
    UserDao userDao;
```

* 构造器注入

```java
    final
    UserDao userDao;

    @Autowired
    public UserServiceImpl(UserDao userDao) {
        this.userDao = userDao;
    }
```

* set方法注入

```java
    private UserDao userDao;

    @Autowired
    public void setUserDao (UserDao userDao) {
        this.userDao = userDao;
    }
```

``相比较而言：``

```t
优点：变量方式注入非常简洁，没有任何多余代码，非常有效的提高了java的简洁性。即使再多几个依赖一样能解决掉这个问题。

缺点：不能有效的指明依赖。相信很多人都遇见过一个bug，依赖注入的对象为null，在启动依赖容器时遇到这个问题都是配置的依赖注入少了一个注解什么的，然而这种方式就过于依赖注入容器了，当没有启动整个依赖容器时，这个类就不能运转，在反射时无法提供这个类需要的依赖。
在使用set方式时，这是一种选择注入，可有可无，即使没有注入这个依赖，那么也不会影响整个类的运行。
在使用构造器方式时已经显式注明必须强制注入。通过强制指明依赖注入来保证这个类的运行。

另一个方面：
依赖注入的核心思想之一就是被容器管理的类不应该依赖被容器管理的依赖，换成白话来说就是如果这个类使用了依赖注入的类，那么这个类摆脱了这几个依赖必须也能正常运行。然而使用变量注入的方式是不能保证这点的。
既然使用了依赖注入方式，那么就表明这个类不再对这些依赖负责，这些都由容器管理，那么如何清楚的知道这个类需要哪些依赖呢？它就要使用set方法方式注入或者构造器注入。

总结下：
变量方式注入应该尽量避免，使用set方式注入或者构造器注入，这两种方式的选择就要看这个类是强制依赖的话就用构造器方式，选择依赖的话就用set方法注入。
```

### Spring Bean的循环依赖

[参考文章](https://www.jianshu.com/p/d935341694d2)

```t
如果使用构造函数注入，则可能会创建一个无法解析的循环依赖场景。
```

#### 什么是循环依赖

下面是[引文作者](https://www.jianshu.com/p/d935341694d2)所遇到的情况，

``代码结构如下：``

* SpringSecurity 配置类：

```java
@Configuration
public class BrowserSecurityConfig extends WebSecurityConfigurerAdapter {
    private final UserDetailsService userDetailsService;

    /**
     * 通过配置类构造函数注入 UserDetailsService
     */
    @Autowired
    public BrowserSecurityConfig(UserDetailsService userDetailsService) {
        this.userDetailsService = userDetailsService;
    }

    /**
     * 在配置类中声明 加密编码器
     */
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    ... ...
}

```

* UserDetailsService 类：

```java
@Component
public class MyUserDetailService implements UserDetailsService {
    private final PasswordEncoder passwordEncoder;

    private Logger logger = LoggerFactory.getLogger(getClass());

   /**
     * 通过构造函数注入 PasswordEncoder
     */
    @Autowired
    public MyUserDetailService(PasswordEncoder passwordEncoder) {
        this.passwordEncoder = passwordEncoder;
    }
    ... ...
}
```

* 运行之后，Spring抛出了如下错误信息：

```t
Description:

The dependencies of some of the beans in the application context form a cycle:

┌─────┐
|  browserSecurityConfig defined in file [D:\CODE\Java\IdeaProjects\mango-security\mango-security-browser\target\classes\stu\mango\security\browser\BrowserSecurityConfig.class]
↑     ↓
|  myUserDetailService defined in file [D:\CODE\Java\IdeaProjects\mango-security\mango-security-browser\target\classes\stu\mango\security\browser\MyUserDetailService.class]
└─────┘
```

该例中，``BrowserSecurityConfig`` 通过构造函数注入 ``UserDetailsService``实例，而 ``UserDetailsService``由通过构造函数注入在``BrowserSecurityConfig`` 中声明的``PasswordEncoder``。

总结来说，Spring Bean的循环依赖是指，类A需要通过构造函数注入的类B的实例（或者B中声明的Bean），而类B需要通过构造函数注入的类A的实例（或者A中声明的Bean）。如果将类A和类B的bean配置为相互注入，则Spring IoC容器会在运行时检测到此循环引用，并引发一个``BeanCurrentlyInCreationException``。与典型情况（没有循环依赖）不同，bean A和bean B之间的循环依赖关系迫使其中一个bean在被完全初始化之前被注入到另一个bean中（这是一个典型的“先有鸡还是先有蛋”场景）。

![image.png](https://i.loli.net/2020/04/24/MmLWbEpuYo9sF3x.png)

#### 解决方案

简明扼要的说，就是——[不使用基于构造函数的依赖注入](http://docs.spring.io/spring/docs/4.3.10.RELEASE/spring-framework-reference/htmlsingle/#beans-constructor-injection)。可通过下面方式解决。

在字段上使用@Autowired注解，让Spring决定在合适的时机注入。【推荐】
用[基于setter方法的依赖注射](http://docs.spring.io/spring/docs/4.3.10.RELEASE/spring-framework-reference/htmlsingle/#beans-setter-injection)取代基于构造函数的依赖注入来解决循环依赖。

### Spring注解@Resource和@Autowired区别对比

@Resource和@Autowired都是做bean的注入时使用，其实@Resource并不是Spring的注解，它的包是javax.annotation.Resource，需要导入，但是Spring支持该注解的注入。

#### 1、共同点

两者都可以写在字段和setter方法上。两者如果都写在字段上，那么就不需要再写setter方法。

#### 2、不同点

##### （1）@Autowired

@Autowired为Spring提供的注解，需要导入包org.springframework.beans.factory.annotation.Autowired;只按照byType注入。

```java
public class TestServiceImpl {
    // 下面两种@Autowired只要使用一种即可
    @Autowired
    private UserDao userDao; // 用于字段上

    @Autowired
    public void setUserDao(UserDao userDao) { // 用于属性的方法上
        this.userDao = userDao;
    }
}
```

@Autowired注解是按照类型（byType）装配依赖对象，默认情况下它要求依赖对象必须存在，如果允许null值，可以设置它的required属性为false。如果我们想使用按照名称（byName）来装配，可以结合@Qualifier注解一起使用。(通过类型匹配找到多个candidate,在没有@Qualifier、@Primary注解的情况下，会使用对象名作为最后的fallback匹配)如下：

```java

public class TestServiceImpl {
    @Autowired
    @Qualifier("userDao")
    private UserDao userDao;
}
```

##### （2）@Resource

@Resource默认按照ByName自动注入，由J2EE提供，需要导入包javax.annotation.Resource。@Resource有两个重要的属性：name和type，而Spring将@Resource注解的name属性解析为bean的名字，而type属性则解析为bean的类型。所以，如果使用name属性，则使用byName的自动注入策略，而使用type属性时则使用byType自动注入策略。如果既不制定name也不制定type属性，这时将通过反射机制使用byName自动注入策略。

```java
public class TestServiceImpl {
    // 下面两种@Resource只要使用一种即可
    @Resource(name="userDao")
    private UserDao userDao; // 用于字段上

    @Resource(name="userDao")
    public void setUserDao(UserDao userDao) { // 用于属性的setter方法上
        this.userDao = userDao;
    }
}
```

注：最好是将@Resource放在setter方法上，因为这样更符合面向对象的思想，通过set、get去操作属性，而不是直接去操作属性。

@Resource装配顺序：

* ①如果同时指定了name和type，则从Spring上下文中找到唯一匹配的bean进行装配，找不到则抛出异常。

* ②如果指定了name，则从上下文中查找名称（id）匹配的bean进行装配，找不到则抛出异常。

* ③如果指定了type，则从上下文中找到类似匹配的唯一bean进行装配，找不到或是找到多个，都会抛出异常。

* ④如果既没有指定name，又没有指定type，则自动按照byName方式进行装配；如果没有匹配，则回退为一个原始类型进行匹配，如果匹配则自动装配。

@Resource的作用相当于@Autowired，只不过@Autowired按照byType自动注入。
