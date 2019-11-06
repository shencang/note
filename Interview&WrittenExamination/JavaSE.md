# javaSE

* 1.如果一个进程在运行过程中占用的内存无限制上升，那么该进程有内存泄漏

* 2.访问修饰符作用范围由大到小排列:public>protected>default>private
    
      default：包内的任何类，重点突出包
      protected：包内的任何类及包外继承了该类的子类，重点突出继承
      
* 3.Java中的异常:可不检测（unchecked）异常:包括运行时异常（RuntimeException与其子类）和错误（Error）。
       
      异常可以分为检查异常和非检查异常.
      检查异常顾名思义就是需要进行检查的异常, 需要使用try catch捕获或者throws抛出. (除去runtimeException及其子类的exception及其子类)
      非检查异常 : runtimeException 及其子类, 还有Error(Error也属于异常, 并且属于非检查异常)
      
* 4.在数据库系统中，产生不一致的根本原因是：
* 并发控制不当
* 数据冗余
* 未对数据进行完整性控制


* 5.class：编译后的Java文件 ；
* .java：是未编译的Java程序；
* .jsp：是Java 服务器页面技术，支持Java代码的动态网页；
* .xml：可拓展文本标记语言，一种文本格式，常用来做配置文件；
* .jar：一种压缩包格式，常用来打包 Java 类库。

* 6.下面这段代码，当 T 分别是引用类型和值类型的时候，分别产生了多少个 T 对象（1 ，1）
T t = new T();
Func(t);
Func 定义如下：
public void Func(T t) {  }

* 7.java中下面哪个能创建并启动线程（）
```java
public class MyRunnable implements Runnable          { 
     public void run()             { 
         //some code here 
     } 
 }
```

new Thread(new MyRunnable()).start()

