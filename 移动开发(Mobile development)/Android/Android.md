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

![activity_life.png](https://i.loli.net/2019/11/07/RhbAw3lLarSOuMJ.png)

![fragment_life.png](https://i.loli.net/2019/11/07/BksYmWZPp2Dx3cK.png)

```text
Activity生命周期图及 Fragment生命周期图


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

### 15.下列代码中哪个是隐式Intent的例子

```java
Intent intent=new Intent(Intent.ACTION_SEND);
intent.putExtra(Intent.EXTRA_TEXT,textMessage);
intent.setType("text/plain");
startActivity(intent);
```

```t
显式启动 是明确指定了需要启动的Activity 或 service 的类名或包名。
隐式启动 不明确制定需要启动哪个Activity，而是通过设置action、data、 Category 等让系统来匹配出合适的目标
```

### 15.阅读代码回答运行结果

```java

public classMainActivity extends Activity implements OnClickListener
{
   private Button mBtnLogin = (Button) findViewById(R.id.btn_login);
   private TextView mTextViewUser;
  
   @Override
   protected void onCreate(BundlesavedInstanceState)
   {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mTextViewUser = (TextView) findViewById(R.id.textview_user);
        mBtnLogin.setOnClickListener(this);
        new Thread()
        {
            @Override
            public void run()
            {
                mTextViewUser.setText(10);
            }
        }.start();
   }
  
   @Override
   public void onClick(View v)
   {
        mTextViewUser.setText(20);
   }
}
```

* NullPointerException

```t
Button的初始化时找不到对应的id的。id绑定应该在setContentView后执行。
代码实测：

1、首先会报错NullPointerException，就是privateButton mBtnLogin = (Button) findViewById(R.id.btn_login);这个位置，要先加载了layout后才能成功获取到相应的按钮组件对象；
2、修改NullPointerException错误后再运行，报错 Resources$NotFoundException，在mTextViewUser.setText(10);这个位置（原本以为会先检查onclick方法里的setText（），但实际是run（）里的setText（）），要改成字符串形式；
3、修改上面的错误后再运行，报错Resources$NotFoundException，这次就轮到mTextViewUser.setText(20);这个位置了；
4、修改上面的错误后再运行，没有报错，程序成功运行，点击按钮后TextView由10变为20，说好的不能在非UI线程里更新UI组件呢？翻看别人的博客后，终于找到答案了，其实非UI线程是可以刷新UI的，前提是它要拥有自己的ViewRoot，ViewRoot是在onResume（）里addview（）创建的，所以是在 onResume（）检查是否为UI线程，一般在onCreate（）中通过子线程可以更新UI，但官方不建议这样做，因为 Android UI操作并不是线程安全的。
PS：而且，可以试下在上面代码的run（）中setText（）前加一句Thread.sleep(2000)，先让线程休眠个2到3秒，就会报错 ViewRootImpl$CalledFromWrongThreadException，说明已经检查到在非UI线程里更新UI。
```

### 16.下列哪些操作会使线程释放锁资源

* wait()
* join()

![16](https://i.loli.net/2019/11/18/Q1veEuWy9j8kxfz.png)

### 17.将一个Activity设置成窗口的样式，只需设置Theme(true)

### 18.Android的四大组件是哪些，它们的作用

```t
答：Activity：Activity是Android程序与用户交互的窗口，是Android构造块中最基本的一种，它需要为保持各界面的状态，做很多持久化的事情，妥善管理生命周期以及一些跳转逻辑

service：后台服务于Activity，封装有一个完整的功能逻辑实现，接受上层指令，完成相关的事物，定义好需要接受的Intent提供同步和异步的接口

Content Provider：是Android提供的第三方应用数据的访问方案，可以派生Content Provider类，对外提供数据，可以像数据库一样进行选择排序，屏蔽内部数据的存储细节，向外提供统一的借口模型，大大简化上层应用，对数据的整合提供了更方便的途径

BroadCast Receiver：接受一种或者多种Intent作触发事件，接受相关消息，做一些简单处理，转换成一条Notification，统一了Android的事件广播模型
```

### 19. 请介绍下Android中常用的五种布局

```t
常用五种布局方式，分别是：FrameLayout（框架布局），LinearLayout （线性布局），AbsoluteLayout（绝对布局），RelativeLayout（相对布局），TableLayout（表格布局）。

一、FrameLayout：所有东西依次都放在左上角，会重叠，这个布局比较简单，也只能放一点比较简单的东西。
二、LinearLayout：线性布局，每一个LinearLayout里面又可分为垂直布局（android:orientation="vertical"）和水平布局（android:orientation="horizontal" ）。当垂直布局时，每一行就只有一个元素，多个元素依次垂直往下；水平布局时，只有一行，每一个元素依次向右排列。
三、AbsoluteLayout：绝对布局用X,Y坐标来指定元素的位置，这种布局方式也比较简单，但是在屏幕旋转时，往往会出问题，而且多个元素的时候，计算比较麻烦。
四、RelativeLayout：相对布局可以理解为某一个元素为参照物，来定位的布局方式。主要属性有：相对于某一个元素android:layout_below、      android:layout_toLeftOf相对于父元素的地方android:layout_alignParentLeft、android:layout_alignParentRigh；
五、TableLayout：表格布局，每一个TableLayout里面有表格行TableRow，TableRow里面可以具体定义每一个元素。每一个布局都有自己适合的方式，这五个布局元素可以相互嵌套应用，做出美观的界面。
```

### 20. android中的动画有哪几类，它们的特点和区别是什么

```t
答：两种，一种是Tween动画、还有一种是Frame动画。Tween动画，这种实现方式可以使视图组件移动、放大、缩小以及产生透明度的变化;另一种Frame动画，传统的动画方法，通过顺序的播放排列好的图片来实现，类似电影。
```

### 21. android 中有哪几种解析xml的类？官方推荐哪种？以及它们的原理和区别

```t
答：XML解析主要有三种方式，SAX、DOM、PULL。常规在PC上开发我们使用Dom相对轻松些，但一些性能敏感的数据库或手机上还是主要采用SAX方式，SAX读取是单向的，优点:不占内存空间、解析属性方便，但缺点就是对于套嵌多个分支来说处理不是很方便。而DOM方式会把整个XML文件加载到内存中去，这里Android开发网提醒大家该方法在查找方面可以和XPath很好的结合如果数据量不是很大推荐使用，而PULL常常用在J2ME对于节点处理比较好，类似SAX方式，同样很节省内存，在J2ME中我们经常使用的KXML库来解析。
```

### 22. ListView的优化方案

```t
答：
  1、如果自定义适配器，那么在getView方法中要考虑方法传进来的参数contentView是否为null，如果为null就创建contentView并返回，如果不为null则直接使用。在这个方法中尽可能少创建view。

   2、给contentView设置tag（setTag（）），传入一个viewHolder对象，用于缓存要显示的数据，可以达到图像数据异步加载的效果。

  3、如果listview需要显示的item很多，就要考虑分页加载。比如一共要显示100条或者更多的时候，我们可以考虑先加载20条，等用户拉到列表底部的时候再去加载接下来的20条。
```

### 23. 请介绍下Android的数据存储方式

```t
答：使用SharedPreferences存储数据；文件存储数据；SQLite数据库存储数据；使用ContentProvider存储数据；网络存储数据；

Preference，File， DataBase这三种方式分别对应的目录是/data/data/Package Name/Shared_Pref, /data/data/Package Name/files, /data/data/Package Name/database 。

一：使用SharedPreferences存储数据

首先说明SharedPreferences存储方式，它是 Android提供的用来存储一些简单配置信息的一种机制，例如：登录用户的用户名与密码。其采用了Map数据结构来存储数据，以键值的方式存储，可以简单的读取与写入，具体实例如下：

void ReadSharedPreferences(){

String strName,strPassword;

SharedPreferences   user = getSharedPreferences(“user_info”,0);

strName = user.getString(“NAME”,””);

strPassword = user getString(“PASSWORD”,””);

}

void WriteSharedPreferences(String strName,String strPassword){

SharedPreferences   user = getSharedPreferences(“user_info”,0);

uer.edit();

user.putString(“NAME”, strName);

user.putString(“PASSWORD” ,strPassword);

user.commit();

}

数据读取与写入的方法都非常简单，只是在写入的时候有些区别：先调用edit()使其处于编辑状态，然后才能修改数据，最后使用commit()提交修改的数据。实际上SharedPreferences是采用了XML格式将数据存储到设备中，在DDMS中的File Explorer中的/data/data/<package name>/shares_prefs下。使用SharedPreferences是有些限制的：只能在同一个包内使用，不能在不同的包之间使用。

二：文件存储数据

文件存储方式是一种较常用的方法，在Android中读取/写入文件的方法，与 Java中实现I/O的程序是完全一样的，提供了openFileInput()和openFileOutput()方法来读取设备上的文件。具体实例如下:

String fn = “moandroid.log”;

FileInputStream fis = openFileInput(fn);

FileOutputStream fos = openFileOutput(fn,Context.MODE_PRIVATE);

三：网络存储数据

网络存储方式，需要与Android 网络数据包打交道，关于Android 网络数据包的详细说明，请阅读Android SDK引用了Java SDK的哪些package？。

四：ContentProvider

1、ContentProvider简介

当应用继承ContentProvider类，并重写该类用于提供数据和存储数据的方法，就可以向其他应用共享其数据。虽然使用其他方法也可以对外共享数据，但数据访问方式会因数据存储的方式而不同，如：采用文件方式对外共享数据，需要进行文件操作读写数据；采用sharedpreferences共享数据，需要使用sharedpreferences API读写数据。而使用ContentProvider共享数据的好处是统一了数据访问方式。


2、Uri类简介

Uri代表了要操作的数据，Uri主要包含了两部分信息：1.需要操作的ContentProvider ，2.对ContentProvider中的什么数据进行操作，一个Uri由以下几部分组成：

1.scheme：ContentProvider（内容提供者）的scheme已经由Android所规定为：content://…

2.主机名（或Authority）：用于唯一标识这个ContentProvider，外部调用者可以根据这个标识来找到它。

3.路径（path）：可以用来表示我们要操作的数据，路径的构建应根据业务而定，如下：

要操作contact表中id为10的记录，可以构建这样的路径:/contact/10

要操作contact表中id为10的记录的name字段， contact/10/name

要操作contact表中的所有记录，可以构建这样的路径:/contact?

要操作的数据不一定来自数据库，也可以是文件等他存储方式，如下:

要操作xml文件中contact节点下的name节点，可以构建这样的路径：/contact/name

如果要把一个字符串转换成Uri，可以使用Uri类中的parse()方法，如下：

Uri uri = Uri.parse("content://com.changcheng.provider.contactprovider/contact")

3、UriMatcher、ContentUrist和ContentResolver简介

因为Uri代表了要操作的数据，所以我们很经常需要解析Uri，并从 Uri中获取数据。Android系统提供了两个用于操作Uri的工具类，分别为UriMatcher 和ContentUris 。掌握它们的使用，会便于我们的开发工作。

UriMatcher：用于匹配Uri，它的用法如下：

1.首先把你需要匹配Uri路径全部给注册上，如下：

//常量UriMatcher.NO_MATCH表示不匹配任何路径的返回码(-1)。

UriMatcher uriMatcher = new UriMatcher(UriMatcher.NO_MATCH);

//如果match()方法匹配content://com.changcheng.sqlite.provider.contactprovider /contact路径，返回匹配码为1

uriMatcher.addURI(“com.changcheng.sqlite.provider.contactprovider”, “contact”, 1);//添加需要匹配uri，如果匹配就会返回匹配码

//如果match()方法匹配 content://com.changcheng.sqlite.provider.contactprovider/contact/230路径，返回匹配码为2

uriMatcher.addURI(“com.changcheng.sqlite.provider.contactprovider”, “contact/#”, 2);//#号为通配符

2.注册完需要匹配的Uri后，就可以使用uriMatcher.match(uri)方法对输入的Uri进行匹配，如果匹配就返回匹配码，匹配码是调用 addURI()方法传入的第三个参数，假设匹配 content://com.changcheng.sqlite.provider.contactprovider/contact路径，返回的匹配码为1。

ContentUris：用于获取Uri路径后面的ID部分，它有两个比较实用的方法：

withAppendedId(uri, id)用于为路径加上ID部分

parseId(uri)方法用于从路径中获取ID部分

ContentResolver：当外部应用需要对ContentProvider中的数据进行添加、删除、修改和查询操作时，可以使用 ContentResolver 类来完成，要获取ContentResolver 对象，可以使用Activity提供的getContentResolver()方法。 ContentResolver使用insert、delete、update、query方法，来操作数据。
```

### 24. activity的启动模式有哪些？是什么含义

```t
答：在android里，有4种activity的启动模式，分别为：

“standard” (默认)

“singleTop”

“singleTask”

“singleInstance”

它们主要有如下不同：

1. 如何决定所属task

“standard”和”singleTop”的activity的目标task，和收到的Intent的发送者在同一个task内，除非intent包括参数FLAG_ACTIVITY_NEW_TASK。

如果提供了FLAG_ACTIVITY_NEW_TASK参数，会启动到别的task里。

“singleTask”和”singleInstance”总是把activity作为一个task的根元素，他们不会被启动到一个其他task里。

2. 是否允许多个实例

“standard”和”singleTop”可以被实例化多次，并且存在于不同的task中，且一个task可以包括一个activity的多个实例；

“singleTask”和”singleInstance”则限制只生成一个实例，并且是task的根元素。 singleTop要求如果创建intent的时候栈顶已经有要创建的Activity的实例，则将intent发送给该实例，而不发送给新的实例。

3. 是否允许其它activity存在于本task内

“singleInstance”独占一个task，其它activity不能存在那个task里；如果它启动了一个新的activity，不管新的activity的launch mode 如何，新的activity都将会到别的task里运行（如同加了FLAG_ACTIVITY_NEW_TASK参数）。

而另外三种模式，则可以和其它activity共存。

4. 是否每次都生成新实例

“standard”对于没一个启动Intent都会生成一个activity的新实例；

“singleTop”的activity如果在task的栈顶的话，则不生成新的该activity的实例，直接使用栈顶的实例，否则，生成该activity的实例。

比如现在task栈元素为A-B-C-D（D在栈顶），这时候给D发一个启动intent，如果D是 “standard”的，则生成D的一个新实例，栈变为A－B－C－D－D。

如果D是singleTop的话，则不会生产D的新实例，栈状态仍为A-B-C-D

如果这时候给B发Intent的话，不管B的launchmode是”standard” 还是 “singleTop” ，都会生成B的新实例，栈状态变为A-B-C-D-B。

“singleInstance”是其所在栈的唯一activity，它会每次都被重用。

“singleTask”如果在栈顶，则接受intent，否则，该intent会被丢弃，但是该task仍会回到前台。

当已经存在的activity实例处理新的intent时候，会调用onNewIntent()方法 如果收到intent生成一个activity实例，那么用户可以通过back键回到上一个状态；如果是已经存在的一个activity来处理这个intent的话，用户不能通过按back键返回到这之前的状态。
```

### 25. 跟activity和Task 有关的 Intent启动方式有哪些？其含义

```t
核心的Intent Flag有：

FLAG_ACTIVITY_NEW_TASK

FLAG_ACTIVITY_CLEAR_TOP

FLAG_ACTIVITY_RESET_TASK_IF_NEEDED

FLAG_ACTIVITY_SINGLE_TOP

FLAG_ACTIVITY_NEW_TASK

  如果设置，这个Activity会成为历史stack中一个新Task的开始。一个Task（从启动它的Activity到下一个Task中的 Activity）定义了用户可以迁移的Activity原子组。Task可以移动到前台和后台；在某个特定Task中的所有Activity总是保持相同的次序。

  这个标志一般用于呈现“启动”类型的行为：它们提供用户一系列可以单独完成的事情，与启动它们的Activity完全无关。

使用这个标志，如果正在启动的Activity的Task已经在运行的话，那么，新的Activity将不会启动；代替的，当前Task会简单的移入前台。参考FLAG_ACTIVITY_MULTIPLE_TASK标志，可以禁用这一行为。

  这个标志不能用于调用方对已经启动的Activity请求结果。

FLAG_ACTIVITY_CLEAR_TOP

  如果设置，并且这个Activity已经在当前的Task中运行，因此，不再是重新启动一个这个Activity的实例，而是在这个Activity上方的所有Activity都将关闭，然后这个Intent会作为一个新的Intent投递到老的Activity（现在位于顶端）中。

  例如，假设一个Task中包含这些Activity：A，B，C，D。如果D调用了startActivity()，并且包含一个指向Activity B的Intent，那么，C和D都将结束，然后B接收到这个Intent，因此，目前stack的状况是：A，B。

  上例中正在运行的Activity B既可以在onNewIntent()中接收到这个新的Intent，也可以把自己关闭然后重新启动来接收这个Intent。如果它的启动模式声明为 “multiple”(默认值)，并且你没有在这个Intent中设置FLAG_ACTIVITY_SINGLE_TOP标志，那么它将关闭然后重新创建；对于其它的启动模式，或者在这个Intent中设置FLAG_ACTIVITY_SINGLE_TOP标志，都将把这个Intent投递到当前这个实例的onNewIntent()中。

  这个启动模式还可以与FLAG_ACTIVITY_NEW_TASK结合起来使用：用于启动一个Task中的根Activity，它会把那个Task中任何运行的实例带入前台，然后清除它直到根Activity。这非常有用，例如，当从Notification Manager处启动一个Activity。

FLAG_ACTIVITY_RESET_TASK_IF_NEEDED

    如果设置这个标志，这个activity不管是从一个新的栈启动还是从已有栈推到栈顶，它都将以the front door of the task的方式启动。这就讲导致任何与应用相关的栈都讲重置到正常状态（不管是正在讲activity移入还是移除），如果需要，或者直接重置该栈为初始状态。

FLAG_ACTIVITY_SINGLE_TOP

  如果设置，当这个Activity位于历史stack的顶端运行时，不再启动一个新的

FLAG_ACTIVITY_BROUGHT_TO_FRONT

  这个标志一般不是由程序代码设置的，如在launchMode中设置singleTask模式时系统帮你设定。

FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET

  如果设置，这将在Task的Activity stack中设置一个还原点，当Task恢复时，需要清理Activity。也就是说，下一次Task带着 FLAG_ACTIVITY_RESET_TASK_IF_NEEDED标记进入前台时（典型的操作是用户在主画面重启它），这个Activity和它之上的都将关闭，以至于用户不能再返回到它们，但是可以回到之前的Activity。

  这在你的程序有分割点的时候很有用。例如，一个e-mail应用程序可能有一个操作是查看一个附件，需要启动图片浏览Activity来显示。这个 Activity应该作为e-mail应用程序Task的一部分，因为这是用户在这个Task中触发的操作。然而，当用户离开这个Task，然后从主画面选择e-mail app，我们可能希望回到查看的会话中，但不是查看图片附件，因为这让人困惑。通过在启动图片浏览时设定这个标志，浏览及其它启动的Activity在下次用户返回到mail程序时都将全部清除。

FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS

  如果设置，新的Activity不会在最近启动的Activity的列表中保存。

FLAG_ACTIVITY_FORWARD_RESULT

  如果设置，并且这个Intent用于从一个存在的Activity启动一个新的Activity，那么，这个作为答复目标的Activity将会传到这个新的Activity中。这种方式下，新的Activity可以调用setResult(int)，并且这个结果值将发送给那个作为答复目标的 Activity。

FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY

  这个标志一般不由应用程序代码设置，如果这个Activity是从历史记录里启动的（常按HOME键），那么，系统会帮你设定。

FLAG_ACTIVITY_MULTIPLE_TASK

  不要使用这个标志，除非你自己实现了应用程序启动器。与FLAG_ACTIVITY_NEW_TASK结合起来使用，可以禁用把已存的Task送入前台的行为。当设置时，新的Task总是会启动来处理Intent，而不管这是是否已经有一个Task可以处理相同的事情。

  由于默认的系统不包含图形Task管理功能，因此，你不应该使用这个标志，除非你提供给用户一种方式可以返回到已经启动的Task。

  如果FLAG_ACTIVITY_NEW_TASK标志没有设置，这个标志被忽略。

FLAG_ACTIVITY_NO_ANIMATION

  如果在Intent中设置，并传递给Context.startActivity()的话，这个标志将阻止系统进入下一个Activity时应用 Acitivity迁移动画。这并不意味着动画将永不运行——如果另一个Activity在启动显示之前，没有指定这个标志，那么，动画将被应用。这个标志可以很好的用于执行一连串的操作，而动画被看作是更高一级的事件的驱动。

FLAG_ACTIVITY_NO_HISTORY

  如果设置，新的Activity将不再历史stack中保留。用户一离开它，这个Activity就关闭了。这也可以通过设置noHistory特性。

FLAG_ACTIVITY_NO_USER_ACTION

  如果设置，作为新启动的Activity进入前台时，这个标志将在Activity暂停之前阻止从最前方的Activity回调的onUserLeaveHint()。

  典型的，一个Activity可以依赖这个回调指明显式的用户动作引起的Activity移出后台。这个回调在Activity的生命周期中标记一个合适的点，并关闭一些Notification。

  如果一个Activity通过非用户驱动的事件，如来电或闹钟，启动的，这个标志也应该传递给Context.startActivity，保证暂停的Activity不认为用户已经知晓其Notification。

FLAG_ACTIVITY_PREVIOUS_IS_TOP

  If set and this intent is being used to launch a new activity from an existing one, the current activity will not be counted as the top activity for deciding whether the new intent should be delivered to the top instead of starting a new one. The previous activity will be used as the top, with the assumption being that the current activity will finish itself immediately.

FLAG_ACTIVITY_REORDER_TO_FRONT

  如果在Intent中设置，并传递给Context.startActivity()，这个标志将引发已经运行的Activity移动到历史stack的顶端。

  例如，假设一个Task由四个Activity组成：A,B,C,D。如果D调用startActivity()来启动Activity B，那么，B会移动到历史stack的顶端，现在的次序变成A,C,D,B。如果FLAG_ACTIVITY_CLEAR_TOP标志也设置的话，那么这个标志将被忽略。

```

### 26. 请描述下Activity的生命周期

```t
答：activity的生命周期方法有：onCreate()、onStart()、onReStart()、onResume()、onPause()、onStop()、onDestory()；

可见生命周期：从onStart()直到系统调用onStop()

前台生命周期：从onResume()直到系统调用onPause()
```

### 27. activity在屏幕旋转时的生命周期

```t
答：不设置Activity的android:configChanges时，切屏会重新调用各个生命周期，切横屏时会执行一次，切竖屏时会执行两次；设置Activity的android:configChanges="orientation"时，切屏还是会重新调用各个生命周期，切横、竖屏时只会执行一次；设置Activity的android:configChanges="orientation|keyboardHidden"时，切屏不会重新调用各个生命周期，只会执行onConfigurationChanged方法
```

### 28. 如何启用Service，如何停用Service

```t
服务的开发比较简单，如下：

第一步：继承Service类

1

public class SMSService extends Service {}

第二步：在AndroidManifest.xml文件中的<application>节点里对服务进行配置:<service android:name=".SMSService" />

服务不能自己运行，需要通过调用Context.startService()或Context.bindService()方法启动服务。这两个方法都可以启动Service，但是它们的使用场合有所不同。使用startService()方法启用服务，调用者与服务之间没有关连，即使调用者退出了，服务仍然运行。使用bindService()方法启用服务，调用者与服务绑定在了一起，调用者一旦退出，服务也就终止，大有“不求同时生，必须同时死”的特点。

如果打算采用Context.startService()方法启动服务，在服务未被创建时，系统会先调用服务的onCreate()方法，接着调用onStart()方法。如果调用startService()方法前服务已经被创建，多次调用startService()方法并不会导致多次创建服务，但会导致多次调用onStart()方法。采用startService()方法启动的服务，只能调用Context.stopService()方法结束服务，服务结束时会调用onDestroy()方法。

如果打算采用Context.bindService()方法启动服务，在服务未被创建时，系统会先调用服务的onCreate()方法，接着调用onBind()方法。这个时候调用者和服务绑定在一起，调用者退出了，系统就会先调用服务的onUnbind()方法，接着调用onDestroy()方法。如果调用bindService()方法前服务已经被绑定，多次调用bindService()方法并不会导致多次创建服务及绑定(也就是说onCreate()和onBind()方法并不会被多次调用)。如果调用者希望与正在绑定的服务解除绑定，可以调用unbindService()方法，调用该方法也会导致系统调用服务的onUnbind()-->onDestroy()方法。

服务常用生命周期回调方法如下：

onCreate() 该方法在服务被创建时调用，该方法只会被调用一次，无论调用多少次startService()或bindService()方法，服务也只被创建一次。

onDestroy()该方法在服务被终止时调用。

与采用Context.startService()方法启动服务有关的生命周期方法

onStart() 只有采用Context.startService()方法启动服务时才会回调该方法。该方法在服务开始运行时被调用。多次调用startService()方法尽管不会多次创建服务，但onStart() 方法会被多次调用。

与采用Context.bindService()方法启动服务有关的生命周期方法

onBind()只有采用Context.bindService()方法启动服务时才会回调该方法。该方法在调用者与服务绑定时被调用，当调用者与服务已经绑定，多次调用Context.bindService()方法并不会导致该方法被多次调用。

onUnbind()只有采用Context.bindService()方法启动服务时才会回调该方法。该方法在调用者与服务解除绑定时被调用
```

### 29. 注册广播有几种方式，这些方式有何优缺点？请谈谈Android引入广播机制的用意

```t
答：首先写一个类要继承BroadcastReceiver
```

* 第一种:在清单文件中声明,添加

```java
<receive android:name=".IncomingSMSReceiver " >

<intent-filter>

<action android:name="android.provider.Telephony.SMS_RECEIVED")

<intent-filter>

<receiver>
```

* 第二种使用代码进行注册如:

```java
IntentFilter filter =  new IntentFilter("android.provider.Telephony.SMS_RECEIVED");

IncomingSMSReceiver receiver = new IncomgSMSReceiver();

registerReceiver(receiver.filter);
```

```t
两种注册类型的区别是：

1)第一种不是常驻型广播，也就是说广播跟随程序的生命周期。

2)第二种是常驻型，也就是说当应用程序关闭后，如果有信息广播来，程序也会被系统调用自动运行。

