# 面试题

----
有机会整理。

[Android面试题总结【完整详细版本"一"】（含答案）](https://blog.csdn.net/m0_37868230/article/details/81457720)

[Android2018面试题总结（真的很全面哦~ Android篇）](https://www.jianshu.com/p/dab1fcf0109d)

[Android拿高薪面试题必看](https://blog.csdn.net/u013651026/article/details/79547022)

[40个比较重要的Android面试题](https://www.cnblogs.com/WangQuanLong/p/5826098.html)

[Android面试题集锦（2019最新总结）](https://blog.csdn.net/qq_17678217/article/details/87177493)

[2019年Android面试题及答案收集](https://blog.csdn.net/jun5753/article/details/83062889)

----

## 组件

### 四大组件是什么

```text
Activity【活动】：用于表现功能。

Service【服务】：后台运行服务，不提供界面呈现。

BroadcastReceiver【广播接收器】：用来接收广播。

Content Provider【内容提供商】：支持在多个应用中存储和读取数据，相当于数据库。
```

### 四个组件的生命周期

```text
Activity生命周期图及 Fragment生命周期图

![activity_life.png](https://i.loli.net/2019/11/07/RhbAw3lLarSOuMJ.png)

![fragment_life.png](https://i.loli.net/2019/11/07/BksYmWZPp2Dx3cK.png)

Service的生命周期：首先Service有两种启动方式，而在这两种启动方式下，它的生命周期不同。

通过startService()方法启动的服务

初始化结束后系统会调用 void onStart(Intent intent) 方法，用于处理传递给startService()的Intent对象。如音乐服务会打开Intent 来探明将要播放哪首音乐，并开始播放。注意：多次调用startService()方法会多次触发onStart()方法。

通过bindService ()方法启动的服务

 初始化结束后系统会调用 IBinder onBind(Intent intent) 方法，用来绑定传递给bindService 的Intent 的对象。注意：多次调用bindService()时，如果该服务已启动则不会再触发此方法。
```

### Handler【Android SDK提供给开发者方便进行异步消息处理的类】

```text
AsyncTask、retrofit都对Handler进行了封装。
```

#### Handler四大组件

```text
1）Message

Message是在线程之间传递的消息，它可以在内部携带少量的信息，用于在不同线程之间交换数据。

例：Message的what字段、arg1字段、arg2字段来携带整型数据，obj字段携带一个Object对象。

2）Handler

处理者，它主要用来发送和处理消息。发送消息一般是使用Handler的sendMessage()方法，消息经过处理后，最终传递到Handler的handlerMessage()方法中。

3）MessageQueue

消息队列，它主要用来存放所有通过Handler发送的消息，这部分消息会一直存在于消息队列中，等待被处理。

注意：每个线程中只会有一个MessageQueue对象。

4）Looper

是每个线程中MessageQueue的管家，调用Looper的loop()方法后，就会进入到一个无限循环当中，每当发现MessageQueue中存在一条消息，就会将其取出传递到Handler的handleMessage()方法当中。

注意：每个线程中只会有一个Looper对象。
```

#### 异步消息处理流程

```text
1）在主线程当中创建一个Handler对象；

2）重写handleMessage()方法；

3）当子线程需要进行UI操作时，创建一个Message对象，并通过Handler将消息发送出去；

4）消息添加到MessageQueue的队列中等待被处理；

5）Looper在MessageQueue中取出待处理消息，发回Handler的handleMessage()方法中。

【由于Handler是在主线程中创建的，因此我们的handleMessage()方法中的代码也会在主线程中执行，避免了异常的产生】

Handler消息机制：

作用：跨线程通信。当子线程中进行耗时操作后需要更新UI时，通过Handler将有关UI的操作切换到主线程中执行。
四要素：

* Message（消息）：需要被传递的消息，其中包含了消息ID，消息处理对象以及处理的数据等，由MessageQueue统一列队，最终由Handler处理。
* MessageQueue（消息队列）：用来存放Handler发送过来的消息，内部通过单链表的数据结构来维护消息列表，等待Looper的抽取。
* Handler（处理者）：负责Message的发送及处理。通过 Handler.sendMessage() 向消息池发送各种消息事件；通过 Handler.handleMessage() 处理相应的消息事件。
* Looper（消息泵）：通过Looper.loop()不断地从MessageQueue中抽取Message，按分发机制将消息分发给目标处理者。

* Handler.sendMessage()发送消息时，会通过MessageQueue.enqueueMessage()向MessageQueue中添加一条消息；
* 通过Looper.loop()开启循环后，不断轮询调用MessageQueue.next()；
* 调用目标Handler.dispatchMessage()去传递消息，目标Handler收到消息后调用Handler.handlerMessage()处理消息。
```

### fragment各种情况下的生命周期

```text
 由于Fragment的生命周期与Activity的生命周期有着牵扯，所以把两者的图放到一起作为对比理解。

 ![Fragment的生命周期与Activity的生命周期](https://github.com/shencang/note/blob/master/Android/image/interview/activity-fragment-life.png)

 接下来就不同情况下的Fragment生命周期做一简单介绍：
```

### Fragment在Activity中replace

新替换的Activity：onAttach() ---> onCreate() ---> onCreatView() ---> onViewCreated ---> onActivityCreated() ---> onStart --->onResume()

被替换的Activity：onPause() ---> onStop() ---> onDestoryView() ---> onDestory() ---> onDetach()

### Fragment在Activity中replace，并addToBackStack

新替换的Fragment（没有在BackStack中）：onAttach > onCreate > onCreateView > onViewCreated > onActivityCreated > onStart > onResume

新替换的Fragment（已经在BackStack中）：onCreateView > onViewCreated > onActivityCreated > onStart > onResume

被替换的Fragment：onPause > onStop > onDestroyView

### Fragment在ViewPager中切换

```text
我们称切换前的的Fragment称为PreviousFragment，简称PF；切换后的Fragment称为NextFragment，简称NF；其他Fragment称为OtherFragment，简称OF。

（在ViewPager中setUserVisibleHint能反映出Fragment是否被切换到后台或前台，所以在这里也当作生命周期）

如果相关的Fragment没有被加载过：
NF： setUserVisibleHint(false)【用户不可见】 > onAttach > onCreate > setUserVisibleHint(true)【用户可见】 > onCreateView > onViewCreated > onActivityCreated > onStart > onResume

OF跟NF相邻： setUserVisibleHint(false) > onAttach > onCreate > onCreateView > onViewCreated > onActivityCreated > onStart > onResume

如果相关的Fragment已经被加载过：
NF跟PF相邻  ：setUserVisibleHint(true)

NF跟PF不相邻：setUserVisibleHint(true) > onCreateView > onViewCreated > onActivityCreated > onStart > onResume

PF跟NF相邻  ：setUserVisibleHint(false)

PF跟NF不相邻：setUserVisibleHint(false) > onPause > onStop > onDestroyView

OF跟PF相邻：onPause > onStop > onDestroyView

OF跟NF相邻：onCreateView > onViewCreated > onActivityCreated > onStart > onResume

OF夹在PF和NF中间：不调用任何生命周期方法

NF跟PF相邻  ：setUserVisibleHint(true)

NF跟PF不相邻：setUserVisibleHint(true) > onCreateView > onViewCreated > onActivityCreated > onStart > onResume

PF跟NF相邻  ：setUserVisibleHint(false)

PF跟NF不相邻：setUserVisibleHint(false) > onPause > onStop > onDestroyView

OF跟PF相邻：onPause > onStop > onDestroyView

OF跟NF相邻：onCreateView > onViewCreated > onActivityCreated > onStart > onResume

OF夹在PF和NF中间：不调用任何生命周期方法

如果重写了FragmentPagerAdapter的DestroyItem方法，并且相关的Fragment已经加载过：
相互切换时只会调用setUserVisibleHint
```

### Fragment进入了运行状态

Fragment在进入运行状态时，以下四个生命周期会随它所属的Activity一起被调用：

onPause() ---> onStop() ---> onStart() ---> onResume()

关于Fragment的onActivityResult方法：
使用Fragment的startActivity方法时，FragmentActivity的onActivityResult方法会回调相应的Fragment的onActivityResult方法，所以在重写FragmentActivity的onActivityResult方法时，注意调用super.onActivityResult。

## 启动模式

```text
1、standard：标准化启动模式

每启动一个Activity，都会重新创建Activity的新的实例，将其放在栈的顶部。不需要考虑这个实例是否已经存在。

每一次启动，它的onCreate()、onStart()、onResume()方法都会被依次调用。

2、singleTop：栈顶复用模式

当前栈中已经有该Activity实例，并且该实例位于栈顶时，会去调用onNewIntent()方法。

当前栈中已有该Activity的实例但是该实例不在栈顶时，依然会去创建Activity。

当前栈中不存在该Activity实例时，会去新创建一个该Activity。

应用场景：IM对话框、新闻客户端推送。

3、singleTask：栈内复用模式

它主要检测【寻找，通过taskAffinity】整个栈中是否已经存在当前想要启动的Activity，存在的话直接将该Activity置于栈顶，之前位于该Activity上面的Activity将被销毁，同时调用onNewIntent()方法，而不存在的话进行创建。

应用场景：应用主界面。

4、singleInstance：

一个人独享一个任务栈。当该Activity启动时，系统会创建一个新的任务栈，同时将Activity放到这个新的任务栈当中，有别的应用来启动该Activity时，由于栈内复用的特性，不会再去创建相应Activity任务栈，而是这两个应用独享一个Activity实例。

例如：应用A中现有两个Activity E、Activity F，为standard启动模式，应用B中有一个Activity G，但其启动模式是singleInstance。应用A想用应用B任务栈当中的Activity G，尽管在不同的应用下，但是应用A仍然会直接复用Activity G。

特性：

1、以SingleInstance模式启动的Activity具有全局唯一性【全局唯一性即指在整个系统当中只会存在一个这样的实例】；

2、如果在启动这样一个Activity时，【整个系统都是单例的】，已经存在了一个实例；

3、以SingleInstance模式启动的Activity具有独占性。

应用场景：呼叫来电。
```

### 问题：onNewIntent()调用时机

```text
singleTop：如果新Activity已经位于任务栈的栈顶，就不会重新创建，并回调 onNewIntent(intent) 方法。

singleTask：只要该Activity在一个任务栈中存在，都不会重新创建，并回调 onNewIntent(intent) 方法。
```

### Activity的四种启动模式对比

```text
Standard:标准的启动模式，如果需要启动一个activity就会创建该activity的实例。也是activity的默认启动模式。

SingeTop:如果启动的activity已经位于栈顶，那么就不会重新创建一个新的activity实例。而是复用位于栈顶的activity实例对象。如果不位于栈顶仍旧会重新创建activity的实例对象。

SingleTask:设置了singleTask启动模式的activity在启动时，如果位于activity栈中，就会复用该activity，这样的话，在该实例之上的所有activity都依次进行出栈操作，即执行对应的onDestroy()方法，直到当前要启动的activity位于栈顶。一般应用在网页的图集，一键退出当前的应用程序。

singleInstance:如果使用singleInstance启动模式的activity在启动的时候会复用已经存在的activity实例。不管这个activity的实例是位于哪一个应用当中，都会共享已经启动的activity的实例对象。使用了singlestance的启动模式的activity会单独的开启一个共享栈，这个栈中只存在当前的activity实例对象。
```

## 网络协议

```text
协议：【协议指计算机通信网络中两台计算机之间进行通信所必须共同遵守的规定或规则】
```

### HTTP协议

#### 基本概念

```text
【超文本传输协议】允许将HTML（超文本标记语言）文档从Web服务器传送到客户端的浏览器。HTTP协议是基于TCP/IP通信协议来传输数据的，可以从服务器端获取图片等数据资源。

URI：【uniform resource identifier】统一的资源标识符，用来唯一的标识一个资源。强调资源！！！
```

#### 组成部分

```text
1）访问资源的命名机制；file

2）存放资源的主机名；

3）资源自身的名称，由路径表示，着重于强调资源。

例：file://a:1234/b/c/d.txt   表示资源目标在a主机下的1234端口的b目录下的c目录下的d.txt文件。
```

#### URL

```text
【uniform resource Location】统一资源定位器，是一种具体的URI。即URL可以用来标识一个资源，而且还指明了如何定位这个资源。强调路径！！！
```

#### URL组成部分

```text
1）协议；

2）存有该资源的主机IP地址；

3）主机资源的具体地址。
```

#### HTTP协议特点

```text
1）简单快速；

2）无连接；【限制每次链接只处理一个请求，服务器处理完客户的请求之后会收到客户端的应答，再断开链接，节省了重复的时间】；

3）无状态：【没有记忆能力，】

HTTP协议的request/response请求头原理剖析：

request有可能经过代理服务器到达web服务器

代理服务器最主要的作用：提高访问速度【大部分代理服务器都具有缓存功能，当你再次访问前一个网络请求时，就可以直接从代理服务器中获取，而不需要请求我们的web服务器】。
```

#### HTTP协议容易混淆知识点

##### （1）http1.0与http1.1的具体区别

```text
http处于计算机网络的应用层。

1）缓存处理

2）带宽优化及网络连接的使用

3）Host头使用：1.1上请求操作和响应操作都支持Host头，而且在请求消息中如果没有Host头的话会报告一个400错误。

4）长连接：在一个TCP连接上，可以传送多个HTTP请求和响应，而不是发送一个HTTP请求就断开一个连接，再发送一个HTTP请求再建立一个连接。
```

##### 存在的问题

```text
1）传输数据时，每次都需要重新创建连接，增加了大量的延迟时间；

2）传输数据时，所有传输的内容都是明文，客户端和服务器端都无法验证对方的身份；

3）使用时，header里携带的内容过大，增加了传输成本。
```

##### （2）get / post方法的区别

```text
1）提交的数据：get提交的数据一般会放在我们的URL之后，用“  ？”来分割；而post提交数据都会放在我们entity-body【消息主体】当中。

2）提交的数据大小是否有限制：get提交的数据是有限制的，因为url是有限制的，不能无限制的输入一个url地址；而post方法提交的是body，因此没有限制。

3）取得变量的值：get方法通过Request.QueryString()来取得变量的值，而post方法通过Request.Form来取得变量的值。

4）安全问题：get提交数据一定会带来安全问题
```

##### （3）Cookie和Session的区别

###### 1）cookie【用户身份的标识】

```text
客户端的解决方案。是由服务器发给客户端的特殊信息，而这些信息以文本文件的方式存放在客户端，然后客户端每次向服务器发送请求的时候都会带上这些特殊的信息。存放在响应头里面。

客户端 向服务端发送一个HTTP Request请求；

服务端给客户端一个HTTP Response ，并且把它的cookies设置给我们的客户端；

客户端将HTTP Request和cookies打包给我们的服务端；

服务端会根据客户端给我们的cookies来进行指定的判断，返回HTTP Response给我们的客户端。

此方法弥补了我们HTTP协议无状态的不足。之前当上述请求响应操作完成后，服务端和客户端就断开连接，服务端就无法从连接上跟踪我们所想要的客户端。
```

###### 2）session

```text

另一种记录客户状态的限制，cookie保存在客户端浏览器中，而session保存在服务器上。客户端浏览器访问服务器时，服务器把客户端信息以某种形式记录在服务器上。

创建session；
在创建session同时，服务器会为该session生成唯一的session id；

在session被创建之后，就可以调用session相关的方法往session中增加内容；

当客户端再次发送请求的时候，会将这个session id带上，服务器接收到请求之后就会依据session id找到相应的session。
```

###### 3）区别

```text
存放的位置不同；

存取的方式不同【cookie保存的是Ascii码字符串，而session中能够保存任何类型的数据】；

安全性上的不同【cookie存放在客户端浏览器中，对我们客户端可见，客户端的一些程序就有可能去修改我们cookie的内容，而session则不然，它存储在服务端上，对客户端是透明的，不存在敏感信息泄露的风险】；

有效期上的不同【一般我们会设置cookie过期时间， session依赖 id，若id设置为-1，当关掉浏览器session就会失效】；对服务器的造成的压力不同【cookie保存在客户端不占用客户资源，session保存在服务端，每一个用户都会产生一个session。在并发很多用户时cookie是一个很好的选择】。
```

#### HTTPS协议

```text
基本概念：对工作在以加密连接（SSL / TLS）上的常规HTTP协议。通过在TCP和HTTP之间加入TLS【Transport Layer Security】来加密。

SSL / TLS协议：安全传输协议，TLS是SSL的升级版，也是现阶段所使用的协议；
```

##### HTTPS传输速度

```text
1）通信慢；

2）SSL必须进行加密处理。
```

##### TLS / SSL握手

```text
1）密码学原理

对称加密：加密数据所用的密钥和解密数据所用的密钥相同。

非对称加密：分私有密钥和公有密钥。

2）数字证书：互联网通讯中标志通讯各方身份信息的一串数字。

3）握手过程

```

## 刷题记录

### 1.当Activity 被消毁时，如何保存它原来的状态（）

* 实现Activity 的 onSaveInstanceState（）方法

### 2.下面关于AndroidUI 框架描述的选项中有误的一项是（）

* ViewGroup 是一个可以将一些信息绘制在屏幕上并与用户产生交互的对象。

```text
View是所有UI组件的基类，而ViewGroup是容纳View及其派生类的容器，ViewGroup也是从View派生出来的。一般来说，开发UI界面都不会直接使用View和ViewGroup（自定义控件的时候使用），而是使用其派生类。
```

### 3.Android 开发中常用的开发与调试工具有很多，下面相关描述不对的是（）

* Android 调试桥 (adb) 是一种功能多样的命令行工具，可让您与设备进行通信。adb 命令便于执行各种设备操作（例如安装和调试应用）

### 4.下面说法错误的是（）

* Window Manager（窗口管理器）管理所有的移动设备窗口功能。

 ```text
      window 有三种类型，分别是应用 Window、子 Window 和系统 Window。应用类 Window 对应一个 Acitivity，子 Window 不能单独存在，需要依附在特定的父 Window 中，比如常见的一些 Dialog 就是一个子 Window。系统 Window是需要声明权限才能创建的 Window，比如 Toast 和系统状态栏都是系统 Window。
      Window 是一个抽象类，表示一个窗口，它的具体实现类是 PhoneWindow，实现位于 WindowManagerService 中。
 ```

### 5.service的启动方法有

1 startService()
2 bindService()

### 6.ListView／RecycleView什么情况下会卡顿，常用的优化手段有哪些?（）

 ```text
    ListView在以下情况会有卡顿：
    1,listview的多层嵌套，多次的onMessure导致卡顿
    2.ADapter数据列表的整体刷新，而非单个受影响的数据刷新（notifySetDataChanged）
    3.在getView方法里inflate的row 嵌套太深（布局过于复杂）或者是布局里面有大图片或者背景所致
    4,在getView方法里ViewHolder初始化后的赋值或者是多个控件的显示状态和背景的显示没有优化好，抑或是里面含有复杂的计算和耗时操作
    5，Adapter的getView方法里面convertView没有使用setTag和getTag方式
    对于此，首先要减少层级，对改变的数据单独刷新，减少复杂计算和耗时操作优化图片素材。减少自适应尺寸的组件数量


    RecycleView在以下情况会有卡顿：
    1,RecyclerView层级较高
    2.RecyclerView布局不等高，需要在绘制item时频繁计算
    3.单次缓存资源较多
    4.在onBindViewHolder/getView方法中，过多的逻辑判断，临时变量
    5.数据列表的整体刷新，而非单个受影响的数据刷新
    对于此，首先要减少层级，对改变的数据单独刷新，减少复杂计算和耗时操作优化图片素材。
    对于不需要动态改变尺寸的item，设置为等高减少计算，
    在onBindViewHolder/getView方法中，减少逻辑判断，减少临时对象创建
    适当控制单次缓存数量
 ```

### 7.ANR产生的原因及解决方法

 ```text
    1）输入事件(按键和触摸事件)5s内没被处理

    2）BroadcastReceiver的事件(onRecieve方法)在规定时间内没处理完(前台广播为10s，后台广播为60s)

    3）service 前台20s后台200s未完成启动  

    4）ContentProvider的publish在10s内没进行完

    为了避免发生ARN不应该在Ui线程做耗时操作，如网络请求，复杂的数据库查询，耗时计算等。对于耗时的工作应放在非ui线程去做，利用广播，handler等进行线程间通信，刷新ui。

其他：

    ANR定义：在Android上，如果你的应用程序有一段时间响应不够灵敏，系统会向用户显示一个对话框，这个对话框称作应用程序无响应（ANR：Application Not Responding）对话框。用户可以选择“等待”而让程序继续运行，也可以选择“强制关闭”。所以一个流畅的合理的应用程序中不能出现anr，而让用户每次都要处理这个对话框。因此，在程序里对响应性能的设计很重要，这样系统不会显示ANR给用户。
    默认情况下，在android中Activity的最长执行时间是5秒，BroadcastReceiver的最长执行时间则是10秒。

    产生原因：
    1 应用进程自身引起：
    1.1.调用thread的join()方法、sleep()方法、wait()方法或者其他线程持有锁或者其它线程终止或崩溃导致主线程等待超时；
    1.2.service binder的数量达到上限，system server中发生WatchDog ANR，service忙导致超时无响应
    1.3.在主线程中做了非常耗时的操作：像耗时的网络访问，大量的数据读写，数据库操作，硬件操作（比如camera)，耗时的计算如操作位图；
    2 其他进程引起的，比如：其他进程CPU占用率过高，导致当前应用进程无法抢占到CPU时间片。常见的问题如文件读写频繁，io进程CPU占用率过高，导致当前应用出现ANR；
    解决方法：
    1.不要让主线程进行耗时工作
    1.1 在关键生命周期方法里尽量少的创建新的操作(可使用重新开启子线程的方式，使用Handler+Message异步更新UI，还可以用asyntask异步任务方式）
    1.2 避免在BroadcastReceiver和子线程里做耗时的操作或计算，应该使用Service
    1.3 避免在Broadcast Receiver里启动一个Activity（会发生焦点的抢夺，使用通知管理）
    2，不要让其他线程阻塞主线程的执行
 ```

### 8.关于AlertDialog描述错误的是()

create()方法创建并显示对话框

AlertDialog的构造方法被声明为protected，所以不能直接使用new关键字来创建AlertDialog类的对象实例。要想创建AlertDialog对话框，需要使用Builder类，该类是AlertDialog类中定义的一个内嵌类。因此必须创建AlertDialog.Builder类的对象实例，然后再调用show()来显示对话框。

AlertDialog不能直接用new关键字构建对象,而必须使用其内部类Builder,因为其构造器都是保护的，所以不允许非子类调用；

### 9.下列关于文件索引结构的叙述中，哪一个是错误的

 ```text
* 采用索引结构，逻辑上连续的文件存放在连续的物理块中(x)
* 系统为每个文件建立一张索引表
* 索引结构的优点是访问速度快，文件长度可以动态变化
* 索引结构的缺点是存储开销大

采用索引这种结构，逻辑上连续的文件可以存放在若干不连续的物理块中，但对于每个文件，在存储介质中除存储文件本身外，还要求系统另外建立一张索引表。 索引结构既适用于顺序存取，也适用于随机存取，并且访问速度快，文件长度可以动态变化。 索引结构的缺点 是由于使用了索引表而增加了存储空间的开销。
 ```

### 10.Android系统对下列哪些对象提供了资源池

 ```text
正确答案: A C

* Message
* Thread
* AsyncTask
* Looper

A.Message提供了消息池，有静态方法Obtain从消息池中取对象；

B.Thread默认不提供资源池，除非使用线程池ThreadPool管理；

C.AsynTask是线程池改造的，池里 默认提供（核数+1）个线程进行并发操作，最大支持（核数  * 2 + 1）个线程，超过后会丢弃其他任务；

D.Looper，每个Looper创建时创建一个消息队列和线程对象，也不是资源池；
 ```

### 11.对于一个已经存在的 SharedPreferences 对象 setting ，想向其中存入一个字符串 ”person”,”setting” 应该先调用什么方法

* edit（）

```text
这个题虽然是安卓的内容，但是可以了解一下。
SharedPreferences他是安卓中的一个轻型的数据存储方式，它的本质是基于xml文件存储key-value键值对数据，通常适用于存储一些配置信息。
使用步骤
    1.通过Context上下文来过去到SharePreferences对象
    2.调用SharePreferences的edit()方法返回一个Editor对象
    3.在通过Editor的putXXX(key , value);方法设置数据
    4. 在通过Editor的  commit(); 方法 关闭对象
```

### 12.下列关于View、Activity、Window的表述正确的是？（）

* 每一个Activity分配唯一个PhoneWindow
* DecorView是PhoneWindow的根视图
* Activity的setContentView()方法必须在Activity完成attach之后调用

```text

```

### 13.SharedPreferences保存文件的路径和扩展名是

* /data/data/package name/shared_prefs/   *.xml

```text
SharedPreferences是Android平台上一个轻量级的存储类，用来保存应用的一些常用配置，比如Activity状态，Activity暂停时，将此activity的状态保存到SharedPereferences中；当Activity重载，系统回调方法onSaveInstanceState时，再从SharedPreferences中将值取出。
以xml方式来保存
```

### 14.关于 android 中播放视频的说法不对的是 ___

* 可以使用SurfaceView组件播视频
* 可以使用VideoView组件播视频
* VideoView组件可以控制播放的位置和大小
* VideoView播放视频的格式可以是3gp

![14](https://i.loli.net/2019/11/11/ozWdXIguTAjVCHv.png)
