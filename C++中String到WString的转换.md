# C++中String到WString的转换
W顾名思义就是Width的缩写，即所谓的“宽”。

首先看一下wstring和string分别如何定义的：

typedef basic_string<char, char_traits<char>, allocator<char> >string;

typedef basic_string<wchar_t, char_traits<wchar_t>, allocator<wchar_t> >wstring;
1
2
3
从上面的代码可以看出，二者的区别就是在于wchar_t和char的区别： 
wchar_t是Unicode字符的数据类型，它实际定义在

wchar_t *szTest=L"This is a Unicode string."
1
先介绍几个函数吧！ 
MultiByteToWideChar 
作用：该函数映射一个字符串到一个宽字符（unicode）的字符串。由该函数映射的字符串没必要是多字节字符组。 
语法：
 
```c++
int MultiByteToWideChar(
  _In_      UINT   CodePage,
  _In_      DWORD  dwFlags,
  _In_      LPCSTR lpMultiByteStr,
  _In_      int    cbMultiByte,
  _Out_opt_ LPWSTR lpWideCharStr,
  _In_      int    cchWideChar
);
```
参数： 
CodePage：指定执行转换的字符集，这个参数可以为系统已安装或有效的任何字符集所给定的值。你也可以指定其为下面的任意一值： 
CP_UTF8：使用UTF-8转换。

dwFlags：一组位标记用以指出是否未转换成预作或宽字符（若组合形式存在），是否使用象形文字替代控制字符，以及如何处理无效字符。

lpMultiByteStr：指向将被转换字符串的字符。

cchMultiByte：指定由参数lpMultiByteStr指向的字符串中字节的个数。如果lpMultiByteStr指定的字符串以空字符终止，可以设置为-1（如果字符串不是以空字符中止，设置为-1可能失败，可能成功），此参数设置为0函数将失败。

lpWideCharStr：指向接收被转换字符串的缓冲区。

cchWideChar：指定由参数lpWideCharStr指向的缓冲区的宽字符个数。若此值为零，函数返回缓冲区所必需的宽字符数，在这种情况下，lpWideCharStr中的缓冲区不被使用。

返回值：如果函数运行成功，并且cchWideChar不为零，返回值是由lpWideCharStr指向的缓冲区中写入的宽字符数

str.c_str() 
语法：

const value_type *c_str( ) const;
1
作用：为名为的字符串中的 C 样式版本的指针。指针值。调用非为 Const 函数后包括无效，析构函数，在对象的 basic_string 的类。

因此呢，我们就可以得到由string转wstring的函数StringToWString

```c++
std::wstring StringToWString(const std::string& str) {
    int num = MultiByteToWideChar(CP_UTF8, 0, str.c_str(), -1, NULL, 0);
    wchar_t *wide = new wchar_t[num];
    MultiByteToWideChar(CP_UTF8, 0, str.c_str(), -1, wide, num);
    std::wstring w_str(wide);
    delete[] wide;
    return w_str;
}
```