```

### 30. 请解释下在单线程模型中Message、Handler、Message Queue、Looper之间的关系

```t
答：简单的说，Handler获取当前线程中的looper对象，looper用来从存放Message的MessageQueue中取出Message，再有Handler进行Message的分发和处理.
```

``Message Queue(消息队列)``：用来存放通过Handler发布的消息，通常附属于某一个创建它的线程，可以通过Looper.myQueue()得到当前线程的消息队列

``Handler``：可以发布或者处理一个消息或者操作一个Runnable，通过Handler发布消息，消息将只会发送到与它关联的消息队列，然也只能处理该消息队列中的消息

``Looper``：是Handler和消息队列之间通讯桥梁，程序组件首先通过Handler把消息传递给Looper，Looper把消息放入队列。Looper也把消息队列里的消息广播给所有的

``Handler``：Handler接受到消息后调用handleMessage进行处理

``Message``：消息的类型，在Handler类中的handleMessage方法中得到单个的消息进行处理

```t
在单线程模型下，为了线程通信问题，Android设计了一个Message Queue(消息队列)， 线程间可以通过该Message Queue并结合Handler和Looper组件进行信息交换。下面将对它们进行分别介绍：
```

1. Message

    Message消息，理解为线程间交流的信息，处理数据后台线程需要更新UI，则发送Message内含一些数据给UI线程。

2. Handler

    Handler处理者，是Message的主要处理者，负责Message的发送，Message内容的执行处理。后台线程就是通过传进来的 Handler对象引用来sendMessage(Message)。而使用Handler，需要implement 该类的 handleMessage(Message)方法，它是处理这些Message的操作内容，例如Update UI。通常需要子类化Handler来实现handleMessage方法。

3. Message Queue

    Message Queue消息队列，用来存放通过Handler发布的消息，按照先进先出执行。

    每个message queue都会有一个对应的Handler。Handler会向message queue通过两种方法发送消息：sendMessage或post。这两种消息都会插在message queue队尾并按先进先出执行。但通过这两种方法发送的消息执行的方式略有不同：通过sendMessage发送的是一个message对象,会被 Handler的handleMessage()函数处理；而通过post方法发送的是一个runnable对象，则会自己执行。

4. Looper

    Looper是每条线程里的Message Queue的管家。Android没有Global的Message Queue，而Android会自动替主线程(UI线程)建立Message Queue，但在子线程里并没有建立Message Queue。所以调用Looper.getMainLooper()得到的主线程的Looper不为NULL，但调用Looper.myLooper() 得到当前线程的Looper就有可能为NULL。对于子线程使用Looper，API Doc提供了正确的使用方法：这个Message机制的大概流程：

     1. 在Looper.loop()方法运行开始后，循环地按照接收顺序取出Message Queue里面的非NULL的Message。

     2. 一开始Message Queue里面的Message都是NULL的。当Handler.sendMessage(Message)到Message Queue，该函数里面设置了那个Message对象的target属性是当前的Handler对象。随后Looper取出了那个Message，则调用 该Message的target指向的Hander的dispatchMessage函数对Message进行处理。在dispatchMessage方法里，如何处理Message则由用户指定，三个判断，优先级从高到低：

     1) Message里面的Callback，一个实现了Runnable接口的对象，其中run函数做处理工作；

     2) Handler里面的mCallback指向的一个实现了Callback接口的对象，由其handleMessage进行处理；

     3) 处理消息Handler对象对应的类继承并实现了其中handleMessage函数，通过这个实现的handleMessage函数处理消息。

      由此可见，我们实现的handleMessage方法是优先级最低的！
     3. Handler处理完该Message (update UI) 后，Looper则设置该Message为NULL，以便回收！

    在网上有很多文章讲述主线程和其他子线程如何交互，传送信息，最终谁来执行处理信息之类的，个人理解是最简单的方法——判断Handler对象里面的Looper对象是属于哪条线程的，则由该线程来执行！

    1. 当Handler对象的构造函数的参数为空，则为当前所在线程的Looper；

    2. Looper.getMainLooper()得到的是主线程的Looper对象，Looper.myLooper()得到的是当前线程的Looper对象。

### 31. 简要解释一下activity、 intent 、intent filter、service、Broadcase、BroadcaseReceiver

```t
答：一个activity呈现了一个用户可以操作的可视化用户界面；一个service不包含可见的用户界面，而是在后台运行，可以与一个activity绑定，通过绑定暴露出来接口并与其进行通信；一个broadcast receiver是一个接收广播消息并做出回应的component，broadcast receiver没有界面；一个intent是一个Intent对象，它保存了消息的内容。对于activity和service来说，它指定了请求的操作名称和待操作数据的URI，Intent对象可以显式的指定一个目标component。如果这样的话，android会找到这个component(基于manifest文件中的声明)并激活它。但如果一个目标不是显式指定的，android必须找到响应intent的最佳component。它是通过将Intent对象和目标的intent filter相比较来完成这一工作的；一个component的intent filter告诉android该component能处理的intent。intent filter也是在manifest文件中声明的。
```

### 32. 说说mvc模式的原理，它在android中的运用,android的官方建议应用程序的开发采用mvc模式。何谓mvc

```t
mvc是model,view,controller的缩写，mvc包含三个部分：

