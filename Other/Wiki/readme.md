## Wiki语法快速参考

    ----       = 创建水平线.

    \\         = 换行, \\\=force line break and clear.

    [link]     = 创建一个链接，指向内部的wiki页面'Link'.

    [this is also a link] = 创建一个链接，指向内部的wiki页面'ThisIsAlsoALink'.

    [click here|link] = 创建一个链接，指向内部的wiki页面'Link', 链接文字是'click here'.

    [1]        = Makes a reference to a footnote numbered 1.

    [#1]       = Marks the footnote number 1.

    [[link]    = 不创建链接而是输出文字'[link]'.

    !heading   = 小号标题

    !!heading  = 中号标题

    !!!heading = 大号标题

    ''text''   = 将text斜体.

    __text__   = 将text粗体.

    {{text}}   = prints 'text' in monospaced font.

    * text     = 无符号列表
    
    # text     = 有符号列表
    ;term:ex   = 名词定义，用'ex'定义名字'term'

## 文字相关语法

在写wiki页面时可以不懂任何wiki语法，只需要像写信那样写自己的wiki页面，用空行来分割不同的段落，这样输出的页面跟你输入时的格式是类似的.

### 标题'!'

    !text    = 用于定义小号标题
    
    !!text   = 用于定义中号标题
    
    !!!text  = 用于定义大号标题

除了用于定义页面输出样式，标题还有两个增值用法

### 书签

    所有标题都会自动生成一个页面书签, 这样我们可以在其他页面定义一个链接到这个页面某个书签的链接. 举例, 在本页有下面这样的标题，
    
    !!This is my heading
    
    那么生成的HTML代码将如下，
    
    This is my heading
    
    在其他页面可以通过如下文字链接到这个书签，

    [TextFormattingRules#ThisIsMyHeading]
    or [Bookmark Text|TextFormattingRules#ThisIsMyHeading]

### 生成索引和目录

Table Of Contents Plugin  将会把标题生成对应的索引和目录

### 无符号列表'*'

    '*'生成无符号列表，多个'*'生成多级无符号列表. 举例:
    * One
    * Two
    * Three
    ** Three.One
生成列表如下

    One
    Two
    Three
    Three.One

### 有符号列表'#'

类似无符号列表, 只是使用'#'. 举例如下:
    # One
    # Two
    # Three
    ## Three.One
生成列表如下

    One
    Two
    Three
    Three.One

### 名词定义与注释';:'

';term:ex'用于名词定义，名词construct的定义举例如下:

    ;__Construct__:''Something you use to do something with''
    将生成如下格式，
    Construct
    Something you use to do something with
    term为空时用于生成注释，举例如下:
    
    ;:''Comment here.''
将生成如下格式，
    Comment here.
    文字效果（粗体和斜体）
    __text__      生成粗体文字
    ''text''      生成斜体文字
    预格式化文本(Preformatted text)
三个'{'可以起到HTML标签里PRE的作用，这个功能在输出程序代码等文字时会非常有用.

### 在Wiki页面里添加图片

#### Inlined Image

    最简单的方式是使用Inlined Image，写法和一般的链接写法类似，举例:[http://image15.360doc.com/DownloadImg/2010/09/1917/5404160_1.png]可显示图片http://image15.360doc.com/DownloadImg/2010/09/1917/5404160_1.png
    
    也可以为图片指定ALT时的文字，格式为[this one here|http://example.com/example.png]. 例如[Hello All|http://image15.360doc.com/DownloadImg/2010/09/1917/5404160_1.png]显示结果:Hello All
    
    图片可以位于Web上任意可以访问的位置，也可以是某个页面的附件，显示时使用不同的链接地址就行，譬如完整URL(http://example.com/example.png)或者附件URL(WikiPage/AttachmentName).
    
    Inline Image有一个局限，就是只支持特定类型的图片格式，JSPWiki默认支持的图片格式是PNG，我们也可以修改配置文件jspwiki.properties来配置支持的图片类型，配置格式举例如下:
    
    jspwiki.translatorReader.inlinePattern.1 = *.jpg
    
    jspwiki.translatorReader.inlinePattern.2 = *.png
    
    当前JSPWiki支持的Inline Image的格式可以参考SystemInfo.
    Image Plugin
    Inline Image使用简单，但没有格式控制，图片类型也受限制，另一种输出图片的方法是使用Plugin机制，具体用法参考Image Plugin.

### 创建超级链接

基本应用

    语法: [Like this] or [Like this|link]
    
    link可以是某个wiki页面, 例如[Rain Zhao]或[link sample to page Rain Zhao|RainZhao].
    
    link也可以是一个完整的URL, 链接地址以下面的协议开头的将被视为外部链接, http:, ftp:, mailto:, https:, or news:. 举例, 语句 [http://java.sun.com], 将显示 http://java.sun.com/, 语句 [Java home page|http://java.sun.com], 将显示 Java home page.

### 页脚注释(Footnotes)

超链地址使用数字将创建一个Footnote, 例如 footnote[1], 将创建footnote[1], 也可以命名一个footnote, 格式与命名一个普通超链一样. 例如 [Footnote number 1|1]将生成[Footnote number 1], 这是另一个 footnote[2].

使用 [#1] 定义footnote, 也可以使用[footnote 1|#1]定义footnote, 上文的两个footnote定义在本页最后.

InterWiki

我们还可以定义一个超链链接到其他wiki里的某个页面. 系统里支持哪些InterWiki是在配置文件里配置的, 配置格式举例如下:

    jspwiki.interWikiRef.JSPWiki = http://www.jspwiki.org/Wiki.jsp?page=%s
    jspwiki.interWikiRef.Edit = Edit.jsp?page=%s
    jspwiki.interWikiRef.WikiWikiWeb = http://c2.com/cgi/wiki?%s
    jspwiki.interWikiRef.Google = http://www.google.com/search?q=%s
应用举例如下:

    [TextFormattingRules on JSPWiki.org|JSPWiki:TextFormattingRules]
    [Edit:TextFormattingRules]
    输入如下:TextFormattingRules on JSPWiki.org, Edit:TextFormattingRules
    InterWiki其实就是输出替换, 通过InterWiki机制我们除了链接其他wiki页面, 还可以实现一些有趣的功能, 譬如实现在新窗口里打开链接:
    
    首先在jspwiki.properties里加入如下配置：
    
    jspwiki.interWikiRef.newhttp=http:%s" TARGET="_new
    jspwiki.interWikiRef.new = Wiki.jsp?page=%s" target="_new
    然后我们在写wiki页面时，就可以选择是否在新窗口里打开新页面了，
    [Foster Schucker]  -- open this wiki page in this window
    [new:Foster Schucker] -- open this wiki page in a new window
    [http://www.jspwiki.org] -- open this external link in this window
    [newhttp://www.jspwiki.org]] -- open this external link in a new window
    在 SystemInfo 里列出了可用的wiki.

### 表格相关语法

使用管道符号('|')生成表格. 使用双管道符号生成表格标题. 举例:

    || Heading 1 || Heading 2
    | ''Gobble'' | Bar
    | [Main]     | [SandBox]

### 使用CSS样式表

    Hi there!
    这是一个使用CSS样式表的示例. 这里使用了样式 "commentbox", 样式定义在 "jspwiki.css" 文件里. 使用格式为 %%commentbox %%.
    我们可以使用CSS样式来输出丰富的字体颜色等各种效果，CSS可以是jspwiki.css已经定义好的样式，也可以自己定义的样式，下面是使用标准样式定义的示例:
    %%small
    This is small text
    %%
    样式 "small" 必须在文件 jspwiki.css 里定义. 这种用法要求wiki页面作者清楚管理员提供了哪些CSS样式, 提供的CSS样式在各个站点可能是不同的.
下面是使用自己定义的CSS样式:

    %%( font-size: 150%; color: red; )
    Hello, world!
    %%
    输出如下:
    Hello, world!
    使用变量
    在JSPWiki里，有一些系统定义好的或者用户自定义的变量，我们可以在自己的Wiki页面里读取并显示这些变量. 基本格式为: [{$variablename}]
    除了在页面里显示一个已有变量, 还可以在页面里使用SET定义页面变量, 基本格式为: [{SET name=value}]
    
    JSPWiki Variables介绍了关于变量的详细信息, JSPWiki MetaData介绍了SET的详细用法.

注意: 变量名是不区分大小写的, "paGeNamE" 与 "PageName" 表示相同的变量.

### 使用Plugin

使用Plugin的基本格式如下:

    [{INSERT <plugin class=""></plugin> WHERE param1=value, param2=value, ...}]

    JSPWiki Plugins详细介绍了Plugin的用法.