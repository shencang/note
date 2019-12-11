# 内网穿透工具--FRP

## 简介

1、对于没有公网 IP 的内网用户来说，远程管理或在外网访问内网机器上的服务是一个问题。

2、今天给大家介绍一款好用内网穿透工具 FRP，FRP 全名：Fast Reverse Proxy。FRP 是一个使用 Go 语言开发的高性能的反向代理应用，可以帮助您轻松地进行内网穿透，对外网提供服务。FRP 支持 TCP、UDP、HTTP、HTTPS等协议类型，并且支持 Web 服务根据域名进行路由转发。

* 项目地址：[GitHub](https://github.com/fatedier/frp)

## FRP 的作用

* 利用处于内网或防火墙后的机器，对外网环境提供 HTTP 或 HTTPS 服务。

* 对于 HTTP, HTTPS 服务支持基于域名的虚拟主机，支持自定义域名绑定，使多个域名可以共用一个 80 端口。

* 利用处于内网或防火墙后的机器，对外网环境提供 TCP 和 UDP 服务，例如在家里通过 SSH 访问处于公司内网环境内的主机。

## FRP的安装

* 下载：

```cmd

 wget https://github.com/fatedier/frp/releases/download/v0.30.0/frp_0.30.0_linux_amd64.tar.gz

```

* 解压并与移动指定目录：

```cmd
 tar xzvf frp_0.30.0_linux_amd64.tar.gz
 mv frp_0.30.0_linux_amd64 frp
```

[未完](https://www.jianshu.com/p/00c79df1aaf0)

* 看到该教程是可能不是不是最新版本或者是其他平台的设备，请访问[项目释放](https://github.com/fatedier/frp/releases)

## FRP 服务端配置

配置 FRP 服务端的前提条件是需要一台具有**公网 IP **的设备，得益于 FRP 是 Go 语言开发的，具有良好的跨平台特性。你可以在 Windows、Linux、MacOS、ARM等几乎任何可联网设备上部署。

这里以 Linux 为例，FRP 默认给出两个服务端配置文件，一个是简版的 frps.ini，另一个是完整版本 frps_full.ini。
我们先来看看简版的 frps.ini，通过这个配置可以快速的搭建起一个 FRP 服务端。

```cmd

cat frps.ini

[common]
bind_port = 7000
默认配置中监听的是 7000 端口，可根据自己实际情况修改。

启动 FRP 服务端
$ ./frps -c ./frps.ini
2018/01/25 10:52:45 [I] [service.go:96] frps tcp listen on 0.0.0.0:7000
2018/01/25 10:52:45 [I] [main.go:112] Start frps success
2018/01/25 10:52:45 [I] [main.go:114] PrivilegeMode is enabled, you should pay more attention to security issues
```

通过上面简单的两步就可以成功启动一个监听在 7000 端口的 FRP 服务端。

![frp-1](https://i.loli.net/2019/12/11/GHubF6IJEvPBRk4.png)