模型（model）对象：是应用程序的主体部分，所有的业务逻辑都应该写在该层。

视图（view）对象：是应用程序中负责生成用户界面的部分。也是在整个mvc架构中用户唯一可以看到的一层，接收用户的输入，显示处理结果。

控制器（control）对象：是根据用户的输入，控制用户界面数据显示及更新model对象状态的部分，控制器更重要的一种导航功能，响应用户出发的相关事件，交给m层处理。

android鼓励弱耦合和组件的重用，在android中mvc的具体体现如下：

1)视图层（view）：一般采用xml文件进行界面的描述，使用的时候可以非常方便的引入，当然，如果你对android了解的比较的多了话，就一定可以想到在android中也可以使用JavaScript+html等的方式作为view层，当然这里需要进行java和javascript之间的通信，幸运的是，android提供了它们之间非常方便的通信实现。

2)控制层（controller）：android的控制层的重任通常落在了众多的acitvity的肩上，这句话也就暗含了不要在acitivity中写代码，要通过activity交割model业务逻辑层处理，这样做的另外一个原因是android中的acitivity的响应时间是5s，如果耗时的操作放在这里，程序就很容易被回收掉。

3)模型层（model）：对数据库的操作、对网络等的操作都应该在model里面处理，当然对业务计算等操作也是必须放在的该层的。
```

### 33. 什么是ANR 如何避免它

```t
答：ANR：Application Not Responding。在Android中，活动管理器和窗口管理器这两个系统服务负责监视应用程序的响应，当用户操作的在5s内应用程序没能做出反应，BroadcastReceiver在10秒内没有执行完毕，就会出现应用程序无响应对话框，这既是ANR。

