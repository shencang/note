
# docker常用命令

## 一、帮助命令

```text
    1.docker版本信息：docker version
```

功能：查看docker版本相关信息

```text
    2.docker详细信息： docker info
```

功能：查看docker的详细信息

```text
    3.docker命令指南：docker --help
```

功能：可以查看docker命令的使用方法

## 二、镜像命令

### 1.本地镜像信息查询：`docker images`

功能：查看docker中包含的镜像信息

执行结果：

```shell
[root@localhost ~]# docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
docker.io/mysql                        latest              be0dbf01a0f3        2 weeks ago         541 MB
docker.io/longhronshens/mycat-docker   latest              f9a4ece7c742        2 years ago         793 MB
选项说明： 1.Repository：表示镜像的仓库源 2.TAG：镜像的标签，同一个仓库源可以有多个TAG，代表不同的版本 3.IMAGE ID：镜像id 4.CREATED：镜像创建时间 5.SIZE：镜像大小
```

```text
1.docker images -a
```

功能：列出本地所有镜像（包含中间层）

执行结果：

```shell

[root@localhost ~]# docker images -a
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
docker.io/mysql                        latest              be0dbf01a0f3        2 weeks ago         541 MB
docker.io/longhronshens/mycat-docker   latest              f9a4ece7c742        2 years ago         793 MB
```

```text
2.docker images -q
```

功能：只显示镜像id

执行结果：

```shell
[root@localhost ~]# docker images -q
be0dbf01a0f3
f9a4ece7c742
```

```text
3.docker images -qa
```

功能：只显示所有镜像id（包含中间层）

执行结果：

```shell
[root@localhost ~]# docker images -q
be0dbf01a0f3
f9a4ece7c742
```

```text
4.docker images --digests
```

功能：显示镜像的摘要（描述）信息

执行结果：

```shell
[root@localhost ~]# docker images --digests
REPOSITORY                             TAG                 DIGEST                                                                    IMAGE ID            CREATED             SIZE
docker.io/mysql                        latest              sha256:8b7b328a7ff6de46ef96bcf83af048cb00a1c86282bfca0cb119c84568b4caf6   be0dbf01a0f3        2 weeks ago         541 MB
```

## 5.docker images --no-trunc
功能：显示完整的镜像id信息

执行结果：

REPOSITORY                             TAG                 IMAGE ID                                                                  CREATED             SIZE
docker.io/mysql                        latest              sha256:be0dbf01a0f3f46fc8c88b67696e74e7005c3e16d9071032fa0cd89773771576   2 weeks ago         541 MB
6.docker images --no-trunc --digests
功能：显示完整的镜像id信息和镜像描述

执行结果：

REPOSITORY                             TAG                 DIGEST                                                                    IMAGE ID                                                                  CREATED             SIZE
docker.io/mysql                        latest              sha256:8b7b328a7ff6de46ef96bcf83af048cb00a1c86282bfca0cb119c84568b4caf6   sha256:be0dbf01a0f3f46fc8c88b67696e74e7005c3e16d9071032fa0cd89773771576   2 weeks ago         541 MB
2.仓库镜像信息查询：docker search [镜像名称]
功能：从仓库中查询镜像信息

执行结果：

[root@localhost ~]# docker search tomcat
INDEX       NAME                                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat                        Apache Tomcat is an open source implementa...  2761      [OK]       
docker.io   docker.io/tomee                         Apache TomEE is an all-Apache Java EE cert...  79        [OK]       
docker.io   docker.io/dordoka/tomcat                Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 ba...  54                   [OK]
docker.io   docker.io/bitnami/tomcat                Bitnami Tomcat Docker Image                     35                   [OK]
...
1.docker search [镜像名称] --no-trunc
功能：显示完整的镜像描述

执行结果：

