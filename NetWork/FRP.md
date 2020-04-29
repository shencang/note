# 内网穿透工具--FRP

## 简介

1、对于没有公网 IP 的内网用户来说，远程管理或在外网访问内网机器上的服务是一个问题。

2、今天给大家介绍一款好用内网穿透工具 FRP，FRP 全名：Fast Reverse Proxy。FRP 是一个使用 Go 语言开发的高性能的反向代理应用，可以帮助您轻松地进行内网穿透，对外网提供服务。FRP 支持 TCP、UDP、HTTP、HTTPS等协议类型，并且支持 Web 服务根据域名进行路由转发。

* 项目地址：[GitHub](https://github.com/fatedier/frp)

### FRP 的作用

* 利用处于内网或防火墙后的机器，对外网环境提供 HTTP 或 HTTPS 服务。

* 对于 HTTP, HTTPS 服务支持基于域名的虚拟主机，支持自定义域名绑定，使多个域名可以共用一个 80 端口。

* 利用处于内网或防火墙后的机器，对外网环境提供 TCP 和 UDP 服务，例如在家里通过 SSH 访问处于公司内网环境内的主机。

### FRP的安装

* 下载：

```cmd

 wget https://github.com/fatedier/frp/releases/download/v0.30.0/frp_0.30.0_linux_amd64.tar.gz

```

* 解压并与移动指定目录：

```cmd
 tar xzvf frp_0.30.0_linux_amd64.tar.gz
 mv frp_0.30.0_linux_amd64 frp
```

* 看到该教程是可能不是不是最新版本或者是其他平台的设备，请访问[项目释放](https://github.com/fatedier/frp/releases)

### FRP 服务端配置

配置 FRP 服务端的前提条件是需要一台具有公网 IP 的设备，得益于 FRP 是 Go 语言开发的，具有良好的跨平台特性。你可以在 Windows、Linux、MacOS、ARM等几乎任何可联网设备上部署。

这里以 Linux 为例，FRP 默认给出两个服务端配置文件，一个是简版的 frps.ini，另一个是完整版本 frps_full.ini。
我们先来看看简版的 frps.ini，通过这个配置可以快速的搭建起一个 FRP 服务端。

```cmd

-> cat frps.ini

[common]
bind_port = 7000
默认配置中监听的是 7000 端口，可根据自己实际情况修改。

启动 FRP 服务端
$ ./frps -c ./frps.ini
2019/12/15 10:52:45 [I] [service.go:96] frps tcp listen on 0.0.0.0:7000
2019/12/15 10:52:45 [I] [main.go:112] Start frps success
2019/12/15 10:52:45 [I] [main.go:114] PrivilegeMode is enabled, you should pay more attention to security issues
```

通过上面简单的两步就可以成功启动一个监听在 7000 端口的 FRP 服务端。

![frp-1](https://i.loli.net/2019/12/11/GHubF6IJEvPBRk4.png)

### FRP 客户端配置

和 FRP 服务端类似，FRP 默认也给出两个客户端配置文件，一个是简版的 frpc.ini，另一个是完整版本 frpc_full.ini。
这里同样以简版的 frpc.ini 文件为例，假设 FRP 服务端所在服务器的公网 IP 为 4.3.2.1。

```cmd

-> vim frpc.ini

[common]
# server_addr 为 FRP 服务端的公网 IP
server_addr = 4.3.2.1
# server_port 为 FRP 服务端监听的端口
server_port = 7000
启动 FRP 客户端
$ ./frpc -c ./frpc.ini
2019/12/15 11:15:49 [I] [proxy_manager.go:284] proxy removed: []
2019/12/15 11:15:49 [I] [proxy_manager.go:294] proxy added: []
2019/12/15 11:15:49 [I] [proxy_manager.go:317] visitor removed: []
2019/12/15 11:15:49 [I] [proxy_manager.go:326] visitor added: []
2019/12/15 11:15:49 [I] [control.go:240] [83775d7388b8e7d9] login to server success, get run id [83775d7388b8e7d9], server udp port [0]
```

这样就可以成功在 FRP 服务端上成功建立一个客户端连接，当然现在还并不能对外提供任何内网机器上的服务，因为我们并还没有在 FRP 服务端注册任何内网服务的端口。

## FRP 使用实例

下面我们就来看几个常用的例子，通过这些例子来了解下 FRP 是如何实现内网服务穿透的。

### 通过 TCP 访问内网机器

```cmd
-> cat frpc.ini

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = 6000
启动 FRP 客户端
$ ./frpc -c ./frpc.ini
2019/12/15 12:21:23 [I] [proxy_manager.go:284] proxy removed: []
2019/12/15 12:21:23 [I] [proxy_manager.go:294] proxy added: [ssh]
2019/12/15 12:21:23 [I] [proxy_manager.go:317] visitor removed: []
2019/12/15 12:21:23 [I] [proxy_manager.go:326] visitor added: []
2019/12/15 12:21:23 [I] [control.go:240] [3b468a55191341cb] login to server success, get run id [3b468a55191341cb], server udp port [0]
2019/12/15 12:21:23 [I] [control.go:165] [3b468a55191341cb] [ssh] start proxy success
```

这样就在 FRP 服务端上成功注册了一个端口为 6000 的服务，接下来我们就可以通过这个端口访问内网机器上 SSH 服务，假设用户名为 mike：
`$ ssh -oPort=6000 mike@4.3.2.1`

### 通过自定义域名访问部署于内网的 Web 服务

有时需要在公有网络通过域名访问我们在本地环境搭建的 Web 服务，但是由于本地环境机器并没有公网 IP，无法将域名直接解析到本地的机器。
现在通过 FRP 就可以很容易实现这一功能，这里以 HTTP 服务为例：首先修改 FRP 服务端配置文件，通过 vhost_http_port 参数来设置 HTTP 访问端口，这里将 HTTP 访问端口设为 8080

```cmd
$ vim frps.ini
[common]
bind_port = 7000
vhost_http_port = 8080
启动 FRP 服务端
$ ./frps -c ./frps.ini
2019/12/15 13:33:26 [I] [service.go:96] frps tcp listen on 0.0.0.0:7000
2019/12/15 13:33:26 [I] [service.go:125] http service listen on 0.0.0.0:8080
2019/12/15 13:33:26 [I] [main.go:112] Start frps success
2019/12/15 13:33:26 [I] [main.go:114] PrivilegeMode is enabled, you should pay more attention to security issues
其次我们在修改 FRP 客户端配置文件并增加如下内容：
-> vim frpc.ini

[web]
type = http
local_port = 80
custom_domains = **.***.com
这里通过 local_port 和 custom_domains 参数来设置本地机器上 Web 服务对应的端口和自定义的域名，这里我们分别设置端口为 80，对应域名为 **.***.com。
启动 FRP 客户端
$ ./frpc -c ./frpc.ini
2019/12/15 13:56:11 [I] [proxy_manager.go:284] proxy removed: []
2019/12/15 13:56:11 [I] [proxy_manager.go:294] proxy added: [web ssh]
2019/12/15 13:56:11 [I] [proxy_manager.go:317] visitor removed: []
2019/12/15 13:56:11 [I] [proxy_manager.go:326] visitor added: []
2019/12/15 13:56:11 [I] [control.go:240] [296fe9e31a551e07] login to server success, get run id [296fe9e31a551e07], server udp port [0]
2019/12/15 13:56:11 [I] [control.go:165] [296fe9e31a551e07] [web] start proxy success
2019/12/15 13:56:11 [I] [control.go:165] [296fe9e31a551e07] [ssh] start proxy success
```

最后将 ..com 的域名 A 记录解析到 FRP 服务器的公网 IP 上，现在便可以通过 `http://.*.com:8080` 这个 URL 访问到处于内网机器上对应的 Web 服务。

```t
HTTPS 服务配置方法类似，只需将 vhost_http_port 替换为 vhost_https_port， type 设置为 https 即可。
```

### 通过密码保护你的 Web 服务

由于所有客户端共用一个 FRP 服务端的 HTTP 服务端口，任何知道你的域名和 URL 的人都能访问到你部署在内网的 Web 服务，但是在某些场景下需要确保只有限定的用户才能访问。
FRP 支持通过 HTTP Basic Auth 来保护你的 Web 服务，使用户需要通过用户名和密码才能访问到你的服务。需要实现此功能主要需要在 FRP 客户端的配置文件中添加用户名和密码的设置。

```cmd

-> vim frpc.ini

[web]
type = http
local_port = 80
custom_domains = **.***.com


## 设置认证的用户名


http_user = abc


## 设置认证的密码


http_pwd = abc

```

这时访问 `http://.*.com:8080` 这个 URL 时就需要输入配置的用户名和密码才能访问。
该功能目前仅限于 HTTP 类型的代理。

### 给 Web 服务增加自定义二级域名

在多人同时使用一个 FRP 服务端实现 Web 服务时，通过自定义二级域名的方式来使用会更加方便。
通过在 FRP 服务端的配置文件中配置 subdomain_host参数就可以启用该特性。之后在 FRP 客户端的 http、https 类型的代理中可以不配置 custom_domains，而是配置一个 subdomain 参数。
然后只需要将 *.{subdomain_host} 解析到 FRP 服务端所在服务器。之后用户可以通过 subdomain 自行指定自己的 Web 服务所需要使用的二级域名，并通过 {subdomain}.{subdomain_host} 来访问自己的 Web 服务。
首先我们在 FRP 服务端配置 subdomain_host 参数：

```cmd
$ vim frps.ini
[common]
subdomain_host = ***.com
其次在 FRP 客户端配置文件配置 subdomain 参数：
$ vim frpc.ini
[web]
type = http
local_port = 80
subdomain = test
```

然后将泛域名 .com 解析到 FRP 服务端所在服务器的公网 IP 地址。FRP 服务端 和 FRP 客户端都启动成功后，通过 test.**.com 就可以访问到内网的 Web 服务。

同一个 HTTP 或 HTTPS 类型的代理中 custom_domains 和 subdomain 可以同时配置。

需要注意的是如果 FPR 服务端配置了 subdomain_host，则 custom_domains 中不能是属于 subdomain_host 的子域名或者泛域名。

### 修改 Host Header

通常情况下 FRP 不会修改转发的任何数据。但有一些后端服务会根据 HTTP 请求 header 中的 host 字段来展现不同的网站，例如 Nginx 的虚拟主机服务，启用 host-header 的修改功能可以动态修改 HTTP 请求中的 host 字段。
实现此功能只需要在 FRP 客户端配置文件中定义 host_header_rewrite 参数。

```cmd
$ vim frpc.ini
[web]
type = http
local_port = 80
custom_domains = test.***.com
host_header_rewrite = dev.***.com
原来 HTTP 请求中的 host 字段 test.***.com 转发到后端服务时会被替换为 dev.***.com。
```

该功能仅限于 HTTP 类型的代理。

[未完](https://www.jianshu.com/p/00c79df1aaf0)