避免方法：Activity应该在它的关键生命周期方法（如onCreate()和onResume()）里尽可能少的去做创建操作。潜在的耗时操作，例如网络或数据库操作，或者高耗时的计算如改变位图尺寸，应该在子线程里（或者异步方式）来完成。主线程应该为子线程提供一个Handler，以便完成时能够提交给主线程。
```

### 34. 什么情况会导致Force Close ？如何避免？能否捕获导致其的异常

```t
答：程序出现异常，比如nullpointer。

避免：编写程序时逻辑连贯，思维缜密。能捕获异常，在logcat中能看到异常信息
```

### 35. 描述一下android的系统架构

```t
android系统架构分从下往上为linux 内核层、运行库、应用程序框架层、和应用程序层。

linuxkernel：负责硬件的驱动程序、网络、电源、系统安全以及内存管理等功能。

libraries和 android runtime：libraries：即c/c++函数库部分，大多数都是开放源代码的函数库，例如webkit（引擎），该函数库负责 android网页浏览器的运行，例如标准的c函数库libc、openssl、sqlite等，当然也包括支持游戏开发2dsgl和 3dopengles，在多媒体方面有mediaframework框架来支持各种影音和图形文件的播放与显示，例如mpeg4、h.264、mp3、 aac、amr、jpg和png等众多的多媒体文件格式。android的runtime负责解释和执行生成的dalvik格式的字节码。