[root@localhost ~]# docker search tomcat --no-trunc
INDEX       NAME                                    DESCRIPTION                                                                                            STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat                        Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies   2761      [OK]       
docker.io   docker.io/tomee                         Apache TomEE is an all-Apache Java EE certified stack where Apache Tomcat is top dog.                 79        [OK]       
docker.io   docker.io/dordoka/tomcat                Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 based docker container.                                       54                   [OK]
docker.io   docker.io/bitnami/tomcat                Bitnami Tomcat Docker Image                                                                            35                   [OK]
docker.io   docker.io/kubeguide/tomcat-app          Tomcat image for Chapter 1                                                                             28                   
docker.io   docker.io/consol/tomcat-7.0             Tomcat 7.0.57, 8080, "admin/admin"                                                                     17                   [OK]
docker.io   docker.io/cloudesire/tomcat             Tomcat server, 6/7/8                                                                                   15                   [OK]
docker.io   docker.io/aallam/tomcat-mysql           Debian, Oracle JDK, Tomcat & MySQL                                                                     13                   [OK]
...
2.docker search [镜像名称] --filter=stars=[指定值]等价于 docker search [镜像名称] -f=stars=[指定值]
功能：列出收藏数不小于指定值的镜像信息

执行结果：

[root@localhost ~]# docker search tomcat -f=stars=30
INDEX       NAME                       DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat           Apache Tomcat is an open source implementa...  2761      [OK]       
docker.io   docker.io/tomee            Apache TomEE is an all-Apache Java EE cert...  79        [OK]       
docker.io   docker.io/dordoka/tomcat   Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 ba...  54                   [OK]
docker.io   docker.io/bitnami/tomcat   Bitnami Tomcat Docker Image                     35                   [OK]
3.docker search tomcat --automated
功能：只列出automated build类型的镜像信息

执行结果：

[root@localhost ~]# docker search tomcat --automated
Flag --automated has been deprecated, use --filter=automated=true instead
INDEX       NAME                                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/dordoka/tomcat                Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 ba...  54                   [OK]
docker.io   docker.io/bitnami/tomcat                Bitnami Tomcat Docker Image                     35                   [OK]
docker.io   docker.io/consol/tomcat-7.0             Tomcat 7.0.57, 8080, "admin/admin"              17                   [OK]
docker.io   docker.io/cloudesire/tomcat             Tomcat server, 6/7/8                            15                   [OK]
...
4.docker search [镜像名] --limit=[值]
功能：只列出指定条数的镜像信息,可以和前面的混搭使用

执行结果：

[root@localhost ~]# docker search tomcat --limit=2
INDEX       NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat                 Apache Tomcat is an open source implementa...  2761      [OK]       
docker.io   docker.io/bitnami/tomcat         Bitnami Tomcat Docker Image                     35                   [OK]
3.拉取镜像：docker pull [镜像名]:[TAG]
功能：从远程仓库中拉取镜像，如果没有指定TAG,默认为latest

执行结果：

[root@localhost docker]# docker pull zookeeper
Using default tag: latest
Trying to pull repository docker.io/library/zookeeper ...
latest: Pulling from docker.io/library/zookeeper
8559a31e96f4: Already exists 
65306eca6b8e: Pull complete 
ddbf88050b6e: Pull complete 
0cb03c61bf26: Pull complete 
0fae52060f18: Pull complete 
a0d6ea5c70b0: Pull complete 
7130f613f7ed: Pull complete 
a76b0e46e043: Pull complete 
Digest: sha256:4a466f78baa1ac26de51ce4619a41db8cf174bd683ac8b3285aca97ac84aa034
Status: Downloaded newer image for docker.io/zookeeper:latest
4.移除本地镜像：docker rmi [镜像id...]
由于不想再次下载，这里将不展示其执行结果

1.删除单个本地镜像：docker rmi -f [镜像id]

2.删除多个本地镜像：docker rmi -f [镜像名:TAG 镜像名:TAG...]

3.删除本地全部镜像：docker rmi -f ${docker images -aq}
三、容器命令
1.新建并启动容器
1.命令格式：docker run [OPTIONS] IMAGE [COMMAND] [ARG...] 2.OPTIONS简介
1.--name='[容器别名]'：为容器指定一个别名 2.-i：以交互模式运行容器，通常与-t一起使用 3.-t：为容器重新分配一个伪输入终端，通常与-i一起使用 4.-P：随机端口映射 5.-p：指定端口映射 1.ip:hostPort:containerPort 2.ip::containerPort 3.hostPort:containerPort 4.containerPort 6.-d：创建自动式守护容器

2.列出容器
命令格式：docker ps [Options] 2.OPTIONS简介
1.列出当前正在运行的容器：docker ps

[root@localhost ~]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2284a529de        mysql               "docker-entrypoint..."   28 hours ago        Up 3 seconds        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
2.列出当前的+之前运行过的容器：docker ps -a

CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2284a529de        mysql               "docker-entrypoint..."   28 hours ago        Up 2 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
3.显示最近创建的容器：docker ps -l

[root@localhost ~]# docker ps -l
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2284a529de        mysql               "docker-entrypoint..."   28 hours ago        Up 4 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
4.只显示容器编号：docker ps -q

[root@localhost ~]# docker ps -q
7b2284a529de
5.全部打印输出：docker ps --no-trunc

[root@localhost ~]# docker ps --no-trunc
CONTAINER ID                                                       IMAGE               COMMAND                         CREATED             STATUS              PORTS                               NAMES
7b2284a529de0f34723880792b2fa16107c787ff0bfc6b75fe3213a12b63dc26   mysql               "docker-entrypoint.sh mysqld"   28 hours ago        Up 7 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
3.退出容器（交互式容器）
1.容器停止并退出：exit

2.容器不停止退出: ctrl+P+Q
4.启动容器：docker start [容器名/容器id]
[root@localhost ~]# docker start mysql01
mysql01
5.重启容器：docker restart mysql01
[root@localhost ~]# docker restart mysql01
mysql01
6.停止容器
1.停止容器：docker stop [容器名]
[root@localhost ~]# docker stop mysql01
mysql01
2.强制停止容器：docker kill [容器名]
[root@localhost ~]# docker kill mysql01
mysql01
7.删除容器
1.删除单个容器：docker rm [容器名/容器id]

2.一次性删除多个容器：
1.docker rm -f ${docker ps -aq} 2.docker ps -aq | xargs docker rm

四、容器日志查看
1.命令格式：docker log -f -t --tail [行数] 容器id

2.OPTIONS简介
1.-t：在日志中加入时间戳

[root@localhost ~]# docker logs -t mysql01
2020-06-26T08:19:18.343090000Z 2020-06-26 08:19:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26T08:19:20.634688000Z 2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2020-06-26T08:19:20.734797000Z 2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26T08:19:21.226702000Z 2020-06-26T08:19:21.210250Z 0 [Warning] [MY-011070] [Server] 'Disabling symbolic links using --skip-symbolic-links (or equivalent) is the default.Consider not using this option as it' is deprecated and will be removed in a future release.
2.-f：跟随最新的日志打印

[root@localhost ~]# docker logs -f mysql01
2020-06-26 08:19:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26T08:19:21.210250Z 0 [Warning] [MY-011070] [Server] 'Disabling symbolic links using --skip-symbolic-links (or equivalent) is the default.Consider not using this option as it' is deprecated and will be removed in a future release.
3.--tail：显示最后多少条日志

[root@localhost ~]# docker logs --tail 3 mysql01
2020-06-26T09:09:28.695860Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
2020-06-26T09:09:28.702762Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users.Consider choosing a different directory.
2020-06-26T09:09:28.745485Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections.Version: '8.0.20'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
五、查看容器内运行的进程
1.命令格式：docker top 容器名/id
[root@localhost ~]# docker top mysql01
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
systemd+            3424                3408                1                   05:09               ?                   00:00:08            mysqld
六、查看容器内部细节
1.命令格式：docker inspect 容器名/id
[root@localhost ~]# docker inspect mysql01
[
    {
        "Id": "7b2284a529de0f34723880792b2fa16107c787ff0bfc6b75fe3213a12b63dc26",
        "Created": "2020-06-25T03:41:42.117229229Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "mysqld"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 3424,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2020-06-26T09:09:27.12868915Z",
            "FinishedAt": "2020-06-26T09:00:09.694185066Z"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "457ff21afb25582c73071b7a50530d8505d1ee17916641703f61c5be1085a47c",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "3306/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "3306"
                    }
                ],
                "33060/tcp": null
            },
            ...
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": 
                    ...
                }
            }
        }
    }
]
七、进入正在运行的容器并以命令行交互
1.命令格式一：docker exec -it [容器名/id] /bin/bash，不需要进入伪输入终端就可以操作容器
[root@localhost ~]# docker exec -it mysql01 /bin/bash
root@7b2284a529de:/# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.20 MySQL Community Server - GPL
mysql>
2.命令格式二：docker attach [容器名/id],必须进入到伪输入终端才可以和容器交互
八、将容器中文件拷贝到主机中
命令格式：docker cp 容器id:容器内部路径 目的主机路径

