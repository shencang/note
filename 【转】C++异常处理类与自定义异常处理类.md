# 【转】C++异常处理类与自定义异常处理类
   作者：CaptainYaung
   
例1：自定义一个继承自excepton的异常类myException
C++标准中，定义在<stdexcept>中的任何异常类都派生自exception Class，本例也只是简单地由exception继承，在try段抛出一个异常并捕捉。代码如下：
```c++

#include<exception>    
#include<iostream>    
using namespace std;    
    
//customized exception class 'myException'    
class myException:public exception    
{    
public:    
    myException():exception("ERROR! Don't divide a number by integer zero.\n")    
    {    
    }    
};    
//entry of the application    
int main()    
{    
    int x=100,y=0;    
    try    
    {    
        if(y==0) throw myException();    
        else cout<<x/y;    
    }    
    catch(myException& me)    
    {    
        cout<<me.what();    
    }    
    system("pause");    
    return 0;    
}    
```

结果如下：
```c++
ERROR! Don't divide a number by integer zero.

请按任意键继续. . .   
```                                               
显然，异常被捕捉到了。此处需要说明的是，VC对异常处理类exception进行了扩展，本例之所以能够使用exception("ERROR!....")的初始化方法正出于这样的原因，C++标准是不允许这样做的。
与此同时，VC又没有遵循标准，有力地支持terminate和unexpected，它只保留了语法，却在编译运行时不提供支持。为了结合terminate和unexpected更加深入了解C++的异常处理，下面的例子采用Dev cpp IDE实现。
例2：依照C++标准实现自定义异常类myException并将throw语句封装到函数check()中
涉及到的更改正如标题所述，（1）重写基类的what()函数，返回错误信息；（2）将throw myException()封装到check()函数中；(3)允许check()函数抛出myException类型的异常。代码如下：

```c++
#include<exception>    
#include<iostream>    
using namespace std;    
    
//customized exception class 'myException'    
class myException:public exception    
{    
public:    
   const char* what()const throw()//#1     
   {    
        return "ERROR! Don't divide a number by integer zero.\n";    
   }        
};    
void check(int y) throw(myException)//#2    
{    
     if(y==0) throw myException();    
}    
//entry of the application    
int main()    
{    
    int x=100,y=0;    
    try    
    {    
        check(y);    
        cout<<x/y;    
    }    
    catch(myException& me)    
    {    
        cout<<me.what();    
    }    
    system("pause");    
    return 0;    
}    
```


结果与例1完全相同。需说明的是，紧跟check()后的throw列表表明允许该函数抛出的异常类型。这里不得不产生疑问，如果抛出了一个不被允许的异常类型将怎样？
例3：抛出unexpected异常
check函数体之后的throw列表，规定了允许抛出的异常类型，一旦违背，就将触发unexpected。可以把unexpected看作系统自动调用的CALLBACK函数，不同的是，也可以手工触发它的执行。本例的情况属于前者。代码如下：
```c++
#include<exception>    
#include<iostream>    
using namespace std;    
    
//customized exception class 'myException'    
class myException:public exception    
{    
public:    
   const char* what()const throw()    
   {    
        return "ERROR! Don't divide a number by integer zero.\n";    
   }        
};    
void check(int y) throw()//#1 only int-type exception is permitted    
{    
     if(y==0) throw myException();    
}    
void myUnexpected()    
{    
     cout<<"Unexpected exception caught!\n";    
     system("pause");    
     exit(-1);    
}    
//entry of the application    
int main()    
{    
    unexpected_handler oldHandler=set_unexpected(myUnexpected);    
    int x=100,y=0;    
    try    
    {    
        check(y);    
        cout<<x/y;    
    }    
    catch(myException& me)    
    {    
        cout<<me.what();    
    }    
    system("pause");    
    return 0;    
}    
```