applicationframework（应用软件架构），java应用程序开发人员主要是使用该层封装好的api进行快速开发。

applications:该层是java的应用程序层，android内置的googlemaps、e-mail、即时通信工具、浏览器、mp3播放器等处于该层，java开发人员开发的程序也处于该层，而且和内置的应用程序具有平等的位置，可以调用内置的应用程序，也可以替换内置的应用程序。

上面的四个层次，下层为上层服务，上层需要下层的支持，调用下层的服务，这种严格分层的方式带来的极大的稳定性、灵活性和可扩展性，使得不同层的开发人员可以按照规范专心特定层的开发。

android应用程序使用框架的api并在框架下运行，这就带来了程序开发的高度一致性，另一方面也告诉我们，要想写出优质高效的程序就必须对整个 applicationframework进行非常深入的理解。精通applicationframework，你就可以真正的理解android的设计和运行机制，也就更能够驾驭整个应用层的开发。
```

### 36. 请介绍下ContentProvider是如何实现数据共享的

```t
一个程序可以通过实现一个Content provider的抽象接口将自己的数据完全暴露出去，而且Content providers是以类似数据库中表的方式将数据暴露。Content providers存储和检索数据，通过它可以让所有的应用程序访问到，这也是应用程序之间唯一共享数据的方法。

