# 3.5寸LCD显示器

[树莓派专用LCD Wiki网站](https://blog.csdn.net/JOYIST/article/details/90694835)

[LCD-wiki](http://www.lcdwiki.com/zh/%E9%A6%96%E9%A1%B5)

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

## 安装虚拟键盘

* 1、 安装必需文件

```cmd
sudo apt-get update
sudo apt-get install libfakekey-dev libpng-dev libxft-dev autoconf libtool
```

* 2、安装编译虚拟键盘matchbox-keyboard

```cmd
git clone https://github.com/mwilliams03/matchbox-keyboard.git
cd matchbox-keyboard
./autogen.sh
```

(注意:” ./autogen.sh”执行时间较
长约几分钟，正确执行后显示界面如下，如执行完不出现类似以下界面则需检查是否有error提示项)

![image.png](https://i.loli.net/2020/08/07/PJQmsj1iUMvgRO2.png)

接着执行：

```cmd
sudo make
sudo make install
```

* 3、安装虚拟键盘所用的共享库

```cmd
sudo apt-get install libmatchbox1
```

如下图：

![image.png](https://i.loli.net/2020/08/07/Y1r3JlL6oHPba7i.png)

* 4、创建虚拟键盘启动脚本

```cmd
sudo nano /usr/bin/toggle-matchbox-keyboard.sh
```

粘贴以下内容并按Ctrl + X和Y保存退出

```t
#!/bin/bash
#This script toggle the virtual keyboard
PID=`pidof matchbox-keyboard`
if [ ! -e $PID ]; then
killall matchbox-keyboard
else
matchbox-keyboard -s 50 extended&
fi
```

给以上脚本增加可执行权限

```cmd
sudo chmod +x /usr/bin/toggle-matchbox-keyboard.sh
```

* 5、把以上脚本增加到开始菜单

```cmd
sudo nano /usr/share/applications/toggle-matchbox-keyboard.desktop
```

粘贴以下内容并按Ctrl+X和Y保存退出

```t
[Desktop Entry]
Name=Toggle Matchbox Keyboard
Comment=Toggle Matchbox Keyboard
Exec=toggle-matchbox-keyboard.sh
Type=Application
Icon=matchbox-keyboard.png
Categories=Panel;Utility;MB
X-MB-INPUT-MECHANSIM=True
```

* 6、在任务栏上创建图标(注意该步骤必须使用"pi"用户权限，如果使用管理员权限，将找不到该文件)

```cmd
nano ~/.config/lxpanel/LXDE-pi/panels/panel
```

* 7、找到类似以下命令(树莓派版本不同可能默认内容有差异)

```cmd
Plugin {
type=launchbar
Config {
    Button {
      id=/usr/share/applications/lxde-x-www-browser.desktop
    }
    Button {
      id=/usr/share/raspi-ui-overrides/applications/pcmanfm.desktop
    }
    Button {
      id=/usr/share/raspi-ui-overrides/applications/lxterminal.desktop
    }
    Button {
      id=/usr/share/applications/wolfram-mathematica.desktop
    }
    Button {
      id=/usr/share/applications/wolfram-language.desktop
    }
  }
}
```

添加以下代码增加一个图标项

```cmd
  Button {
id=toggle-matchbox-keyboard.desktop
        }
```

修改完效果如下图所示：

![image.png](https://i.loli.net/2020/08/07/bEkv1QB5wdmTLof.png)

* 8、修改完后执行以下命令重启系统，正常可看到屏幕任务栏处多出了一个虚拟键盘图标

```cmd
sudo reboot
P.S. 通过SSH登陆如何改变虚拟键盘大小

DISPLAY=:0.0 matchbox-keyboard -s 50 extended
DISPLAY=:0.0 matchbox-keyboard -s 100 extended
```
