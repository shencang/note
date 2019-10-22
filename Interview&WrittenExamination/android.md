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

### 四大组件是什么？
Activity【活动】：用于表现功能。

Service【服务】：后台运行服务，不提供界面呈现。

BroadcastReceiver【广播接收器】：用来接收广播。

Content Provider【内容提供商】：支持在多个应用中存储和读取数据，相当于数据库。

### 四个组件的生命周期？

Activity生命周期图及 Fragment生命周期图  

                                                                                                                                        
![Activity生命周期图](https://github.com/shencang/note/blob/master/Android/image/interview/activity_life.png)


![Fragment生命周期图](https://github.com/shencang/note/blob/master/Android/image/interview/fragment_life.png)


Service的生命周期：首先Service有两种启动方式，而在这两种启动方式下，它的生命周期不同。

通过startService()方法启动的服务

初始化结束后系统会调用 void onStart(Intent intent) 方法，用于处理传递给startService()的Intent对象。如音乐服务会打开Intent 来探明将要播放哪首音乐，并开始播放。注意：多次调用startService()方法会多次触发onStart()方法。

通过bindService ()方法启动的服务

 初始化结束后系统会调用 IBinder onBind(Intent intent) 方法，用来绑定传递给bindService 的Intent 的对象。注意：多次调用bindService()时，如果该服务已启动则不会再触发此方法。

### Handler【Android SDK提供给开发者方便进行异步消息处理的类】：
AsyncTask、retrofit都对Handler进行了封装。

#### （1）Handler四大组件

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

#### 异步消息处理流程：

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

###  fragment各种情况下的生命周期？
 由于Fragment的生命周期与Activity的生命周期有着牵扯，所以把两者的图放到一起作为对比理解。

 ![Fragment的生命周期与Activity的生命周期](https://github.com/shencang/note/blob/master/Android/image/interview/activity-fragment-life.png)

 接下来就不同情况下的Fragment生命周期做一简单介绍：

### Fragment在Activity中replace
新替换的Activity：onAttach() ---> onCreate() ---> onCreatView() ---> onViewCreated ---> onActivityCreated() ---> onStart --->onResume()

被替换的Activity：onPause() ---> onStop() ---> onDestoryView() ---> onDestory() ---> onDetach()

### Fragment在Activity中replace，并addToBackStack
新替换的Fragment（没有在BackStack中）：onAttach > onCreate > onCreateView > onViewCreated > onActivityCreated > onStart > onResume

新替换的Fragment（已经在BackStack中）：onCreateView > onViewCreated > onActivityCreated > onStart > onResume

被替换的Fragment：onPause > onStop > onDestroyView

### Fragment在ViewPager中切换
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

### Fragment进入了运行状态：
Fragment在进入运行状态时，以下四个生命周期会随它所属的Activity一起被调用：

onPause() ---> onStop() ---> onStart() ---> onResume()

关于Fragment的onActivityResult方法：
使用Fragment的startActivity方法时，FragmentActivity的onActivityResult方法会回调相应的Fragment的onActivityResult方法，所以在重写FragmentActivity的onActivityResult方法时，注意调用super.onActivityResult。




## 启动模式：

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

### 问题：onNewIntent()调用时机？

singleTop：如果新Activity已经位于任务栈的栈顶，就不会重新创建，并回调 onNewIntent(intent) 方法。

singleTask：只要该Activity在一个任务栈中存在，都不会重新创建，并回调 onNewIntent(intent) 方法。


### Activity的四种启动模式对比？

Standard:标准的启动模式，如果需要启动一个activity就会创建该activity的实例。也是activity的默认启动模式。

SingeTop:如果启动的activity已经位于栈顶，那么就不会重新创建一个新的activity实例。而是复用位于栈顶的activity实例对象。如果不位于栈顶仍旧会重新创建activity的实例对象。

SingleTask:设置了singleTask启动模式的activity在启动时，如果位于activity栈中，就会复用该activity，这样的话，在该实例之上的所有activity都依次进行出栈操作，即执行对应的onDestroy()方法，直到当前要启动的activity位于栈顶。一般应用在网页的图集，一键退出当前的应用程序。

singleInstance:如果使用singleInstance启动模式的activity在启动的时候会复用已经存在的activity实例。不管这个activity的实例是位于哪一个应用当中，都会共享已经启动的activity的实例对象。使用了singlestance的启动模式的activity会单独的开启一个共享栈，这个栈中只存在当前的activity实例对象。


## 网络协议：

协议：【协议指计算机通信网络中两台计算机之间进行通信所必须共同遵守的规定或规则】

### HTTP协议

#### 基本概念：

【超文本传输协议】允许将HTML（超文本标记语言）文档从Web服务器传送到客户端的浏览器。HTTP协议是基于TCP/IP通信协议来传输数据的，可以从服务器端获取图片等数据资源。

URI：【uniform resource identifier】统一的资源标识符，用来唯一的标识一个资源。强调资源！！！

#### 组成部分：

1）访问资源的命名机制；file

2）存放资源的主机名；

3）资源自身的名称，由路径表示，着重于强调资源。

例：file://a:1234/b/c/d.txt   表示资源目标在a主机下的1234端口的b目录下的c目录下的d.txt文件。

#### URL：

【uniform resource Location】统一资源定位器，是一种具体的URI。即URL可以用来标识一个资源，而且还指明了如何定位这个资源。强调路径！！！

#### 组成部分：

1）协议；

2）存有该资源的主机IP地址；

3）主机资源的具体地址。

#### HTTP协议特点：

1）简单快速；

2）无连接；【限制每次链接只处理一个请求，服务器处理完客户的请求之后会收到客户端的应答，再断开链接，节省了重复的时间】；

3）无状态：【没有记忆能力，】

HTTP协议的request/response请求头原理剖析：

request有可能经过代理服务器到达web服务器

代理服务器最主要的作用：提高访问速度【大部分代理服务器都具有缓存功能，当你再次访问前一个网络请求时，就可以直接从代理服务器中获取，而不需要请求我们的web服务器】。

#### HTTP协议容易混淆知识点：

##### （1）http1.0与http1.1的具体区别：

http处于计算机网络的应用层。

1）缓存处理

2）带宽优化及网络连接的使用

3）Host头使用：1.1上请求操作和响应操作都支持Host头，而且在请求消息中如果没有Host头的话会报告一个400错误。

4）长连接：在一个TCP连接上，可以传送多个HTTP请求和响应，而不是发送一个HTTP请求就断开一个连接，再发送一个HTTP请求再建立一个连接。

##### 存在的问题：

1）传输数据时，每次都需要重新创建连接，增加了大量的延迟时间；

2）传输数据时，所有传输的内容都是明文，客户端和服务器端都无法验证对方的身份；

3）使用时，header里携带的内容过大，增加了传输成本。

##### （2）get / post方法的区别：

1）提交的数据：get提交的数据一般会放在我们的URL之后，用“  ？”来分割；而post提交数据都会放在我们entity-body【消息主体】当中。

2）提交的数据大小是否有限制：get提交的数据是有限制的，因为url是有限制的，不能无限制的输入一个url地址；而post方法提交的是body，因此没有限制。

3）取得变量的值：get方法通过Request.QueryString()来取得变量的值，而post方法通过Request.Form来取得变量的值。

4）安全问题：get提交数据一定会带来安全问题

##### （3）Cookie和Session的区别：

###### 1）cookie【用户身份的标识】：

客户端的解决方案。是由服务器发给客户端的特殊信息，而这些信息以文本文件的方式存放在客户端，然后客户端每次向服务器发送请求的时候都会带上这些特殊的信息。存放在响应头里面。

客户端 向服务端发送一个HTTP Request请求；

服务端给客户端一个HTTP Response ，并且把它的cookies设置给我们的客户端；

客户端将HTTP Request和cookies打包给我们的服务端；

服务端会根据客户端给我们的cookies来进行指定的判断，返回HTTP Response给我们的客户端。

此方法弥补了我们HTTP协议无状态的不足。之前当上述请求响应操作完成后，服务端和客户端就断开连接，服务端就无法从连接上跟踪我们所想要的客户端。

###### 2）session：

另一种记录客户状态的限制，cookie保存在客户端浏览器中，而session保存在服务器上。客户端浏览器访问服务器时，服务器把客户端信息以某种形式记录在服务器上。

创建session；
在创建session同时，服务器会为该session生成唯一的session id；

在session被创建之后，就可以调用session相关的方法往session中增加内容；

当客户端再次发送请求的时候，会将这个session id带上，服务器接收到请求之后就会依据session id找到相应的session。

###### 3）区别：

存放的位置不同；

存取的方式不同【cookie保存的是Ascii码字符串，而session中能够保存任何类型的数据】；

安全性上的不同【cookie存放在客户端浏览器中，对我们客户端可见，客户端的一些程序就有可能去修改我们cookie的内容，而session则不然，它存储在服务端上，对客户端是透明的，不存在敏感信息泄露的风险】；

有效期上的不同【一般我们会设置cookie过期时间， session依赖 id，若id设置为-1，当关掉浏览器session就会失效】；对服务器的造成的压力不同【cookie保存在客户端不占用客户资源，session保存在服务端，每一个用户都会产生一个session。在并发很多用户时cookie是一个很好的选择】。

#### HTTPS协议：

基本概念：对工作在以加密连接（SSL / TLS）上的常规HTTP协议。通过在TCP和HTTP之间加入TLS【Transport Layer Security】来加密。

SSL / TLS协议：安全传输协议，TLS是SSL的升级版，也是现阶段所使用的协议；

##### HTTPS传输速度：

1）通信慢；

2）SSL必须进行加密处理。

##### TLS / SSL握手：

1）密码学原理

对称加密：加密数据所用的密钥和解密数据所用的密钥相同。

非对称加密：分私有密钥和公有密钥。

2）数字证书：互联网通讯中标志通讯各方身份信息的一串数字。

3）握手过程