![thread](https://github.com/shencang/note/blob/master/Interview%26WrittenExamination/image/thread.png)


* 8.RuntimeException是Throwable的一个子类，它指示合理的应用程序不应试图捕获的严重问题。

（An RuntimeException is a subclass of Throwable that indicates serious problems that a reasonable application should not try to catch.）

运行时异常： 都是RuntimeException类及其子类异常，如NullPointerException(空指针异常)、IndexOutOfBoundsException(下标越界异常)等，这些异常是不检查异常，程序中可以选择捕获处理，也可以不处理。这些异常一般是由程序逻辑错误引起的，程序应该从逻辑角度尽可能避免这类异常的发生。运行时异常的特点是Java编译器不会检查它，也就是说，当程序中可能出现这类异常，即使没有用try-catch语句捕获它，也没有用throws子句声明抛出它，也会编译通过。

非运行时异常 （编译异常）： 是RuntimeException以外的异常，类型上都属于Exception类及其子类。从程序语法角度讲是必须进行处理的异常，如果不处理，程序就不能编译通过。如IOException、SQLException等以及用户自定义的Exception异常，一般情况下不自定义检查异常。

![exception](https://github.com/shencang/note/blob/master/Interview%26WrittenExamination/image/exception.png)

* 9.下面哪些具体实现类可以用于存储键，值对，并且方法调用提供了基本的多线程安全支持：()


    java.util.ConcurrentHashMap与java.util.Hashtable
    
    
    Hashtable的方法都是synchrnized修饰的线程安全，
    ConcurrentHashMap并发容器，JDK7采用分段锁，JDK8采用CAS算法，线程安全，建议使用，Connections工具类提供了一个方法synchrnizedMap可以把Map同步，本质就是给每一个方法加上synchrnized关键字进行同步


* 10.JavaWEB中有一个类，当会话种邦定了属性或者删除了属性时，他会得到通知，这个类是：(  HttpSessionAttributeListener  )


    HttpSessionAttributeListener：可以实现此侦听器接口获取此web应用程序中会话属性列表更改的通知；
    
    HttpSessionBindingListener：当该对象从一个会话中被绑定或者解绑时通知该对象，这个对象由HttpSessionBindingEvent对象通知。这可能是servlet程序显式地从会话中解绑定属性的结果，可能是由于会话无效，也可能是由于会话超时；
    
    HttpSessionObjectListener：没有该接口API；
    
    HttpSessionListener：当web应用程序中的活动会话列表发生更改时通知该接口的实现类，为了接收该通知事件，必须在web应用程序的部署描述符中配置实现类；
    
    HttpSessionActivationListener：绑定到会话的对象可以侦听容器事件，通知它们会话将被钝化，会话将被激活。需要一个在虚拟机之间迁移会话或持久会话的容器来通知所有绑定到实现该接口会话的属性。

* 11.以下哪些jvm的垃圾回收方式采用的是复制算法回收

    新生代串行收集器，新生代并行回收收集器
    
    
    两个最基本的java回收算法：复制算法和标记清理算法
    复制算法：两个区域A和B，初始对象在A，继续存活的对象被转移到B。此为新生代最常用的算法
    标记清理：一块区域，标记可达对象（可达性分析），然后回收不可达对象，会出现碎片，那么引出
    标记-整理算法：多了碎片整理，整理出更大的内存放更大的对象
    两个概念：新生代和年老代
    新生代：初始对象，生命周期短的
    永久代：长时间存在的对象
    整个java的垃圾回收是新生代和年老代的协作，这种叫做分代回收。
    P.S：Serial New收集器是针对新生代的收集器，采用的是复制算法
    Parallel New（并行）收集器，新生代采用复制算法，老年代采用标记整理
    Parallel Scavenge（并行）收集器，针对新生代，采用复制收集算法
    Serial Old（串行）收集器，新生代采用复制，老年代采用标记整理
    Parallel Old（并行）收集器，针对老年代，标记整理
    CMS收集器，基于标记清理
    G1收集器：整体上是基于标记 整理 ，局部采用复制
    
    综上：新生代基本采用复制算法，老年代采用标记整理算法。cms采用标记清理。


* 12.以下哪个接口的定义是正确的？（ ）

```java
interface  B
      {  void  print();}
```

    虽然说在Java8可以在接口中定义静态方法了（此处定义指的是含body的实现），
    但是不能只声明，只声明的会被编译器识别为抽象方法，而抽象方法不能用static修饰

* 13.Java程序初始化顺序：

    父类的静态代码块
    子类的静态代码块
    父类的普通代码块
    父类的构造方法
    子类的普通代码块
    子类的构造方法
    
    
* 14.下面有关struts1和struts2的区别，描述错误的是？B
  
  Struts1要求Action类继承一个抽象基类。Struts 2 Action类可以实现一个Action接口
  
  Struts1 Action对象为每一个请求产生一个实例。Struts2 Action是单例模式并且必须是线程安全的
  
  Struts1 Action 依赖于Servlet API，Struts 2 Action不依赖于容器，允许Action脱离容器单独被测试
  
  Struts1 整合了JSTL，Struts2可以使用JSTL，但是也支持OGNL
    
    从action类上分析:
    1.Struts1要求Action类继承一个抽象基类。Struts1的一个普遍问题是使用抽象类编程而不是接口。 
    2. Struts 2 Action类可以实现一个Action接口，也可实现其他接口，使可选和定制的服务成为可能。Struts2提供一个ActionSupport基类去实现常用的接口。Action接口不是必须的，任何有execute标识的POJO对象都可以用作Struts2的Action对象。
    从Servlet 依赖分析: 
    3. Struts1 Action 依赖于Servlet API ,因为当一个Action被调用时HttpServletRequest 和 HttpServletResponse 被传递给execute方法。 
    4. Struts 2 Action不依赖于容器，允许Action脱离容器单独被测试。如果需要，Struts2 Action仍然可以访问初始的request和response。但是，其他的元素减少或者消除了直接访问HttpServetRequest 和 HttpServletResponse的必要性。
    从action线程模式分析: 
    5. Struts1 Action是单例模式并且必须是线程安全的，因为仅有Action的一个实例来处理所有的请求。单例策略限制了Struts1 Action能作的事，并且要在开发时特别小心。Action资源必须是线程安全的或同步的。 
    6. Struts2 Action对象为每一个请求产生一个实例，因此没有线程安全问题。（实际上，servlet容器给每个请求产生许多可丢弃的对象，并且不会导致性能和垃圾回收问题）


* 15.在一个基于分布式的游戏服务器系统中，不同的服务器之间，哪种通信方式是不可行的（管道）？
 
 
    对于管道，有下面这几种类型：
    ①普通管道（PIPE）：通常有两种限制，一是单工，即只能单向传输；二是血缘，即常用于父子进程间（或有血缘关系的进程间）。
    ②流管道（s_pipe）：去除了上述的第一种限制，实现了双向传输。
    
    ③命名管道（name_pipe）：去除了上述的第二种限制，实现了无血缘关系的不同进程间通信。
    显然，要求是对于不同的服务器之间的通信，是要要求全双工形式的，而管道只能是半双工，虽然可以双向，但是同一时间只能有一个方向传输，全双工和半双工的区别可以如下图示理解：

![pipe.png](https://i.loli.net/2019/11/06/qnzx5C3Rl2us8BA.png)

* 16.Java程序的种类有：


    （a）内嵌于Web文件中，由浏览器来观看的_Applet
    
    （b）可独立运行的 Application
    
    （c）服务器端的 Servlets
    
    Application
    ―Java应用程序”是可以独立运行的Java程序。
    由Java解释器控制执行。
    Applet
      ―Java小程序”不能独立运行（嵌入到Web页中）。
      由Java兼容浏览器控制执行。
    
    Serverlets
    是Java技术对CGI 编程的解决方案。
    是运行于Web server上的、作为来自于Web browser 或其他HTTP client端的请求和在server上的数据库及其他应用程序之间的中间层程序。
    Serverlets的工作是：
    读入用户发来的数据（通常在web页的form中）
    找出隐含在HTTP请求中的其他请求信息（如浏览器功能细节、请求端主机名等。
    产生结果(调用其他程序、访问数据库、直接计算)
    格式化结果（网页）
    设置HTTP response参数(如告诉浏览器返回文档格式)
    将文档返回给客户端。
    
* 17.往OuterClass类的代码段中插入内部类声明, 哪一个是错误的:(都不对)
```java
public class OuterClass{
    private float f=1.0f;
    //插入代码到这里
}
```
```java
class InnerClass{
public static float func(){return f;}
}
abstract class InnerClass{
public abstract float func(){}
}
static class InnerClass{
protected static float func(){return f;}
}
public class InnerClass{
 static float func(){return f;}
}

```


    主要考核了这几个知识点：
    1.静态内部类才可以声明静态方法
    2.静态方法不可以使用非静态变量
    3.抽象方法不可以有函数体
其他参考见[链接](https://www.nowcoder.com/test/question/done?tid=29150376&qid=5120#summary)

* 18.Java是一门支持反射的语言,基于反射为Java提供了丰富的动态性支持，下面关于Java反射的描述，哪些是错误的：( A D F   )


    A，Java反射主要涉及的类如Class, Method, Filed,等，他们都在java.lang.reflet包下
    B，通过反射可以动态的实现一个接口，形成一个新的类，并可以用这个类创建对象，调用对象方法
    C，通过反射，可以突破Java语言提供的对象成员、类成员的保护机制，访问一般方式不能访问的成员
    D,Java反射机制提供了字节码修改的技术，可以动态的修剪一个类
    E,Java的反射机制会给内存带来额外的开销。例如对永生堆的要求比不通过反射要求的更多
    F,Java反射机制一般会带来效率问题，效率问题主要发生在查找类的方法和字段对象，因此通过缓存需要反射类的字段和方法就能达到与之间调用类的方法和访问类的字段一样的效率

---
    A选项Class类位于lang包下面，D选项反射的本质就是从字节码中查找，动态获取类的整容结构，包括属性，构造器，动态调用对象的方法，而不是修剪类，F选项我觉得应该是，使用了反射的效率都会降低，就算加了缓存





# 小米面试总结：

### 类加载器的运行机制：

每个每个编写的".java"类文件都存储着需要执行的程序逻辑，这些".java"文件经过Java编译器编译成拓展名为".class"的文件，".class"文件中保存着Java代码经转换后的虚拟机指令，当需要使用某个类时，虚拟机将会加载它的".class"文件，并创建对应的class对象，将class文件加载到虚拟机的内存，这个过程称为类加载，这里我们需要了解一下类加载的过程，如下：

![类加载器](https://github.com/shencang/note/blob/master/Interview%26WrittenExamination/image/classloader.png)
    
* 加载：类加载过程的一个阶段：通过一个类的完全限定查找此类字节码文件，并利用字节码文件创建一个Class对象

* 验证：目的在于确保Class文件的字节流中包含信息符合当前虚拟机要求，不会危害虚拟机自身安全。主要包括四种验证，文件格式验证，元数据验证，字节码验证，符号引用验证。    

* 准备：为类变量(即static修饰的字段变量)分配内存并且设置该类变量的初始值即0(如static int i=5;这里只将i初始化为0，至于5的值将在初始化时赋值)，这里不包含用final修饰的static，因为final在编译的时候就会分配了，注意这里不会为实例变量分配初始化，类变量会分配在方法区中，而实例变量是会随着对象一起分配到Java堆中。

* 解析：主要将常量池中的符号引用替换为直接引用的过程。符号引用就是一组符号来描述目标，可以是任何字面量，而直接引用就是直接指向目标的指针、相对偏移量或一个间接定位到目标的句柄。有类或接口的解析，字段解析，类方法解析，接口方法解析(这里涉及到字节码变量的引用，如需更详细了解，可参考《深入Java虚拟机》)。

* 初始化：类加载最后阶段，若该类具有超类，则对其进行初始化，执行静态初始化器和静态初始化成员变量(如前面只初始化了默认值的static变量将会在这个阶段赋值，成员变量也将被初始化)。

这便是类加载的5个过程，而类加载器的任务是根据一个类的全限定名来读取此类的二进制字节流到JVM中，然后转换为一个与目标类对应的java.lang.Class对象实例，在虚拟机提供了3种类加载器，引导（Bootstrap）类加载器、扩展（Extension）类加载器、系统（System）类加载器（也称应用类加载器），下面分别介绍

* 启动（Bootstrap）类加载器
启动类加载器主要加载的是JVM自身需要的类，这个类加载使用C++语言实现的，是虚拟机自身的一部分，它负责将 <JAVA_HOME>/lib路径下的核心类库或-Xbootclasspath参数指定的路径下的jar包加载到内存中，注意必由于虚拟机是按照文件名识别加载jar包的，如rt.jar，如果文件名不被虚拟机识别，即使把jar包丢到lib目录下也是没有作用的(出于安全考虑，Bootstrap启动类加载器只加载包名为java、javax、sun等开头的类)。

* 扩展（Extension）类加载器
扩展类加载器是指Sun公司(已被Oracle收购)实现的sun.misc.Launcher$ExtClassLoader类，由Java语言实现的，是Launcher的静态内部类，它负责加载<JAVA_HOME>/lib/ext目录下或者由系统变量-Djava.ext.dir指定位路径中的类库，开发者可以直接使用标准扩展类加载器。

* 系统（System）类加载器
也称应用程序加载器是指 Sun公司实现的sun.misc.Launcher$AppClassLoader。它负责加载系统类路径java -classpath或-D java.class.path 指定路径下的类库，也就是我们经常用到的classpath路径，开发者可以直接使用系统类加载器，一般情况下该类加载是程序中默认的类加载器，通过ClassLoader#getSystemClassLoader()方法可以获取到该类加载器。
　 在Java的日常应用程序开发中，类的加载几乎是由上述3种类加载器相互配合执行的，在必要时，我们还可以自定义类加载器，需要注意的是，Java虚拟机对class文件采用的是按需加载的方式，也就是说当需要使用该类时才会将它的class文件加载到内存生成class对象，而且加载某个类的class文件时，Java虚拟机采用的是双亲委派模式即把请求交由父类处理，它一种任务委派模式，下面我们进一步了解它。

### final关键词：

#### class
   修饰类当用final去修饰一个类的时候，表示这个类不能被继承。
   
   注意：
   
   a. 被final修饰的类，final类中的成员变量可以根据自己的实际需要设计为final。
   
   b. final类中的成员方法都会被隐式的指定为final方法。说明：在自己设计一个类的时候，要想好这个类将来是否会被继承，如果可以被继承，则该类不能使用fianl修饰，在这里呢，一般来说工具类我们往往都会设计成为一个fianl类。在JDK中，被设计为final类的有String、System等。

#### 方法

   被final修饰的方法不能被重写。
   
   注意：
   
   a. 一个类的private方法会隐式的被指定为final方法。
   
   b. 如果父类中有final修饰的方法，那么子类不能去重写。
    
#### 修饰成员变量

注意：

   a. 必须初始化值。

   b. 被final修饰的成员变量赋值，有两种方式：1、直接赋值 2、全部在构造方法中赋初值。

   c. 如果修饰的成员变量是基本类型，则表示这个变量的值不能改变。

   d. 如果修饰的成员变量是一个引用类型，则是说这个引用的地址的值不能修改，但是这个引用所指向的对象里面的内容还是可以改变的。
    
    
### volatile
volatile 是一个类型修饰符。volatile 的作用是作为指令关键字，确保本条指令不会因编译器的优化而省略。
* 特性

保证了不同线程对这个变量进行操作时的可见性，即一个线程修改了某个变量的值，这新值对其他线程来说是立即可见的。（实现可见性）

禁止进行指令重排序。（实现有序性）

volatile 只能保证对单次读/写的原子性。i++ 这种操作不能保证原子性。

* 可见性实现

volatile 变量的内存可见性是基于内存屏障（Memory Barrier）实现。

内存屏障，又称内存栅栏，是一个 CPU 指令。

在程序运行时，为了提高执行性能，编译器和处理器会对指令进行重排序，JMM 为了保证在不同的编译器和 CPU 上有相同的结果，通过插入特定类型的内存屏障来禁止特定类型的编译器重排序和处理器重排序，插入一条内存屏障会告诉编译器和 CPU：不管什么指令都不能和这条 Memory Barrier 指令重排序。


### object的equals
　判断两个对象是否等价，是OOP编程中常见的需求(下面围绕Java来进行阐述)。

  对于String来说，就是其本身的name->对应的是其字符串内容。对于其他类或者自定义的内容，需要进一步制定规则做进一步处理。

  其中一个思路：
  
  * 第一步，先判断引用值是否相等，此时person1.equals(person1)这样的情况，就可以很快返回结果true。
  
　* 第二步，判断类型是否匹配，如果两个对象等价，前提是它们一定为相同的类型，此时person1.equals(null)这样的情况，也能进行判断并返回结果false。

　* 第三步，按部就班地按照预设的特征值进行对象的等价性判断。
  
说明几点:

* 1.类中的equals方法是一定要重写/覆盖(Override)的，因为要让它按照设计的需求来根据特征值判断等价性。

　　这里的特征值，就是String类型的name属性，表示每个Person对象的名字。由于在equals方法中只设定了这一个需要比较的特征值，因此只要两个Person类对象的name相同，那么他们的判断结果就是相同。

* 2.类中的hashCode方法需要重写/覆盖

　　　　事实上，当实现了1之后，就能保证判断两个对象等价性是否成立了(此时已经能保证程序中person1.equals(person2)值为true。但是这样得到的equals方法是有很大限定性的。比如把person1加入到一个HashSet中，此时判断HashSet中是否包含person2，由于在设计时，特征值只是name，那么此时期望HashSet.contains(person2)的值也应为true，但如果不实现hashCode方法，返回值只能是false。

　　　　对于这个原因，可以把Java中每个实例对象的存储过程都想象成“将包含该对象的数据‘抛到’一个桶里”，为了更快地比价，就把整个程序运行时的空间，分成相当多的“桶”，并为每个桶编号，对于桶内装载的数据，有这样的规定：为每个实例对象进行编号，只有编号相同的两个对象，它们才有可能分配到一个桶里。这样一来，要想判断两个对象是否等价(即是否能让equals方法返回true)，只需要访问这个桶就可以了，因为这两个对象一定是出现在相同的桶里的。步骤1已经实现了“找到两个对象之后，根据某个特征值进行判断”，但是并未实现“让两个对象分配到一个桶里”。这就是问题的关键所在。所以为了保证两个对象分配到相同的“桶”里，就要重写它们的hashCode方法，Java中为每种类型都默认实现了该类型的hashCode方法。下面的实现了hashCode的代码中，由于特征值是name，为了保证这两个Person类对象等价，那么它们的name一定相同，那考虑到name(Sting类型)已经实现了hashCode，此时就简单地把它们的name的hashCode值进行返回即可。这样就能保证，如果两个Person对象的name如果相同，那么它们的hashCode一定相同，同时也便于下一步判断。

　　　　注：重点在于理解这个“桶”的概念，通过这个抽象过程，便也可以很好地理解“Java中两个等价的对象一定有相同的hashCode值，但两个拥有相同hashCode值的对象不一定等价”这句话。这句话的重点就在于考虑“桶”是如何装载的、以及它“装载”的是什么类型对象等等细节。



### object的HashCode与HashMap

参考下面的hashMap的链接，非常详细

### GC
   垃圾回传机制


### 参考链接
[深入理解Java类加载器(ClassLoader)](https://blog.csdn.net/javazejian/article/details/73413292)

[Java类加载机制及自定义加载器](https://www.cnblogs.com/gdpuzxs/p/7044963.html)

[【Java 并发笔记】volatile 相关整理](https://www.jianshu.com/p/ccfe24b63d87)

[深入理解Java-GC机制](https://blog.csdn.net/qq_36314960/article/details/79923581)

[Java集合之一—HashMap](https://blog.csdn.net/woshimaxiao1/article/details/83661464)

[Java的equals方法实现及其细节](https://www.cnblogs.com/stevenshen123/p/9199354.html)

[java并发](https://www.nowcoder.com/discuss/150809?type=0&order=0&pos=9&page=0)

[java8文档](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)