其主要目的是保存容器中的数据，将其持久化
一、帮助命令
docker版本信息：docker version
功能：查看docker版本相关信息

docker详细信息： docker info
功能：查看docker的详细信息

docker命令指南：docker --help
功能：可以查看docker命令的使用方法

二、镜像命令
1. 本地镜像信息查询：docker images
功能：查看docker中包含的镜像信息

执行结果：

[root@localhost ~]# docker images
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
docker.io/mysql                        latest              be0dbf01a0f3        2 weeks ago         541 MB
docker.io/longhronshens/mycat-docker   latest              f9a4ece7c742        2 years ago         793 MB
选项说明：

Repository：表示镜像的仓库源
TAG：镜像的标签，同一个仓库源可以有多个TAG，代表不同的版本
IMAGE ID：镜像id
CREATED：镜像创建时间
SIZE：镜像大小

docker images -a
功能：列出本地所有镜像（包含中间层）

执行结果：

[root@localhost ~]# docker images -a
REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
docker.io/mysql                        latest              be0dbf01a0f3        2 weeks ago         541 MB
docker.io/longhronshens/mycat-docker   latest              f9a4ece7c742        2 years ago         793 MB
docker images -q
功能：只显示镜像id

执行结果：

[root@localhost ~]# docker images -q
be0dbf01a0f3
f9a4ece7c742
docker images -qa
功能：只显示所有镜像id（包含中间层）

执行结果：

[root@localhost ~]# docker images -q
be0dbf01a0f3
f9a4ece7c742
docker images --digests
功能：显示镜像的摘要（描述）信息

执行结果：

[root@localhost ~]# docker images --digests
REPOSITORY                             TAG                 DIGEST                                                                    IMAGE ID            CREATED             SIZE
docker.io/mysql                        latest              sha256:8b7b328a7ff6de46ef96bcf83af048cb00a1c86282bfca0cb119c84568b4caf6   be0dbf01a0f3        2 weeks ago         541 MB
docker images --no-trunc
功能：显示完整的镜像id信息

执行结果：

REPOSITORY                             TAG                 IMAGE ID                                                                  CREATED             SIZE
docker.io/mysql                        latest              sha256:be0dbf01a0f3f46fc8c88b67696e74e7005c3e16d9071032fa0cd89773771576   2 weeks ago         541 MB
docker images --no-trunc --digests
功能：显示完整的镜像id信息和镜像描述

执行结果：

REPOSITORY                             TAG                 DIGEST                                                                    IMAGE ID                                                                  CREATED             SIZE
docker.io/mysql                        latest              sha256:8b7b328a7ff6de46ef96bcf83af048cb00a1c86282bfca0cb119c84568b4caf6   sha256:be0dbf01a0f3f46fc8c88b67696e74e7005c3e16d9071032fa0cd89773771576   2 weeks ago         541 MB
2. 仓库镜像信息查询：docker search [镜像名称]
功能：从仓库中查询镜像信息

执行结果：

[root@localhost ~]# docker search tomcat
INDEX       NAME                                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat                        Apache Tomcat is an open source implementa...   2761      [OK]       
docker.io   docker.io/tomee                         Apache TomEE is an all-Apache Java EE cert...   79        [OK]       
docker.io   docker.io/dordoka/tomcat                Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 ba...   54                   [OK]
docker.io   docker.io/bitnami/tomcat                Bitnami Tomcat Docker Image                     35                   [OK]
...
docker search [镜像名称] --no-trunc
功能：显示完整的镜像描述

执行结果：

[root@localhost ~]# docker search tomcat --no-trunc
INDEX       NAME                                    DESCRIPTION                                                                                            STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat                        Apache Tomcat is an open source implementation of the Java Servlet and JavaServer Pages technologies   2761      [OK]       
docker.io   docker.io/tomee                         Apache TomEE is an all-Apache Java EE certified stack where Apache Tomcat is top dog.                  79        [OK]       
docker.io   docker.io/dordoka/tomcat                Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 based docker container.                                        54                   [OK]
docker.io   docker.io/bitnami/tomcat                Bitnami Tomcat Docker Image                                                                            35                   [OK]
docker.io   docker.io/kubeguide/tomcat-app          Tomcat image for Chapter 1                                                                             28                   
docker.io   docker.io/consol/tomcat-7.0             Tomcat 7.0.57, 8080, "admin/admin"                                                                     17                   [OK]
docker.io   docker.io/cloudesire/tomcat             Tomcat server, 6/7/8                                                                                   15                   [OK]
docker.io   docker.io/aallam/tomcat-mysql           Debian, Oracle JDK, Tomcat & MySQL                                                                     13                   [OK]
...
docker search [镜像名称] --filter=stars=[指定值]等价于 docker search [镜像名称] -f=stars=[指定值]
功能：列出收藏数不小于指定值的镜像信息

