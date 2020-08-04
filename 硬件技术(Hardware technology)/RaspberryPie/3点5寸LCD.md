# 3.5寸LCD显示器

## 安装

风扇自选安装，不赘述

![image.png](https://i.loli.net/2020/08/04/cHyiTtlS3z2De1V.png)

## 树莓派操作指南

首先安装raspbian系统

```cmd
sudo rm -rf LCD-show
git clone https://github.com/Lcdwiki/LCD-show.git
cd LCD-show
sudo ./MHS35-show

```

## 旋转屏幕

```cmd

cd LCD-show
sudo ./rotate.sh 90(或者其他角度)
```