要想使应用程序的数据公开化，可通过2种方法：创建一个属于你自己的Content provider或者将你的数据添加到一个已经存在的Content provider中，前提是有相同数据类型并且有写入Content provider的权限。

如何通过一套标准及统一的接口获取其他应用程序暴露的数据？

Android提供了ContentResolver，外界的程序可以通过ContentResolver接口访问ContentProvider提供的数据。
```

### 37. Service和Thread的区别

```t
答：servie是系统的组件，它由系统进程托管（servicemanager）；它们之间的通信类似于client和server，是一种轻量级的ipc通信，这种通信的载体是binder，它是在linux层交换信息的一种ipc。而thread是由本应用程序托管。
1). Thread：Thread 是程序执行的最小单元，它是分配CPU的基本单位。可以用 Thread 来执行一些异步的操作。

2). Service：Service 是android的一种机制，当它运行的时候如果是Local Service，那么对应的 Service 是运行在主进程的 main 线程上的。如：onCreate，onStart 这些函数在被系统调用的时候都是在主进程的 main 线程上运行的。如果是Remote Service，那么对应的 Service 则是运行在独立进程的 main 线程上。

既然这样，那么我们为什么要用 Service 呢？其实这跟 android 的系统机制有关，我们先拿 Thread 来说。Thread 的运行是独立于 Activity 的，也就是说当一个 Activity 被 finish 之后，如果你没有主动停止 Thread 或者 Thread 里的 run 方法没有执行完毕的话，Thread 也会一直执行。因此这里会出现一个问题：当 Activity 被 finish 之后，你不再持有该 Thread 的引用。另一方面，你没有办法在不同的 Activity 中对同一 Thread 进行控制。

举个例子：如果你的 Thread 需要不停地隔一段时间就要连接服务器做某种同步的话，该 Thread 需要在 Activity 没有start的时候也在运行。这个时候当你 start 一个 Activity 就没有办法在该 Activity 里面控制之前创建的 Thread。因此你便需要创建并启动一个 Service ，在 Service 里面创建、运行并控制该 Thread，这样便解决了该问题（因为任何 Activity 都可以控制同一 Service，而系统也只会创建一个对应 Service 的实例）。