执行结果：

[root@localhost ~]# docker search tomcat -f=stars=30
INDEX       NAME                       DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat           Apache Tomcat is an open source implementa...   2761      [OK]       
docker.io   docker.io/tomee            Apache TomEE is an all-Apache Java EE cert...   79        [OK]       
docker.io   docker.io/dordoka/tomcat   Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 ba...   54                   [OK]
docker.io   docker.io/bitnami/tomcat   Bitnami Tomcat Docker Image                     35                   [OK]
docker search tomcat --automated
功能：只列出automated build类型的镜像信息

执行结果：

[root@localhost ~]# docker search tomcat --automated
Flag --automated has been deprecated, use --filter=automated=true instead
INDEX       NAME                                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/dordoka/tomcat                Ubuntu 14.04, Oracle JDK 8 and Tomcat 8 ba...   54                   [OK]
docker.io   docker.io/bitnami/tomcat                Bitnami Tomcat Docker Image                     35                   [OK]
docker.io   docker.io/consol/tomcat-7.0             Tomcat 7.0.57, 8080, "admin/admin"              17                   [OK]
docker.io   docker.io/cloudesire/tomcat             Tomcat server, 6/7/8                            15                   [OK]
...
docker search [镜像名] --limit=[值]
功能：只列出指定条数的镜像信息,可以和前面的混搭使用

执行结果：

[root@localhost ~]# docker search tomcat --limit=2
INDEX       NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
docker.io   docker.io/tomcat                 Apache Tomcat is an open source implementa...   2761      [OK]       
docker.io   docker.io/bitnami/tomcat         Bitnami Tomcat Docker Image                     35                   [OK]
3. 拉取镜像：docker pull [镜像名]:[TAG]
功能：从远程仓库中拉取镜像，如果没有指定TAG,默认为latest

执行结果：

[root@localhost docker]# docker pull zookeeper
Using default tag: latest
Trying to pull repository docker.io/library/zookeeper ... 
latest: Pulling from docker.io/library/zookeeper
8559a31e96f4: Already exists 
65306eca6b8e: Pull complete 
ddbf88050b6e: Pull complete 
0cb03c61bf26: Pull complete 
0fae52060f18: Pull complete 
a0d6ea5c70b0: Pull complete 
7130f613f7ed: Pull complete 
a76b0e46e043: Pull complete 
Digest: sha256:4a466f78baa1ac26de51ce4619a41db8cf174bd683ac8b3285aca97ac84aa034
Status: Downloaded newer image for docker.io/zookeeper:latest
4. 移除本地镜像：docker rmi [镜像id...]
由于不想再次下载，这里将不展示其执行结果

删除单个本地镜像：docker rmi -f [镜像id]

删除多个本地镜像：docker rmi -f [镜像名:TAG 镜像名:TAG...]
删除本地全部镜像：docker rmi -f ${docker images -aq}
三、容器命令
1. 新建并启动容器
命令格式：docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
OPTIONS简介

--name='[容器别名]'：为容器指定一个别名
-i：以交互模式运行容器，通常与-t一起使用
-t：为容器重新分配一个伪输入终端，通常与-i一起使用
-P：随机端口映射
-p：指定端口映射
ip:hostPort:containerPort
ip::containerPort
hostPort:containerPort
containerPort
-d：创建自动式守护容器
2. 列出容器
命令格式：docker ps [Options]
OPTIONS简介

