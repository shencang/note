# Markdown
### MarkDown添加图片的三种方式

插图最基础的格式就是：

    ![Alt text](图片链接 "optional title")


Alt text：图片的Alt标签，用来描述图片的关键词，可以不写。最初的本意是当图片因为某种原因不能被显示时而出现的替代文字，后来又被用于SEO，可以方便搜索引擎根据Alt text里面的关键词搜索到图片。 图片链接：可以是图片的本地地址或者是网址。"optional title"：鼠标悬置于图片上会出现的标题文字，可以不写。

插入本地图片
只需要在基础语法的括号中填入图片的位置路径即可，支持绝对路径和相对路径。
例如：

     ![avatar](/home/picture/1.png)


不灵活不好分享，本地图片的路径更改或丢失都会造成markdown文件调不出图。

插入网络图片
只需要在基础语法的括号中填入图片的网络链接即可，现在已经有很多免费/收费图床和方便传图的小工具可选。
例如：

     ![avatar](http://baidu.com/pic/doge.png)


将图片存在网络服务器上，非常依赖网络。

把图片存入markdown文件
用base64转码工具把图片转成一段字符串，然后把字符串填到基础格式中链接的那个位置。

基础用法：

        ![avatar](data:image/png;base64,iVBORw0......)
这个时候会发现插入的这一长串字符串会把整个文章分割开，非常影响编写文章时的体验。如果能够把大段的base64字符串放在文章末尾，然后在文章中通过一个id来调用，文章就不会被分割的这么乱了。
高级用法
比如：

        ![avatar][base64str]
        [base64str]:data:image/png;base64,iVBORw0......

最后，base64的图片编码如何得来？

使用python将图片转化为base64字符串
```python
import base64
f=open('723.png','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(ls_f)

```


base64字符串转化为图片
```python
import base64
bs='iVBORw0KGgoAAAANSUhEUg....' # 太长了省略
imgdata=base64.b64decode(bs)
file=open('2.jpg','wb')
file.write(imgdata)
file.close()
```
[Form](https://www.jianshu.com/p/280c6a6f2594)

