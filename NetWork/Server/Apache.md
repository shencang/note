# Apache

## linux 下 apache启动、停止、重启命令

* 基本的操作方法：
本文假设apahce安装目录为/usr/local/apache2，这些方法适合任何情况,如果配置了全局变量，直接使用指令即可，去除前缀。

* apahce启动命令：

```cmd
/usr/local/apache2/bin/apachectl start
```

* apache停止命令

```cmd
/usr/local/apache2/bin/apachectl stop
```

* apache重新启动命令：

```cmd
/usr/local/apache2/bin/apachectl restart
```

* 要在重启 Apache 服务器时不中断当前的连接，则应运行：

```cmd
/usr/local/sbin/apachectl graceful
```

* 如果apache安装成为linux的服务的话，可以用以下命令操作：

```cmd
service httpd start 启动

service httpd restart 重新启动

service httpd stop 停止服务

```

### Linux系统为Ubuntu

#### 一、Start Apache 2 Server /启动apache服务

```cmd
# /etc/init.d/apache2 start
```

* or

```cmd
sudo /etc/init.d/apache2 start
```

#### 二、 Restart Apache 2 Server /重启apache服务

```cmd
# /etc/init.d/apache2 restart
```

* or

```cmd
sudo /etc/init.d/apache2 restart
```

#### 三、Stop Apache 2 Server /停止apache服务

```cmd
# /etc/init.d/apache2 stop
```

* or

```cmd
sudo /etc/init.d/apache2 stop
```

[参考](https://www.cnblogs.com/piwefei/p/5996772.html)
