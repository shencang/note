# django+nginx+uwSGI云服务器部署教程
##### ~~经历7次重装服务器的血与泪的总结~~
* Django的安装以及环境配置可以通过[Django入门与实践](https://www.imooc.com/video/13928)来学习。

* [Django入门指南](https://docs.djangoproject.com/en/2.1/)

* 本次教程重点参考：[Django实践以及服务器部署](https://github.com/wangyufei1006/Study-Notes/blob/master/Web/Django%E5%AE%9E%E8%B7%B5%E4%BB%A5%E5%8F%8A%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%83%A8%E7%BD%B2.md?tdsourcetag=s_pctim_aiomsg)

----
## **准备**
首先是**环境**，
#### 系统
我的服务器环境是CentOS 7.4 ，uUbuntu配置方式类似。
主要yum命令与apr-get的区别。因为使用了uwSGI,在目前的今天（2019.6.28)windows下仍然无法使用该插件。虽然有极难的方式使其支持，但是不建议尝试。
#### 数据库
数据库可用的很多，包括自带的sqlLite或者自行安装Mysql等等。这里只说MySQL。

#### Django与python
但是请注意，**在Django 2.1版本时正式放弃支持MySQL 5.6及以下版本的支持。** 原因是新的ORM的语句已经无法支持。
其次是Python版本，**使用MySql请使用python3.5以上版本**。其下不支持。


本次使用centOS7.4+Mysql5.7+django2.2+python3.6.3完成（作死边缘疯狂试探）

----
Django常用指令和示例项目编写参考[Django实践以及服务器部署](https://github.com/wangyufei1006/Study-Notes/blob/master/Web/Django%E5%AE%9E%E8%B7%B5%E4%BB%A5%E5%8F%8A%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%83%A8%E7%BD%B2.md?tdsourcetag=s_pctim_aiomsg)
建议数据库和Django学习到一定程度再往下走。

补充常用CentOs（linux）指令：

    新文件夹 mkdir

    查看端口 lsof -i tcp:80

    列出端口 netstat -ntlp

    文件改名 mv a  b

    启动uwsgi：uwsgi --ini /root/sites/shencangblue.com/XingZhi_web/uwsgi.ini --daemonize /tmp/uwsgi.log

    查找 locate 
    
    

## 使用nginx+uwSGI部署Django项目

* 满足条件
  * 可以通过外网访问的服务器
  * 域名(当然没有域名也可以，直接通过IP进行访问)

#### 搭建服务器

* 本教程使用的本地环境是Windows10（64位-1903），服务器环境为CentOS 7.4（64位）。

#### 安装软件

* 新的服务器的用户是root，我们需要新建一个拥有超级权限的新用户。

  [可选步骤]
  ```
  #在root下创建一个新用户，user是用户名
  root@localhost:~# useradd -m -s /bin/bash user
  
  #把新创建的用户加入到超级权限组
  root@localhost:~# usermod -a -G sudo user
  
  #为新用户设置密码
  root@localhost:~# passwd user
  
  #切换到新用户
  root@localhost:~# su - user
  
  #切换成功，注意到root已经变为user了
  user@localhost:~$
  ```
  [可选步骤]
* 如果是新服务器的话，需要更新一下系统。

  ```
  user@localhost:~$ sudo apt-get update
  user@localhost:~$ sudo apt-get upgrade
  ```
 * 安装软件，用到的软件有`Nginx`、`uwSGI`、`Git`、`pip`、`Django`、`virtualenv`和`Anaconda`。

  ```
  #安装Anaconda，找到最新的Anaconda版本https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
  
  #下载
  uesr@localhost:~$ wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-5.0.1-Linux-x86_64.sh
  
  #安装
  uesr@localhost:~$ bash Anaconda3-5.0.1-Linux-x86_64.sh
  
  #Linux里面默认的是python2.7，我们需要切换到python3.6
  #=原装环境请不要随意修改！yum指令依赖2.7，动手能力强的可以手动重置yum的依赖定位实现全局高python版本
  uesr@localhost:~$ echo 'export PATH="/home/hqy/anaconda2/bin:$PATH"' >> ~/.bashrc
  uesr@localhost:~$ source ~/.bashrc
  
  #检查一下，看是否是python3.6
  uesr@localhost:~$ python --version
  
  #安装Nginx
  uesr@localhost:~$ sudo yum install nginx
  
  #安装uwSGI
  uesr@localhost:~$ sudo yum install uwsgi
  
  #安装git
  uesr@localhost:~$ sudo yum install git
  
  #安装pip
  uesr@localhost:~$ sudo yum install python3-pip
  
  #安装virtualenv
  uesr@localhost:~$ sudo pip install virtualenv(可能需要更新pip,使用命令更新)
  
  #安装Django
  sudo pip install django
  ```
#### 解析域名

* 将域名和服务器的IP地址绑定后，可以通过域名访问服务器。

#### 启动Nginx服务

* Nginx是用来处理静态文件请求的，比如说访问一个博客文章的页面时，服务器会收到两种请求：

  * 显示文章的详细信息，这些信息保存在数据库中
  * 图片、CSS、js等存在服务器某个文件夹下的静态文件。

* 前面我们已经安装了Nginx，并且域名已经和IP地址绑定了，运行下面的命令启动Nginx服务：

  ```
  user@localhost:~$ sudo service nginx start(这里需要注意一下，服务器需要开放80端口，外网才能进行访问)
  ```
    
  在浏览器输入域名，看到页面说明Nginx启动成功了。
  记住这指令，后面用的比较多
    
## 部署代码
#### 以下借用[Django实践以及服务器部署](https://github.com/wangyufei1006/Study-Notes/blob/master/Web/Django%E5%AE%9E%E8%B7%B5%E4%BB%A5%E5%8F%8A%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%83%A8%E7%BD%B2.md?tdsourcetag=s_pctim_aiomsg)]的部分代码

#### 部署前的配置

* Django项目中会有一些CSS、JS等静态文件，这个目录通常位于根目录下，命名为static，需要在项目的`settings.py`里做一些配置。

  ```
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR,'static)#指明静态文件的收集目录
  ```

  为了安全起见，在生产环境下关闭`DEBUG`选项以及设置允许访问的域名。

  ```
  DEBUG = False
  ALLOWED_HOSTS = ['127.0.0.1','localhost']
  用[*]可以使得可以接入任意的ip
  ```

  `ALLOWED_HOSTS`是允许访问的域名列表，前两个是本地域名，最后一个是服务器IP地址。

  项目还会依赖一些第三方python库，为了在服务器上安装，我们需要将全部依赖写入`requirements.txt`文件中激活本地的虚拟环境，进入项目的根目录，运行`pip freeze >requirements.txt`命令。

  ```
  E:\Painting>
  pip freeze > requirements.txt
  ```

  这时项目的根目录下会生成一个requirement.txt的文本文件，里面是项目的所有依赖。

#### 将代码上传到Github

* 这里对于大多数人来说已经很熟悉了。

  ```
  git add .
  git commit -m "blog"
  git push origin master
  ```
  推荐使用vs或者python提供的工具，可以实现轻松的版本管理
  
#### 设置服务器目录结构
  
  运行下面的命令：

  ```
  wangyuyfei@localhost:~$ mkdir -p ~/sites/39.105.110.19
  ```

  创建虚拟环境，进入到`39.105.110.19`目录下，运行`virtualenv`命令创建虚拟环境：

  ```
  wangyuyfei@localhost:~$ cd ~/sites/39.105.110.19
  wangyuyfei@localhost:~/sites/39.105.110.19$ virtualenv --python=python3 env
  ```

  检查一下虚拟环境是否创建成功，运行`ls`命令查看，看到`env	`这个文件夹说明虚拟环境创建成功。

  ```
  wangyuyfei@localhost:~/sites/39.105.110.19$ ls
  env
  ```

  接着从代码仓库把项目拉取下来，`git clone`后面的地址换成自己项目的仓库地址。

  ```
  wangyuyfei@localhost:~/sites/39.105.110.19$ git clone https://github.com/wangyufei1006/Painting.git
  ```

  运行`ls`命令检查是否拉取成功。

  ```
  wangyuyfei@localhost:~/sites/39.105.110.19$ ls
  AICopyBook env
  ```
#### 安装项目依赖

* 激活虚拟环境，再进入到项目根目录，安装项目的全部依赖：

  ```
  wangyuyfei@localhost:~/sites/39.105.110.19$ source env/bin/activate
  (env) wangyuyfei@localhost:~/sites/39.105.110.19$ cd Painting/
  (env) wangyuyfei@localhost:~/sites/39.105.110.19/Painting$ pip install -r requirements.txt 
  ```
  安装会遇到这个问题因为缺失mysql_config文件无法安装`mysqlclient`的问题
  我的该部分文档记述了问题如何解决：
  [CentOS](https://github.com/shencang/note/tree/master/Server/CentOS)
  如果还有`certifi`因为无法完整卸载而导致无法安装新的版本的问题
  请修改pip的版本为9.0.1即可安装。会弹警告。
  
  
  

#### 收集静态文件

* 虚拟环境下继续运行`python manage.py collectstatic`命令收集静态文件到static目录下：

  ```
  (env) wangyuyfei@localhost:~/sites/39.105.110.19/Painting$ python manage.py collectstatic
  ```

#### 生成数据库
* 执行这一步前请完成mysql用户的创建，并创建数据库，并授予权限。
可参考 [CentOS](https://github.com/shencang/note/tree/master/Server/CentOS)中的数据库部分
之后修改项目的目录下的settings.py文件的
```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xingzhi',
        'USER': 'root',
        'PASSWORD': '111111',
        'HOST': '',
        'PORT': '',
    }
}

```

* 虚拟环境下运行`python manage.py migrate`命令创建数据库文件：

  ```
  (env) wangyuyfei@localhost:~/sites/39.105.110.19/Painting$ python manage.py migrate
  ```

#### 创建超级用户

* 虚拟环境下运行`python manage.py createsuperuser`命令创建一个超级用户，方便进入Django管理 后台。

  ```
  (env) wangyuyfei@localhost:~/sites/39.105.110.19/Painting$ python manage.py createsuperuser
  ```
## 配置Nginx&Uwsgi

* 配置uwsgi

配置uwsgi：uwsgi可支持命令行启动、json格式配置文件启动、ini格式配置文件启动、xml配置文件启动

命令行启动：可以使用uwsgi --help查看启动选项
ini配置文件启动：

```
uwsgi：uwsgi --ini /root/sites/shencangblue.com/XingZhi_web/uwsgi.ini --daemonize /tmp/uwsgi.log
```

常用配置参数

```
http ： #协议类型和端口号

processes ： #开启的进程数量

workers ： #开启的进程数量，等同于processes（官网的说法是spawn the specified number ofworkers / processes）

chdir ： #指定运行目录（chdir to specified directory before apps loading）

wsgi-file ： #载入wsgi-file（load .wsgi file）

stats ： #在指定的地址上，开启状态服务（enable the stats server on the specified address）

threads ： #运行线程。由于GIL的存在，我觉得这个真心没啥用。（run each worker in prethreaded mode with the specified number of threads）

master ： #允许主进程存在（enable master process）

daemonize ： #使进程在后台运行，并将日志打到指定的日志文件或者udp服务器（daemonize uWSGI）。实际上最常用的，还是把运行记录输出到一个本地文件上。

pidfile ： #指定pid文件的位置，记录主进程的pid号。

vacuum ： #当服务器退出的时候自动清理环境，删除unix socket文件和pid文件（try to remove all of the generated file/sockets）

log-maxsize ：#记录日志配置最大多少，超过这个数会切割，单位kb
logto ：#指定输出日志到文件logto = /tmp/uwsgi.log
```
在django项目中与manage.py同级目录创建配置文件，这里命名为uwsgi.ini

~~这个地方翻了很多次车。~~
```
socket = 127.0.0.1:9001
chdir = /root/download/Android_Zigbee_Django/mydjango
module = mydjango.wsgi:application
#wsgi-file = /root/download/Android_Zigbee_Django/mydjango/mydjango/wsgi.py
master = true
vhost = true
no-stie = true
workers = 2
reload-mercy = 10
vacuum = true
max-requests = 1000
limit-as = 512
buffer-sizi = 30000
pidfile = /var/run/uwsgi.pid
daemonize = /var/log/uwsgi.log
```
```
ModuleNotFoundError: No module named 'django'
unable to load app 0 (mountpoint='') (callable not found or import error)
```
错误是由home指定的环境问题造成或者没有定位项目造成的
前者可以通过在uwsgi.ini文件中进行修改，指定虚拟环境home即可
```
home = /root/.virtualenvs/env_xadmin
```


启动uwsgi服务：

```
uwsgi：uwsgi --ini /root/sites/shencangblue.com/XingZhi_web/uwsgi.ini --daemonize /tmp/uwsgi.log
```
也可以指定（四选一即可）：virtualenv、venv、 home、 pyhome

* 配置nginx

**上面引用的教程中使用的nginx是老版本，文件位置变动已经较大。
如果使用的是1.12.1及以上版本，请按照我的位置定位文件。**
nginx主要位置是代理转发作用

nginx.conf 位于/etc/nginx/nginx.conf

```
#information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    #include /etc/nginx/conf.d/*.conf;

    server {
        listen       80 default_server;
        #listen       [::]:80 default_server;
        server_name  _;
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        # include /etc/nginx/default.d/*.conf;

        location / {
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    default_type        application/octet-stream;
        }
    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    #include /etc/nginx/conf.d/*.conf;

    server {
        listen       80;
        #listen       [::]:80 default_server;
        server_name  shencangblue.com;
        #root         /usr/share/nginx/html;
        charset      utf-8;
        error_log    logs/xingzhi.log;
        client_max_body_size 75M;
        # Load configuration files for the default server block.
        #include /etc/nginx/default.d/*.conf;

        location / {
         include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
        uwsgi_read_timeout 5;
        }
        location /static {
        expires 30d;
        autoindex on; 
        add_header Cache-Control private;
        alias /root/sites/shencangblue.com/XingZhi_web/static;
     }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

# Settings for a TLS enabled server.
#
#    server {
#        listen       443 ssl http2 default_server;
#        listen       [::]:443 ssl http2 default_server;
#        server_name  _;
#        root         /usr/share/nginx/html;
#
#        ssl_certificate "/etc/pki/nginx/server.crt";
#        ssl_certificate_key "/etc/pki/nginx/private/server.key";
#        ssl_session_cache shared:SSL:1m;
#        ssl_session_timeout  10m;
#        ssl_ciphers HIGH:!aNULL:!MD5;
#        ssl_prefer_server_ciphers on;
#
#        # Load configuration files for the default server block.
#        include /etc/nginx/default.d/*.conf;
#
#        location / {
#        }
#
#        error_page 404 /404.html;
#            location = /40x.html {
#        }
#
#        error_page 500 502 503 504 /50x.html;
#            location = /50x.html {
#        }
#    }

}

```
主要注释对应的行，否则只会显示默认的页面
**注意！注意！注意！**原来nginx.conf配置有两行必须注释掉。（这就是我一直搞不好的原因。。。）
```
	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
```

验证nginx.conf配置是否正确
```
nginx -t
```
启动nginx，访问项目url若出现Exception Value: Invalid HTTP_HOST header异常 ，需要在settings.py中ALLOWED_HOSTS = ['*']

* [可选]

####  **[重启脚本centos6.x]**
```
#!/bin/bash
if [ ! -n "$1" ]
then
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "uwsgi" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        uwsgi /xxx/www/uwsgi.ini --daemonize /var/log/uwsgi.log --post-buffering 32768 --buffer-size 32768
        echo "Start uwsgi service [OK]"
    fi


elif [ $1 = stop ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    killall -9 uwsgi
    uwsgi --ini /xxx/www/uwsgi.ini --daemonize /var/log/uwsgi.log  --post-buffering 32768 --buffer-size 32768 --touch-reload "/xxx/www/reload.set"
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
fi
```