# Vue.js 问题解决

## 1. [vue-cli3 没有config.js文件的解决办法](https://www.jianshu.com/p/a47662af75c5)

## 2.Vue 问题 CLI-idea

[官方-脚手架](https://cli.vuejs.org/zh/guide/installation.html)

![image.png](https://i.loli.net/2020/02/25/NvikegKqHwzj74f.png)

## 3. npm一直停在"checking installable status"或者下载卡住的问题

* 原因：旧的npm缓存与项目冲突和资源下载不畅

解决方法：

步骤一

```cmd
(sudo) npm cache clean
```

步骤二

```cmd
npm config set registry https://registry.npm.taobao.org
```

[备选方案](https://www.cnblogs.com/sansancn/p/11139030.html)

[备选方案2](https://blog.csdn.net/Ellen5203/article/details/104339425)

## 4. [vue项目中开启Eslint碰到的一些问题及其规范](https://www.cnblogs.com/plb2307/p/10586585.html)