因此你可以把 Service 想象成一种消息服务，而你可以在任何有 Context 的地方调用 Context.startService、Context.stopService、Context.bindService，Context.unbindService，来控制它，你也可以在 Service 里注册 BroadcastReceiver，在其他地方通过发送 broadcast 来控制它，当然这些都是 Thread 做不到的。
```

### 38. Android本身的api并未声明会抛出异常，则其在运行时有无可能抛出runtime异常，你遇到过吗？诺有的话会导致什么问题？如何解决

```t
答：会，比如nullpointerException。我遇到过，比如textview.setText()时，textview没有初始化。会导致程序无法正常运行出现forceclose。打开控制台查看logcat信息找出异常信息并修改程序。
```

### 39. IntentService有何优点

```t
答：Acitivity的进程，当处理Intent的时候，会产生一个对应的Service； Android的进程处理器现在会尽可能的不kill掉你；非常容易使用
```

### 40. 如果后台的Activity由于某原因被系统回收了，如何在被系统回收之前保存当前状态

```t
答：重写onSaveInstanceState()方法，在此方法中保存需要保存的数据，该方法将会在activity被回收之前调用。通过重写onRestoreInstanceState()方法可以从中提取保存好的数据
```

### 41. 如何将一个Activity设置成窗口的样式

答：activity标签中配置：

```java
android :theme="@android:style/Theme.Dialog"
```

另外

```java
android:theme="@android:style/Theme.Translucent"
```

是设置透明

### 42. 如何退出Activity？如何安全退出已调用多个Activity的Application

```t
答：对于单一Activity的应用来说，退出很简单，直接finish()即可。当然，也可以用killProcess()和System.exit()这样的方法。
```

对于多个activity，

* 1、记录打开的Activity：每打开一个Activity，就记录下来。在需要退出时，关闭每一个Activity即可。

* 2、发送特定广播：在需要结束应用时，发送一个特定的广播，每个Activity收到广播后，关闭即可。

* 3、递归退出：在打开新的Activity时使用startActivityForResult，然后自己加标志，在onActivityResult中处理，递归关闭。为了编程方便，最好定义一个Activity基类，处理这些共通问题。

```t
在2.1之前，可以使用ActivityManager的restartPackage方法。

它可以直接结束整个应用。在使用时需要权限android.permission.RESTART_PACKAGES。

注意不要被它的名字迷惑。

可是，在2.2，这个方法失效了。在2.2添加了一个新的方法，killBackground Processes()，需要权限 android.permission.KILL_BACKGROUND_PROCESSES。可惜的是，它和2.2的restartPackage一样，根本起不到应有的效果。

另外还有一个方法，就是系统自带的应用程序管理里，强制结束程序的方法，forceStopPackage()。它需要权限android.permission.FORCE_STOP_PACKAGES。并且需要添加android:sharedUserId="android.uid.system"属性。同样可惜的是，该方法是非公开的，他只能运行在系统进程，第三方程序无法调用。

因为需要在Android.mk中添加LOCAL_CERTIFICATE := platform。

而Android.mk是用于在Android源码下编译程序用的。

从以上可以看出，在2.2，没有办法直接结束一个应用，而只能用自己的办法间接办到。
```

现提供几个方法，供参考：

* 1、抛异常强制退出：

```t
该方法通过抛异常，使程序Force Close。

验证可以，但是，需要解决的问题是，如何使程序结束掉，而不弹出Force Close的窗口。
```

* 2、记录打开的Activity：

```t
每打开一个Activity，就记录下来。在需要退出时，关闭每一个Activity即可。
```

* 3、发送特定广播：

```t
在需要结束应用时，发送一个特定的广播，每个Activity收到广播后，关闭即可。
```

* 4、递归退出

```t
在打开新的Activity时使用startActivityForResult，然后自己加标志，在onActivityResult中处理，递归关闭。
```

```t
除了第一个，都是想办法把每一个Activity都结束掉，间接达到目的。但是这样做同样不完美。你会发现，如果自己的应用程序对每一个Activity都设置了nosensor，在两个Activity结束的间隙，sensor可能有效了。但至少，我们的目的达到了，而且没有影响用户使用。为了编程方便，最好定义一个Activity基类，处理这些共通问题。
```

### 43. AIDL的全称是什么？如何工作？能处理哪些类型的数据

答：全称是：``Android Interface Define Language``

```t
在Android中, 每个应用程序都可以有自己的进程. 在写UI应用的时候, 经常要用到Service. 在不同的进程中, 怎样传递对象呢?显然, Java中不允许跨进程内存共享. 因此传递对象, 只能把对象拆分成操作系统能理解的简单形式, 以达到跨界对象访问的目的. 在J2EE中,采用RMI的方式, 可以通过序列化传递对象. 在Android中, 则采用AIDL的方式. 理论上AIDL可以传递Bundle,实际上做起来却比较麻烦。

AIDL(AndRoid接口描述语言)是一种借口描述语言; 编译器可以通过aidl文件生成一段代码，通过预先定义的接口达到两个进程内部通信进程的目的. 如果需要在一个Activity中, 访问另一个Service中的某个对象, 需要先将对象转化成AIDL可识别的参数(可能是多个参数), 然后使用AIDL来传递这些参数, 在消息的接收端, 使用这些参数组装成自己需要的对象.

AIDL的IPC的机制和COM或CORBA类似, 是基于接口的，但它是轻量级的。它使用代理类在客户端和实现层间传递值. 如果要使用AIDL, 需要完成2件事情: 1. 引入AIDL的相关类.; 2. 调用aidl产生的class.
```

* AIDL的创建方法:

```t
AIDL语法很简单,可以用来声明一个带一个或多个方法的接口，也可以传递参数和返回值。 由于远程调用的需要, 这些参数和返回值并不是任何类型.下面是些AIDL支持的数据类型:
```

#### 1. 不需要import声明的简单Java编程语言类型(int,boolean等)

#### 2. String, CharSequence不需要特殊声明

#### 3. List, Map和Parcelables类型, 这些类型内所包含的数据成员也只能是简单数据类型, String等其他比支持的类型

(未尝试Parcelables, 在Eclipse+ADT下编译不过, 或许以后会有所支持)

### 44. 请解释下Android程序运行时权限与文件系统权限的区别

```t
答：运行时权限Dalvik( android授权)

