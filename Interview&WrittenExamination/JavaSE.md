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


# 小米面试总结：

### 类加载器的运行机制：

每个每个编写的".java"类文件都存储着需要执行的程序逻辑，这些".java"文件经过Java编译器编译成拓展名为".class"的文件，".class"文件中保存着Java代码经转换后的虚拟机指令，当需要使用某个类时，虚拟机将会加载它的".class"文件，并创建对应的class对象，将class文件加载到虚拟机的内存，这个过程称为类加载，这里我们需要了解一下类加载的过程，如下：

![类加载器](https://github.com/shencang/note/blob/master/Interview%26WrittenExamination/image/classloader)
    
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