结果如下：
```c++
Unexpected exception caught!

请按任意键继续. . .     
```
check函数的throw列表为空，即不允许抛出任何类型的异常，然而实际上当异常发生时，系统不能等闲视之，它将调用unexpected处理方法。所以，限定一个函数throw列表为空是值得程序员警醒的事，需要特别留意。如果将#1处的代码修改为throw(int)等也能得到相同的结果。所谓unexpected异常，说白了就是函数体允许抛出异常类型范围之外的异常。如果check函数后面根本没有throw，则表示函数任何类型的异常都被允许。
例4：抛出函数体允许的异常，但没被捕捉到的情况
思考这样一个问题，如果函数check的throw列表中有异常类型myException，而且在y==0时，它的确抛出myException类型的异常，但是没有被catch到，这时会发生什么？
在正式回答这个问题之前，先讨论“没被catch到”的意思。比如，修改例3的代码如下：（##为修改之处）
```c++

#include<exception>    
#include<iostream>    
using namespace std;    
    
//customized exception class 'myException'    
class myException:public exception    
{    
public:    
   const char* what()const throw()    
   {    
        return "ERROR! Don't divide a number by integer zero.\n";    
   }        
};    
void check(int y) //any type of exception is permitted    
{    
     if(y==0) throw myException();    
}    
void myUnexpected()    
{    
     cout<<"Unexpected exception caught!\n";    
     system("pause");    
     exit(-1);    
}    
//entry of the application    
int main()    
{    
    unexpected_handler oldHandler=set_unexpected(myUnexpected);    
    int x=100,y=0;    
    try    
    {    
        check(y);    
        cout<<x/y;    
    }    
    catch(int &e) //##1 no catch sentence matches the throw type    
    {    
        cout<<e<<endl;    
    }    
    /*               ##2 if add this part, any type which's not handler before will  
                        be caught  
    catch(...)  
    {  
                    cout<<"Unkown exception caught!\n";  
         }  
    */    
    system("pause");    
    return 0;    
}    

```

编译运行，程序将会出错，因为check函数抛出的myException异常没有被处理。在缺省情况下，一旦出现抛出异常没被处理的问题，系统将自动调用abort()函数，终止程序允许，在控制台将会看到这样的提示：
This application has requested the Runtime to terminate it in an unusual way.Please contact the application's support team for more information.
不过可以增加##2部分的代码，catch(...)表示捕捉任何类型的异常。
注意：check函数不被允许的异常类型并不会进入到catch语句的判断中来，因此catch(...)对unexpected exception没有作用。
仍然考虑没有##2部分的情况。正如前面所述，系统将自动调用abort()函数终止程序。实际上，它触发的是terminate，类似于unexpected，仍然可以自定义terminate的处理方法。甚至terminate语法上跟unexpected都十分近似。修改代码为：
```c++

#include<exception>    
#include<iostream>    
using namespace std;    
    
//customized exception class 'myException'    
class myException:public exception    
{    
public:    
   const char* what()const throw()    
   {    
        return "ERROR! Don't divide a number by integer zero.\n";    
   }        
};    
void check(int y) //any type of exception is permitted    
{    
     if(y==0) throw myException();    
}    
void myUnexpected()    
{    
     cout<<"Unexpected exception caught!\n";    
     system("pause");    
     exit(-1);    
}    
void myTerminate() //##1 set it be the terminate handler    
{    
     cout<<"Unhandler exception!\n";    
     system("pause");    
     exit(-1);    
}    
//entry of the application    
int main()    
{    
    unexpected_handler oldHandler=set_unexpected(myUnexpected);    
    terminate_handler preHandler=set_terminate(myTerminate);    
    int x=100,y=0;    
    try    
    {    
        check(y);    
        cout<<x/y;    
    }    
    catch(int &e) //no catch sentence matches the throw type    
    {    
        cout<<e<<endl;    
    }    
    system("pause");    
    return 0;    
}    
```
结果如下：
```c++
Unhandler exception!
请按任意键继续. . .  
```
  
结论：C++为异常处理提供了友好的支持。
用户可以自定义异常类型，异常类型并不受到限制，可以是内建数据类型如int,double等，也可以是自定义的类，也可以从C++某个异常类继承下来。例1采用了派生自exception的方法。
除此之外，在定义函数时，可以显式指定函数体抛出的异常类型。隐式情况下，缺省允许函数抛出任何类型的异常。有可以增加throw语句，对异常类型加以限制。特别的是，throw()表示不允许函数抛出任何类型的异常。如果违反了throw列表规定的异常类型，系统将调用unexpected hanlder进行处理，可以自定义unexpected异常处理方法。例2和例3对它们进行了说明。
如果对于函数体throw列表合法的异常被抛出，但是却没有被程序捕捉处理，系统将调用terminate handler进行处理。缺省情况下，只是简单调用abort()函数终止程序，同样可以自定义terminate处理方法。例4对它进行了说明。