文件系统 linux 内核授权
```

### 45. 系统上安装了多种浏览器，能否指定某浏览器访问指定页面？请说明原由

```t
通过直接发送Uri把参数带过去，或者通过manifest里的intentfilter里的data属性
```

### 46. android系统的优势和不足

答：Android平台手机 5大优势：

#### 一、开放性

```t
在优势方面，Android平台首先就是其开发性，开发的平台允许任何移动终端厂商加入到Android联盟中来。显著的开放性可以使其拥有更多的开发者，随着用户和应用的日益丰富，一个崭新的平台也将很快走向成熟。开放性对于Android的发展而言，有利于积累人气，这里的人气包括消费者和厂商，而对于消费者来讲，随大的受益正是丰富的软件资源。开放的平台也会带来更大竞争，如此一来，消费者将可以用更低的价位购得心仪的手机。
```

#### 二、挣脱运营商的束缚

```t
在过去很长的一段时间，特别是在欧美地区，手机应用往往受到运营商制约，使用什么功能接入什么网络，几乎都受到运营商的控制。从去年iPhone 上市 ，用户可以更加方便地连接网络，运营商的制约减少。随着EDGE、HSDPA这些2G至3G移动网络的逐步过渡和提升，手机随意接入网络已不是运营商口中的笑谈，当你可以通过手机IM软件方便地进行即时聊天时，再回想不久前天价的彩信和图铃下载业务，是不是像噩梦一样？互联网巨头Google推动的Android终端天生就有网络特色，将让用户离互联网更近。
```

#### 三、丰富的硬件选择

```t
这一点还是与Android平台的开放性相关，由于Android的开放性，众多的厂商会推出千奇百怪，功能特色各具的多种产品。功能上的差异和特色，却不会影响到数据同步、甚至软件的兼容，好比你从诺基亚 Symbian风格手机 一下改用苹果 iPhone ，同时还可将Symbian中优秀的软件带到iPhone上使用、联系人等资料更是可以方便地转移，是不是非常方便呢？
```

#### 四、不受任何限制的开发商

```t
Android平台提供给第三方开发商一个十分宽泛、自由的环境，不会受到各种条条框框的阻扰，可想而知，会有多少新颖别致的软件会诞生。但也有其两面性，血腥、暴力、情色方面的程序和游戏如可控制正是留给Android难题之一。
```

#### 五、无缝结合的Google应用

```t
如今叱诧互联网的Google已经走过10年度历史，从搜索巨人到全面的互联网渗透，Google服务如地图、邮件、搜索等已经成为连接用户和互联网的重要纽带，而Android平台手机将无缝结合这些优秀的Google服务。
```

再说Android的5大不足：

#### 一、安全和隐私

```t
由于手机 与互联网的紧密联系，个人隐私很难得到保守。除了上网过程中经意或不经意留下的个人足迹，Google这个巨人也时时站在你的身后，洞穿一切，因此，互联网的深入将会带来新一轮的隐私危机。
```

#### 二、首先开卖Android手机的不是最大运营商

```t
众所周知，T-Mobile在23日，于美国纽约发布 了Android首款手机G1。但是在北美市场，最大的两家运营商乃AT&T和Verizon，而目前所知取得Android手机销售权的仅有 T-Mobile和Sprint，其中T-Mobile的3G网络相对于其他三家也要逊色不少，因此，用户可以买账购买G1，能否体验到最佳的3G网络服务则要另当别论了！
```

#### 三、运营商仍然能够影响到Android手机

```t
在国内市场，不少用户对购得移动定制机不满，感觉所购的手机被人涂画了广告一般。这样的情况在国外市场同样出现。Android手机的另一发售运营商Sprint就将在其机型中内置其手机商店程序。
```

#### 四、同类机型用户减少

```t
在不少手机论坛都会有针对某一型号的子论坛，对一款手机的使用心得交流，并分享软件资源。而对于Android平台手机，由于厂商丰富，产品类型多样，这样使用同一款机型的用户越来越少，缺少统一机型的程序强化。举个稍显不当的例子，现在山寨机泛滥，品种各异，就很少有专门针对某个型号山寨机的讨论和群组，除了哪些功能异常抢眼、颇受追捧的机型以外。
```

#### 五、过分依赖开发商缺少标准配置

```t
在使用PC端的Windows Xp系统的时候，都会内置微软Windows Media Player这样一个浏览器程序，用户可以选择更多样的播放器，如Realplay或暴风影音等。但入手开始使用默认的程序同样可以应付多样的需要。在 Android平台中，由于其开放性，软件更多依赖第三方厂商，比如Android系统的SDK中就没有内置音乐 播放器，全部依赖第三方开发，缺少了产品的统一性。
```

### 47. Android dvm的进程和Linux的进程, 应用程序的进程是否为同一个概念

```t
答：DVM指dalivk的虚拟机。每一个Android应用程序都在它自己的进程中运行，都拥有一个独立的Dalvik虚拟机实例。而每一个DVM都是在Linux 中的一个进程，所以说可以认为是同一个概念。
```

### 48. sim卡的EF文件是什么？有何作用

```t
答：sim卡的文件系统有自己规范，主要是为了和手机通讯，sim本 身可以有自己的操作系统，EF就是作存储并和手机通讯用的
```

### 49. 嵌入式操作系统内存管理有哪几种， 各有何特性

```t
页式，段式，段页，用到了MMU,虚拟空间等技术
```

### 50. 什么是嵌入式实时操作系统, Android 操作系统属于实时操作系统吗

```t
嵌入式实时操作系统是指当外界事件或数据产生时，能够接受并以足够快的速度予以处理，其处理的结果又能在规定的时间之内来控制生产过程或对处理系统作出快速响应，并控制所有实时任务协调一致运行的嵌入式操作系统。主要用于工业控制、 军事设备、 航空航天等领域对系统的响应时间有苛刻的要求，这就需要使用实时系统。又可分为软实时和硬实时两种，而android是基于linux内核的，因此属于软实时。
```

### 51. 一条最长的短信息约占多少byte

```t
中文70(包括标点)，英文160，160个字节。
```

### 52. 如何将SQLite数据库(dictionary.db文件)与apk文件一起发布

```t
解答：可以将dictionary.db文件复制到Eclipse Android工程中的res aw目录中。所有在res aw目录中的文件不会被压缩，这样可以直接提取该目录中的文件。可以将dictionary.db文件复制到res aw目录中
```

### 53. 如何将打开res aw目录中的数据库文件

```t
解答：在Android中不能直接打开res aw目录中的数据库文件，而需要在程序第一次启动时将该文件复制到手机内存或SD卡的某个目录中，然后再打开该数据库文件。

复制的基本方法是使用getResources().openRawResource方法获得res aw目录中资源的 InputStream对象，然后将该InputStream对象中的数据写入其他的目录中相应文件中。在Android SDK中可以使用SQLiteDatabase.openOrCreateDatabase方法来打开任意目录中的SQLite数据库文件。
```

### 54. DDMS和TraceView的区别

```t
DDMS是一个程序执行查看器，在里面可以看见线程和堆栈等信息，TraceView是程序性能分析器 。
```

### 55. java中如何引用本地语言

`JNI（java native interface  java 本地接口）`接口 。

### 56. 谈谈Android的IPC（进程间通信）机制

```t
IPC是内部进程通信的简称， 是共享"命名管道"的资源。Android中的IPC机制是为了让Activity和Service之间可以随时的进行交互，故在Android中该机制，只适用于Activity和Service之间的通信，类似于远程方法调用，类似于C/S模式的访问。通过定义AIDL接口文件来定义IPC接口。Servier端实现IPC接口，Client端调用IPC接口本地代理。
```

### 40. NDK是什么

```t
NDK是一些列工具的集合，NDK提供了一系列的工具，帮助开发者迅速的开发C/C++的动态库，并能自动将so和java 应用打成apk包。

NDK集成了交叉编译器，并提供了相应的mk文件和隔离cpu、平台等的差异，开发人员只需简单的修改mk文件就可以创建出so
```
