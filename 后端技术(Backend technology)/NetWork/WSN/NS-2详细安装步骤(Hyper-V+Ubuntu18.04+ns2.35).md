# NS-2详细安装步骤

## 安装信息

### 虚拟机信息

* Hyper-V
* Ubuntu 18.04 （x64)

### NS-2

* ns-allinone-2.35

## 安装步骤

### 虚拟机安装

VMware或者Hyper-V自行安装，Hyper-v自带在线获取镜像，VMware需要安装镜像，无论哪种，获取下载之后，安装并初始化。这里不赘述。

#### Hyper-v

![Hyper-v-start](https://i.loli.net/2019/11/28/s8XDGleN6rokHub.png)

#### VMware

![VMware-start](https://i.loli.net/2019/11/28/W1cQotKyLzaBr3g.png)

### 环境工具

先运行：

```cmd
sudo apt-get update #更新源列表
sudo apt-get upgrade #更新已经安装的包
sudo apt-get dist-upgrade #更新软件，升级系统
```

![ub-up](https://i.loli.net/2019/11/28/amrDlp8GzBxtioy.png)

确认无误之后，执行：

```cmd
sudo apt-get install build-essential  #编译器gcc make
sudo apt-get install tcl8.4 tcl8.4-dev tk8.4 tk8.4-dev  #tcl、tk库文件
sudo apt-get install libxmu-dev libxmu-headers   #与nam有关的库文件
```

如果运行遇到找不到tcl8.4与tk8.4等问题，去掉8.4版本号或者改为8.6即可，即：

```cmd
sudo apt-get install tcl tcl-dev tk tk-dev  #tcl、tk库文件
```

### 软件下载

* 我制作了下载的分流-[下载](http://data.shencangblue.com/index.php/s/c8E2LHjZW7K5Plz)

想要自己找的强迫症看这里：

* NS-2[官网](http://www.isi.edu/nsnam/ns/ns-build.html)在页面中找到

找到 allinone：

![allinone](https://i.loli.net/2019/11/28/KzJ4cjO3XtxbIqm.png)

你肯定留意到了windows的支持文字描述，但是很遗憾，后面的说明文档已经ERROR 500了，放弃吧.

点击跳转，到下载源码的地方，选择Download source: current release 2.35

![Download source](https://i.loli.net/2019/11/28/a8psEuGzbJDf62B.png)

### 软件安装

#### 路径确定

下载好源码之后，将其放到Ubuntu系统下的自己喜欢的地方，准备解压(图示是我保存的位置)

![filepath1](https://i.loli.net/2019/11/28/QaSd5fmEt278DJO.png)

![filepath2](https://i.loli.net/2019/11/28/5p7LsioDvZhAnGd.png)

（此处左边的文件夹是我已经解压的目录）

#### 解压与编译

使用Ubuntu自带图形化解压或者在压缩包目录使用命令：

```cmd
 tar -xzvf ns-allinone-2.35.tar.gz
```

之后运行命令：

```cmd
./install
```

开始编译：
![install](https://i.loli.net/2019/11/28/N6ViTBj7hmWCS1M.png)

运行之后如果成功的话类似于下图

![sec](https://i.loli.net/2019/11/28/2eWMAjwPhTNoCLg.png)

### 编译问题解决

#### mdart/dart_abp.o 报错

* 错误描述
![e1](https://i.loli.net/2019/11/28/xjZ8BiQ7bh3gJpW.png)

* 解决
 Ubuntu18.4的gcc为7.4版本，需要降低版本到gcc 5.4

先确认自己的gcc版本

```cmd
gcc -v
```

如果是7.x.x之类的版本。选择安装gcc5

```cmd
ls /usr/bin/gcc*
```

如果结果只有：/usr/bin/gcc  /usr/bin/gcc-7两种目录，那么我们需要安装gcc5

```cmd
sudo apt-get install gcc-5 gcc-5-multilib g++-5 g++-5-multilib
```

安装好后输入以下指令：

```cmd
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 40

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 50
```

接着输入：

```cmd
sudo update-alternatives --config gcc
```

会看到如下的选项，有 3 个候选项可用于替换 gcc (提供 /usr/bin/gcc)。

格式：

```cmd
选择 路径 优先级 状态
------------------------------------------------------------
* 0 /usr/bin/gcc-5 50 自动模式
1 /usr/bin/gcc-5 50 手动模式
2 /usr/bin/gcc-7 40 手动模式
```

要维持当前值[*]请按回车键，或者键入选择的编号：
要想用ns2要用gcc5。
同样也要设置一下g++的

```cmd
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 50

sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 40 #这个没用

```

如果想删除可选项的话可以键入以下指令：

```cmd
sudo update-alternatives --remove gcc /usr/bin/gcc-5
```

下面是查看g++版本可切换的

```cmd
sudo update-alternatives --config g++
```

注意：gcc和g++的版本在同时切换到相同版本，比如：gcc7、g++7，切换到gcc5、g++5，才能编译成功。

完成之后重新编译，编译出同样问题就再次检查gcc，再次编译。

#### linkstates/ls.o 报错

* 错误描述：
![ls](https://i.loli.net/2019/11/28/YpRDf5y3kx6WVIr.png)

* 解决

修改ls文件，具体的位置ns-allinone-2.35下搜索ls.h，把该文件打开后里面的第137行

```c++
 void eraseAll() {
      erase(baseMap::begin(), baseMap::end());
       } 改为： void eraseAll() {
            this->erase(baseMap::begin(), baseMap::end());
            }
```

  也就是把erase用this->erase替换掉就好了 。进行
 完后，再一次进行安装。

#### make: *** [tk3d.o] 错误

安装libx11-dev可以解决问题

```cmd
sudo apt-get install libx11-dev
```

#### .can't find X includes otcl-1.14 configuration failed

安装libXt-dev可以解决问题

```cmd
sudo apt-get install libXt-dev
```

## 环境变量配置

找到你的用户名下的主目录，/home/xxx，xxx是你的安装时的账户名，例如我的是jiyue。

```cmd
cd /home/jiyue
```

创建配置文件：

```cmd
sudo gedit .bashrc
```

(注意有个点在bashrc前面,如果前面这个命令不行的话 输入命令：gedit ~/.bashrc)

在文档的最后面加上以下环境变量:

```cmd
export PATH=$PATH:/home/jiyue/ns2/ns-allinone-2.35/bin:/home/jiyue/ns2/ns-allinone-2.35/tcl8.5.10/unix:/home/jiyue/ns2/ns-allinone-2.35/tk8.5.10/unix
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home//jiyue/ns2/ns-allinone-2.35/otcl-1.14:/home/jiyue/ns2/ns-allinone-2.35/lib
export TCL_LIBRARY=$TCL_LIBRARY:/home//jiyue/ns2/ns-allinone-2.35/tcl8.5.10/library

```

保存会有警告，先无视。

完成后记得保存并退出。重启终端。输入ns,出现%,说明ns2安装成功

![finish](https://i.loli.net/2019/11/28/2kb5r74ONx3sZqe.png)

注意：环境变量配错的话，会提示“程序“ns2”尚未安装，让你执行一个安装命令。 此时请勿使用命令安装！

注意：环境变量配错的话，会提示“程序“ns2”尚未安装，让你执行一个安装命令。 此时请勿使用命令安装！

注意：环境变量配错的话，会提示“程序“ns2”尚未安装，让你执行一个安装命令。 此时请勿使用命令安装！

如果反复确认没问题但还是不行，测试以下环境变量格式：

```cmd
PATH="$PATH:/home/jiyue/ns2/ns-allinone-2.35/bin:/home/jiyue/ns2/ns-allinone-2.35/tcl8.5.10/unix:/home/jiyue/ns2/ns-allinone-2.35/tk8.5.10/unix"
LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home//jiyue/ns2/ns-allinone-2.35/otcl-1.14:/home/jiyue/ns2/ns-allinone-2.35/lib"
TCL_LIBRARY="$TCL_LIBRARY:/home//jiyue/ns2/ns-allinone-2.35/tcl8.5.10/library"

```

到这里，ns-2全面安装成功。
