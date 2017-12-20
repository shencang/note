#C语言system函数
Windows函数

windows操作系统下system () 函数详解（主要是在C语言中的应用）　函数名： system
功 能： 发出一个DOS命令
用 法： int system(char *command);
system函数已经被收录在标准c库中，可以直接调用
程序例：
```c 
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
printf("About to spawn and run a DOS command\n");
system("dir");
return 0;
}
```

```c++
又如：system("pause")可以实现冻结屏幕，便于观察程序的执行结果；system("CLS")可以实现清屏操作。而调用color函数可以改变控制台的前景色和背景，具体参数在下面说明。
例如，用 system("color 0A"); 其中color后面的0是背景色代号，A是前景色代号。各颜色代码如下：
0=黑色 1=蓝色 2=绿色 3=湖蓝色 4=红色 5=紫色 6=黄色 7=白色 8=灰色 9=淡蓝色 A=淡绿色 B=淡浅绿色 C=淡红色 D=淡紫色 E=淡黄色 F=亮白色
ASSOC    显示或修改文件扩展名关联。
AT       计划在计算机上运行的命令和程序。
ATTRIB   显示或更改文件属性。
BREAK    设置或清除扩展式 CTRL+C 检查。
CACLS    显示或修改文件的访问控制列表(ACLs)。
CALL     从另一个批处理程序调用这一个。
CD       显示当前目录的名称或将其更改。
CHCP     显示或设置活动代码页数。
CHDIR    显示当前目录的名称或将其更改。
CHKDSK   检查磁盘并显示状态报告。
CHKNTFS 显示或修改启动时间磁盘检查。
CLS      清除屏幕。
CMD      打开另一个 Windows 命令解释程序窗口。
COLOR    设置默认控制台前景和背景颜色。
COMP     比较两个或两套文件的内容。
COMPACT 显示或更改 NTFS 分区上文件的压缩。
CONVERT 将 FAT 卷转换成 NTFS。您不能转换当前驱动器。
COPY     将至少一个文件复制到另一个位置。
DATE     显示或设置日期。
DEL      删除至少一个文件。
DIR      显示一个目录中的文件和子目录。
DISKCOMP 比较两个软盘的内容。
DISKCOPY 将一个软盘的内容复制到另一个软盘。
DOSKEY   编辑命令行、调用 Windows 命令并创建宏。
ECHO     显示消息，或将命令回显打开或关上。
ENDLOCAL 结束批文件中环境更改的本地化。
ERASE    删除至少一个文件。
EXIT     退出 CMD.EXE 程序(命令解释程序)。
FC       比较两个或两套文件，并显示不同处。
FIND     在文件中搜索文字字符串。
FINDSTR 在文件中搜索字符串。
FOR      为一套文件中的每个文件运行一个指定的命令
FORMAT   格式化磁盘，以便跟 Windows 使用。
FTYPE    显示或修改用于文件扩展名关联的文件类型。
GOTO     将 Windows 命令解释程序指向批处理程序中某个标明的行。
GRAFTABL 启用 Windows 来以图像模式显示扩展字符集。
HELP     提供 Windows 命令的帮助信息。
IF       执行批处理程序中的条件性处理。
LABEL    创建、更改或删除磁盘的卷标。
MD       创建目录。
MKDIR    创建目录。
MODE     配置系统设备。
MORE     一次显示一个结果屏幕。
MOVE     将文件从一个目录移到另一个目录。
PATH     显示或设置可执行文件的搜索路径。
PAUSE    暂停批文件的处理并显示消息。
POPD     还原 PUSHD 保存的当前目录的上一个值。
PRINT    打印文本文件。
PROMPT   更改 Windows 命令提示符。
PUSHD    保存当前目录，然后对其进行更改。
RD       删除目录。
RECOVER 从有问题的磁盘恢复可读信息。
REM      记录批文件或 CONFIG.SYS 中的注释。
REN      重命名文件。
RENAME   重命名文件。
REPLACE 替换文件。
RMDIR    删除目录。
SET      显示、设置或删除 Windows 环境变量。
SETLOCAL 开始批文件中环境更改的本地化。
SHIFT    更换批文件中可替换参数的位置。
SORT     对输入进行分类。
START    启动另一个窗口来运行指定的程序或命令。
SUBST    将路径跟一个驱动器号关联。
TIME     显示或设置系统时间。
TITLE    设置 CMD.EXE 会话的窗口标题。
TREE     以图形模式显示驱动器或路径的目录结构。
TYPE     显示文本文件的内容。
VER      显示 Windows 版本。
VERIFY   告诉 Windows 是否验证文件是否已正确写入磁盘。
VOL      显示磁盘卷标和序列号。
XCOPY    复制文件和目录树。

（注意：Microsoft Visual C++6.0 支持system）
```
举例
看了下面实例，相信你会对学到更多system在C程序设计中的应用。
例一：
```c
C语言调用DOS命令实现定时关机：
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int print()
{
printf(" ╪╪╪╪╪╪╧╧╧╧╧╧╧╧╪╪╪╪╪╪\n");
printf("╔═══╧╧C语言关机程序 ╧╧═══╗\n");
printf("║※1.实现10分钟内的定时关闭计算机 ║\n");
printf("║※2.立即关闭计算机　 ║\n");
printf("║※3.注销计算机　 ║\n");
printf("║※0.退出系统　 ║\n");
printf("╚═══════════════════╝\n");
return 0;
}
void main()
{
system("title C语言关机程序");//设置cmd窗口标题
system("mode con cols=48 lines=25");//窗口宽度高度
system("color 0B");
system("date /T");
system("TIME /T");
char cmd[20]="shutdown -s -t ";
char t[5]="0";
print();
int c;
scanf("%d",&c);
getchar();
switch(c)
{
case 1:printf("您想在多少秒后自动关闭计算机？（0~600）\n");scanf("%s",t);system(strcat(cmd,t));break;
case 2:system("shutdown -p");break;
case 3:system("shutdown -l");break;
case 0:break;
default:printf("Error!\n");
}
system("pause");
exit(0);
}
```
例二：
用C语言删除文件，例如文件的位置是d:\123.txt
用system（）函数执行windows命令。
```c
#include <stdlib.h>
#include <stdio.h>
int main(void)
{
system("del d:\123.txt");
return 0;
}
Linux/Unix函数
```
函数详解
（执行shell 命令）
相关函数
fork，execve，waitpid，popen
表头文件
#include<stdlib.h>
定义函数
int system(const char * string);
函数说明
system（）会调用fork（）产生子进程，由子进程来调用/bin/sh-c string来执行参数string字符串所代表的命令，此命令执行完后随即返回原调用的进程。在调用system（）期间SIGCHLD 信号会被暂时搁置，SIGINT和SIGQUIT 信号则会被忽略。
返回值
如果fork（）失败 返回-1：出现错误
如果exec（）失败，表示不能执行Shell，返回值相当于Shell执行了exit（127）
如果执行成功则返回子Shell的终止状态
如果system（）在调用/bin/sh时失败则返回127，其他失败原因返回-1。若参数string为空指针（NULL），则返回非零值>；。如果system（）调用成功则最后会返回执行shell命令后的返回值，但是此返回值也有可能为 system（）调用/bin/sh失败所返回的127，因此最好能再检查errno 来确认执行成功。
附加说明
在编写具有SUID/SGID权限的程序时请勿使用system（），system（）会继承环境变量，通过环境变量可能会造成系统安全的问题。
范例
```c
include<stdlib.h>
main()
{
system（“ls -al /etc/passwd /etc/shadow”）；
}
执行结果：
-rw-r--r-- 1 root root 705 Sep 3 13 :52 /etc/passwd
-r--------- 1 root root 572 Sep 2 15 :34 /etc/shado
```
例2：
```c
char tmp[];
sprintf(tmp,"/bin/mount -t vfat %s /mnt/usb",dev);
system(tmp);
```
其中dev是/dev/sda1.
与exec的区别
1、system（）和exec（）都可以执行进程外的命令，system是在原进程上开辟了一个新的进程，但是exec是用新进程（命令）覆盖了原有的进程
2、system（）和exec（）都有能产生返回值，system的返回值并不影响原有进程，但是exec的返回值影响了原进程
具体例：
效果如下：


```c
#include <stdio.h>  
#include <stdlib.h>  
int main()  
{  
    system("mode con cols=50 lines=25");//窗口宽度高度  
  
    //indicate ten number,black background  
    for(int i=0;i<10;i++)  
        printf("第%2d个数字是：%d\n",i+1,i);  
    //system pause untill some key was pressed  
    system("pause");  
    //console clear the screen  
    system("cls");  
    //console font color be change 02,BLUE  
    system("COLOR 02");  
      
    for(int j=0;j<10;j++)  
        printf("第%d个符号是：%c\n",j+1,(char)(63+j));  
    system("pause");  
    //  
    system("VOL");  
    system("pause");  
    return 0;  
}  

