# 内网穿透工具--FRP

## 简介

1、对于没有公网 IP 的内网用户来说，远程管理或在外网访问内网机器上的服务是一个问题。

2、今天给大家介绍一款好用内网穿透工具 FRP，FRP 全名：Fast Reverse Proxy。FRP 是一个使用 Go 语言开发的高性能的反向代理应用，可以帮助您轻松地进行内网穿透，对外网提供服务。FRP 支持 TCP、UDP、HTTP、HTTPS等协议类型，并且支持 Web 服务根据域名进行路由转发。

* 项目地址：[GitHub](https://github.com/fatedier/frp)

## FRP 的作用

* 利用处于内网或防火墙后的机器，对外网环境提供 HTTP 或 HTTPS 服务。

* 对于 HTTP, HTTPS 服务支持基于域名的虚拟主机，支持自定义域名绑定，使多个域名可以共用一个 80 端口。

* 利用处于内网或防火墙后的机器，对外网环境提供 TCP 和 UDP 服务，例如在家里通过 SSH 访问处于公司内网环境内的主机。

[未完](https://www.jianshu.com/p/00c79df1aaf0)
