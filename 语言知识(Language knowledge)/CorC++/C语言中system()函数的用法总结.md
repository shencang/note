# C语言中system()函数的用法总结(转)

system()函数功能强大，很多人用却对它的原理知之甚少先看linux版system函数的源码：

```c
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>
#include <unistd.h>

int system(const char * cmdstring)
{
    pid_t pid;
    int status;


    if(cmdstring == NULL){
         return (1);
    }

    if((pid = fork())<0){
            status = -1;
    }

    else if(pid = 0){
        execl("/bin/sh", "sh", "-c", cmdstring, (char *)0);
        exit(127); //子进程正常执行则不会执行此语句
    }

    else{
           while(waitpid(pid, &status, 0) < 0){
                if(errno != EINTER){
                    status = -1;
                    break;
                }
            }
        }

        return status;
}
```

分析一下原理估计就能看懂了：

当system接受的命令为NULL时直接返回，否则fork出一个子进程，因为fork在两个进程：父进程和子进程中都返回，这里要检查返回的pid，fork在子进程中返回0，在父进程中返回子进程的pid，父进程使用waitpid等待子进程结束，子进程则是调用execl来启动一个程序代替自己，execl("/bin/sh", "sh", "-c", cmdstring, (char*)0)是调用shell，这个shell的路径是/bin/sh，后面的字符串都是参数，然后子进程就变成了一个shell进程，这个shell的参数是cmdstring，就是system接受的参数。在windows中的shell是command，想必大家很熟悉shell接受命令之后做的事了。

再解释下fork的原理：当一个进程A调用fork时，系统内核创建一个新的进程B，并将A的内存映像复制到B的进程空间中，因为A和B是一样的，那么他们怎么知道自己是父进程还是子进程呢，看fork的返回值就知道，上面也说了fork在子进程中返回0，在父进程中返回子进程的pid。

windows中的情况也类似，就是execl换了个又臭又长的名字，参数名也换的看了让人发晕的，我在MSDN中找到了原型，给大家看看：

```c
HINSTANCE   ShellExecute(
                HWND   hwnd,
                LPCTSTR   lpVerb,
                LPCTSTR   lpFile,
                LPCTSTR   lpParameters,
                LPCTSTR   lpDirectory,
                INT   nShowCmd
   );
```

用法见下：

```c
ShellExecute(NULL, "open", "c:\\a.reg", NULL, NULL, SW_SHOWNORMAL);
```

你也许会奇怪 ShellExecute中有个用来传递父进程环境变量的参数 lpDirectory，linux中的execl却没有，这是因为execl是编译器的函数（在一定程度上隐藏具体系统实现），在linux中它会接着产生一个linux系统的调用 execve, 原型见下：

```c
int execve(const char * file,const char **argv,const char **envp);
```

看到这里就会明白为什么system（）会接受父进程的环境变量，但是用system改变环境变量后，system一返回主函数还是没变。原因从system的实现可以看到，它是通过产生新进程实现的，从我的分析中可以看到父进程和子进程间没有进程通信，子进程自然改变不了父进程的环境变量。

使用了system函数就能执行dos指令。

```c
#include <stdio.h>
#include <stdlib.h>

xiaoyu()
{
    char *a;
    int n=0;
    FILE *f;
    f=fopen("file.bat","w+");/*新建一个批处理*/
    if(f==NULL) {
        exit(1);
    }

    a="echo"; /*DOS命令*/
    for(n=65;n<=90;n++) {/*大写A-Z*/
        fprintf(f,"%s %c\n",a,n);/*利用ASCII码输出A-Z，写出批处理*/
    }
    fclose(f);
    system("file.bat");/*运行批处理*/
}

int main(int argc, char argv[])
{
    char *string;

    xiaoyu();
    string="echo C语言的system函数\n";/*输出中文*/
    system(string);
    system("pause");/*程序暂停*/
    return 0;
}
```

C中可以使用DOS命令，以后编程通过调用DOS命令很多操作就简单多了。
