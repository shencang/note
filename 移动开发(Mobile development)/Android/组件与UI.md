# 组件与UI

## banner - 横幅

[android-banner项目的使用](https://www.jianshu.com/p/b3d3858b1e59)

[android的轮播图Banner之本地加载和网络加载图片](https://blog.csdn.net/life_s/article/details/80610770)

## 悬浮窗

[Android-悬浮窗效果FloatingView](https://www.jianshu.com/p/579f25ae002b)

[Android 悬浮窗全系统版本实现](https://blog.csdn.net/zhuchenglin830/article/details/81812747)

## 单元测试

[Android单元测试只看这一篇就够了](https://www.jianshu.com/p/aa51a3e007e2)

[Android单元测试-常见的方案比较](https://www.jianshu.com/p/925191464389)

## 更新

[android 检测新版本，下载更新功能](https://www.jianshu.com/p/8eaffd56becf)

## 支持库

### Android Support v4\v7\v13和AndroidX理解

    为什么要用support库呢？
    
    因为在低版本Android平台上开发一个APP时，想使用高版本才有的功能，此时就需要使用Support来支持兼容。

#### 1. android-support-v4

    compile "com.android.support:support-v4
    
    2011年4月份，谷歌推出最低兼容到1.6版本系统的包。
    
    eclipse新建工程时，都默认包含了，里面有类似Fragment，NotificationCompat，LoadBroadcastManager，ViewPager，PageTabAtrip，Loader，FileProvider  等等控件。
    
    V4包含了V7和V13的基础功能。

#### 2. android-support-v7

    compile "com.android.support:appcompat-v7:xx.xx"
    
    2014年 I/O大会时推出，最低兼容Android2.1系统。
    
    最新的v7包增加了很多material design的兼容类和素材，其中涉及的内容有Theme、value、布局、新的控件、新的动画实现方式，包含了support-v4的全部内容。
    
    android studio在创建工程的时候默认导入了v7工程，并且将style使用了兼容style。

#### 3. android-support-v13

    为平板开发推出的版本兼容包，最低兼容Android3.2的系统。可以说Android 3.x系统都是平板专用系统。

#### 4. androidX

     从android9.0 (API28)开始, support库将会进行改动, V7: 28.0.0将会是support库的终结版本。未来新的特性和改进都会进入Androidx包。其主要原因是support库的命名已经越来越令人迷惑 ，包越来越臃肿。
    
    依赖包的变化从：api 'com.android.support:appcompat-v7:28.0.0'
    
    变成了：api 'androidx.appcompat:appcompat:1.0.0'
    
    需要注意的是，build.gradle中的插件版本要在3.2.0以上才可以。
    
    如果项目中包含的第3方包中引用了support包，而又想使用androidX，则可以进行如下配置：
    
    android.useAndroidX=true
    
    android.enableJetifier=false
    
    Android Studio就提供了sopport转androix的能力；需要先在gradle.properties 文件中加入配置：
    
    android.useAndroidX=true
    
    android.enableJetifier=true

### assert（断言，非资源那个）

    在android中看到这个关键字，你的第一反应应该是操作资源文件用的，但是据我今天的了解并非如此，这个在android中还有另一个作用就是用来调试的，名字叫断言。

    顾名思义是：ASSERT()是一个调试程序时经常使用的宏，在程序运行时它计算括号内的表达式，如果表达式为FALSE (0), 程序将报告错误，并终止执行。如果表达式不为0，则继续执行后面的语句。这个宏通常原来判断程序中是否出现了明显非法的数据，如果出现了终止程序以免导致严重后果，同时也便于查找错误。

[原断言assert()与调试帮助](https://blog.csdn.net/enterprise_/article/details/82111501)

[Android系统自带下载DownloadManager使用方法完美实现](https://blog.csdn.net/qq_29428215/article/details/80570034)

[Android 5.0、6.0、7.0、8.0、9.0 新特性，DownloadManager踩坑记](https://blog.csdn.net/csdn_aiyang/article/details/85780925)

## Android UI

[Android--UI之ScrollView](https://www.cnblogs.com/plokmju/p/android_ScrollView.html)

[Android 解决TableRow中TextView或Edittext超出屏幕，不能自动换行或换行问题](https://blog.csdn.net/fan7983377/article/details/52054333)

[EditText限制只能输入整数](https://blog.csdn.net/a872822645/article/details/51741975)

[EditText设置只能输入整数金额](https://blog.csdn.net/youjia29/article/details/78271365)

## ADB

[玩转ADB命令（ADB命令使用大全）](https://blog.csdn.net/zhonglunshun/article/details/78362439)

Android 调试桥 (adb) 是一种功能多样的命令行工具，可让您与设备进行通信。adb 命令便于执行各种设备操作（例如安装和调试应用），并提供对 Unix shell（可用来在设备上运行各种命令）的访问权限。它是一种客户端-服务器程序，包括以下三个组件：

- 客户端：用于发送命令。客户端在开发计算机上运行。您可以通过发出 adb 命令从命令行终端调用客户端。

- 守护进程 (adbd)：在设备上运行命令。守护进程在每个设备上作为后台进程运行。

- 服务器：管理客户端和守护进程之间的通信。服务器在开发计算机上作为后台进程运行。

adb 包含在 Android SDK 平台工具软件包中。您可以使用 SDK 管理器下载此软件包，管理器会将此软件包安装在 android_sdk/platform-tools/。或者，如果您需要独立的 Android SDK 平台工具软件包，可以点击此处进行下载。

要了解如何连接设备以进行 adb 通信，包括如何使用 Connection Assistant 对常见问题进行排查，请参阅在硬件设备上运行应用。

adb 的工作原理

当您启动某个 adb 客户端时，客户端会先检查是否有 adb 服务器进程正在运行。如果没有，它将启动服务器进程。服务器在启动后会与本地 TCP 端口 5037 绑定，并监听 adb 客户端发出的命令 - 所有 adb 客户端均通过端口 5037 与 adb 服务器通信。

然后，服务器会与所有正在运行的设备建立连接。它通过扫描 5555 到 5585 之间（该范围供前 16 个模拟器使用）的奇数号端口查找模拟器。服务器一旦发现 adb 守护进程 (adbd)，便会与相应的端口建立连接。请注意，每个模拟器都使用一对按顺序排列的端口 - 用于控制台连接的偶数号端口和用于 adb 连接的奇数号端口。例如：

    模拟器 1，控制台：5554

    模拟器 1，adb：5555

    模拟器 2，控制台：5556

    模拟器 2，adb：5557

    依此类推… 
如上所示，在端口 5555 处与 adb 连接的模拟器与控制台监听端口为 5554 的模拟器是同一个。

服务器与所有设备均建立连接后，您便可以使用 adb 命令访问这些设备。由于服务器管理与设备的连接，并处理来自多个 adb 客户端的命令，因此您可以从任意客户端（或从某个脚本）控制任意设备。

[ADB官方详细介绍与使用](https://developer.android.google.cn/studio/command-line/adb)