列出当前正在运行的容器：docker ps
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2284a529de        mysql               "docker-entrypoint..."   28 hours ago        Up 3 seconds        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
列出当前的+之前运行过的容器：docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2284a529de        mysql               "docker-entrypoint..."   28 hours ago        Up 2 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
显示最近创建的容器：docker ps -l
[root@localhost ~]# docker ps -l
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
7b2284a529de        mysql               "docker-entrypoint..."   28 hours ago        Up 4 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
只显示容器编号：docker ps -q
[root@localhost ~]# docker ps -q
7b2284a529de
全部打印输出：docker ps --no-trunc
[root@localhost ~]# docker ps --no-trunc
CONTAINER ID                                                       IMAGE               COMMAND                         CREATED             STATUS              PORTS                               NAMES
7b2284a529de0f34723880792b2fa16107c787ff0bfc6b75fe3213a12b63dc26   mysql               "docker-entrypoint.sh mysqld"   28 hours ago        Up 7 minutes        0.0.0.0:3306->3306/tcp, 33060/tcp   mysql01
3.退出容器（交互式容器）
容器停止并退出：exit

容器不停止退出: ctrl+P+Q
4. 启动容器：docker start [容器名/容器id]
[root@localhost ~]# docker start mysql01
mysql01
5. 重启容器：docker restart mysql01
[root@localhost ~]# docker restart mysql01
mysql01
6. 停止容器
停止容器：docker stop [容器名]
[root@localhost ~]# docker stop mysql01
mysql01
强制停止容器：docker kill [容器名]
[root@localhost ~]# docker kill mysql01
mysql01
7. 删除容器
删除单个容器：docker rm [容器名/容器id]

一次性删除多个容器：
docker rm -f ${docker ps -aq}
docker ps -aq | xargs docker rm
四、容器日志查看
命令格式：docker log -f -t --tail [行数] 容器id

OPTIONS简介
-t：在日志中加入时间戳
[root@localhost ~]# docker logs -t mysql01
2020-06-26T08:19:18.343090000Z 2020-06-26 08:19:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26T08:19:20.634688000Z 2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2020-06-26T08:19:20.734797000Z 2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26T08:19:21.226702000Z 2020-06-26T08:19:21.210250Z 0 [Warning] [MY-011070] [Server] 'Disabling symbolic links using --skip-symbolic-links (or equivalent) is the default. Consider not using this option as it' is deprecated and will be removed in a future release.
-f：跟随最新的日志打印
[root@localhost ~]# docker logs -f mysql01
2020-06-26 08:19:18+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2020-06-26 08:19:20+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.20-1debian10 started.
2020-06-26T08:19:21.210250Z 0 [Warning] [MY-011070] [Server] 'Disabling symbolic links using --skip-symbolic-links (or equivalent) is the default. Consider not using this option as it' is deprecated and will be removed in a future release.
--tail：显示最后多少条日志
[root@localhost ~]# docker logs --tail 3 mysql01
2020-06-26T09:09:28.695860Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
2020-06-26T09:09:28.702762Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
2020-06-26T09:09:28.745485Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.20'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
五、查看容器内运行的进程
命令格式：docker top 容器名/id
[root@localhost ~]# docker top mysql01
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
systemd+            3424                3408                1                   05:09               ?                   00:00:08            mysqld
六、查看容器内部细节
命令格式：docker inspect 容器名/id
[root@localhost ~]# docker inspect mysql01
[
    {
        "Id": "7b2284a529de0f34723880792b2fa16107c787ff0bfc6b75fe3213a12b63dc26",
        "Created": "2020-06-25T03:41:42.117229229Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "mysqld"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 3424,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2020-06-26T09:09:27.12868915Z",
            "FinishedAt": "2020-06-26T09:00:09.694185066Z"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "457ff21afb25582c73071b7a50530d8505d1ee17916641703f61c5be1085a47c",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "3306/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "3306"
                    }
                ],
                "33060/tcp": null
            },
            ...
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": 
                    ...
                }
            }
        }
    }
]
七、进入正在运行的容器并以命令行交互
命令格式一：docker exec -it [容器名/id] /bin/bash，不需要进入伪输入终端就可以操作容器
[root@localhost ~]# docker exec -it mysql01 /bin/bash
root@7b2284a529de:/# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.20 MySQL Community Server - GPL
mysql>
命令格式二：docker attach [容器名/id],必须进入到伪输入终端才可以和容器交互
八、将容器中文件拷贝到主机中
命令格式：docker cp 容器id:容器内部路径 目的主机路径

其主要目的是保存容器中的数据，将其持久化