# Vue

[组件编写](https://www.cnblogs.com/pengfei-nie/p/9134367.html)

## vue2.0 如何自定义组件（vue组件的封装）

[转载](https://www.cnblogs.com/pengfei-nie/p/9134367.html)

## 一、前言

之前的博客聊过 vue2.0和react的技术选型；聊过vue的axios封装和vuex使用。今天简单聊聊 vue 组件的封装。

vue 的ui框架现在是很多的，但是鉴于移动设备的复杂性，兼容性问题突出。像 Mint-UI 等说实话已经很不错了，但是坑也是不少，而且项目中很多功能仅凭这些也实现不了，这需要我们去封装自己的可复用组件。

## 二、封装组件的步骤

* 1.  建立组件的模板，先把架子搭起来，写写样式，考虑好组件的基本逻辑。

* 2.  准备好组件的数据输入。即分析好逻辑，定好 props 里面的数据、类型。(后面详解)

* 3.  准备好组件的数据输出。即根据组件逻辑，做好要暴露出来的方法。（后面详解）

* 4.  封装完毕了，直接调用即可。

  接下来以一个很简单的例子具体说明一下

  现在先看一下demo的效果图

![1113254-20180604172026258-1937876034.gif](https://i.loli.net/2020/10/25/TurM3lLImpEfKao.gif)

## 三、代码详解

* 1. 先说一下 props

我们在父组件中需要将子组件需要的数据导入，用法如下：

```html
<search @selectFunc="selectFunc" :searchList="searchList" :selectValue="selectValue"></search>
```

`:searchList="searchList"`  就是我们的数据，这个可以写多个。这里我传输了2个参数过去，主要是做数据修改的说明。大家可以先忽略。

 在子组件中，我们的接收和使用方法如下：

```js
props: {
      searchList: Array,
      selectValue: Object
    },
mounted() {
      this.data = this.searchList
    },

```

我们在 props 中接收数据，注意props对象里面`键值`是对改数据的 `数据类型` 的规定。做了规范，使用者就只能传输指定类型的数据，否则报警告

而props对象中的数据，我们可以直接在当前组件中使用  this.searchList，可以直接使用。这里要强调一下，props传过来的数据只做展示，不得修改，想修改，再新写一个data中的变量承接做数据的再处理。至于原因，同上，可以看一下js的原型。至于原理嘛，不懂的可以取脑补一下 `js的原型` 。os：这些基础，在这就不做详述了。

以上就是props传递过来的数据的使用了。

* 2. emit的使用(如何暴露组件方法)

我们已经会使用 父组件向子组件传数据了，那如子组件如何来修改父组件的数据呢？

这里提供 2 种实现方法，但是 第一种不推荐，强烈不推荐

方式一：

 ```js
　　　　　selectValue: {
          data: '1'
        },
　　　　。。。。。。。。。。。。。。。

       this.selectValue.data = '我被修改了'
```

即，父组件将 对象 数据传递给子组件，子组件直接修改props过来的对象的值

可以实现，感觉是一个比较快捷的方式。但是不推荐，这种方式写多了，容易出错，特别是多层组件嵌套的时候。这种修改对代码的迭代和错误的捕捉都不友好，所以建议大家别这样写。

他的实现原理简单提一下： 这个对象、数组啦，是引用数据类型，说白了，就是存储单元的信息是指针，真正数据在别的地方，通过指针查询的数据，所以这样写，对浏览器来说仅仅是传递了一个指针，数据还是同一份数据。所以你能修改。

方式二：

正儿八经的通过 $emit 方法去掉父组件的方法，在父组件中修改data的数据。（根正苗红的方法，规范写法）

```html
// 子组件
this.$emit('selectFunc', value)
// 父组件
<search @selectFunc="selectFunc" :searchList="searchList" :selectValue="selectValue"></search>

selectFunc(value) {
        this.selectValue2 = value
        console.log(this.selectValue)
        console.log(this.selectValue2)
      }
```

　　　　将父组件的方法注入子组件  @selectFunc="selectFunc" ，然后在子组件中通过 $emit 调用他，并传递参数。达到修改的目的。

## 四、 demo代码

父组件：

```html
<template>
    <section class="f-mainPage">
        <!--selectFunc 选择完成的回调      searchList 下拉列表的数据-->
        <search @selectFunc="selectFunc" :searchList="searchList" :selectValue="selectValue"></search>
    </section>
</template>

<script type="text/ecmascript-6">
  import Search from '../vuePlugin/search'
  export default {
    data() {
      return {
        searchList: ['草船借箭', '大富翁', '测试数据'],
        // 直接通过props传递对象 修改，挺便捷的,但是不规范
        selectValue: {
          data: '1'
        },
        // 通过emit修改，规范写法
        selectValue2: ''
      }
    },
    mounted() {},
    methods: {
      pageGo(path) {
        this.$router.push('/' + path)
      },
      selectFunc(value) {
        this.selectValue2 = value
        console.log(this.selectValue)
        console.log(this.selectValue2)
      }
    },
    components: {
      Search
    }
  }
</script>

<style lang="scss" scoped>
.f-mainPage{
    width: 100%;
    .g-banner{
    width: 100%;
    background-image: url(../../../static/main_bg.png);
    background-repeat: no-repeat;
    background-size: 100% 100%;
    position: relative;
    overflow: hidden;
    color: white;
    text-align: center;
    p:nth-child(1) {
      margin: 10px auto 0px auto;
      font-size: 1.3rem;
    }
    .f-banscri {
      margin: 15px auto 8px auto;
      font-size: 0.95rem;
    }
    .f-moneyMax{
      margin: 5px auto 0px auto;
      font-size: 2.4rem;
    }
    .f-returnCash{
      width: 120px;
      height: 35px;
      text-align: center;
      line-height: 35px;
      background-color: white;
      color: #169BD5;
      display: inline-block;
      border-radius: 5px;
      font-size: 1rem;
      margin-top: 35px;
      position: relative;
      .f-mmmbd{
          position: absolute;
          width: 100%;
          height: 100%;
          background-color: transparent;
          top: 0;
          left: 0;
      }
    }
    }
    .g-cashInfor{
    width: 100%;
    text-align: center;
    display: flex;
    justify-content: space-between;
    div{
        width: 50%;
        height: 60px;
        line-height: 60px;
        box-sizing: border-box;
    }
    div:nth-child(1){
        border-bottom: 1px solid #878787;
        border-right:  1px solid #878787;
    }
    div:nth-child(2){
        border-bottom: 1px solid #878787;
    }
}
    .g-operate{
        width: 100%;
        height: auto;
        overflow: hidden;
        ul{
            list-style: none;
            padding: 0;
            margin: 0;
            font-size: 1.05rem;
            li{
                height: 60px;
                line-height: 60px;
                padding-left: 25px;
                position: relative;
                span{
                    width: 20px;
                    height: 20px;
                    position: absolute;
                    top: 20px;
                    right: 20px;  
                    background-image: url(../../../static/go.png);
                    background-repeat: no-repeat;
                    background-size: 100% 100%;
                }
            }
        }
        .f-goodNews{
            width: 340px;
            height: 144.5px;
            margin: 20px auto 30px auto;
            text-align: center;
            background-image: url(../../../static/banner.png);
            background-repeat: no-repeat;
            background-size: 100% 100%;
        }
    }
}
</style>
```

子组件：

```html
<template>
    <div class="searchZJ">
      <div class="f-search">
          <div class="f-searchIn" v-bind:class="{searchInFous: this.fousFlag}">{{this.searchValue}}<span v-bind:class="{searchActive: this.searchFlag}" v-on:click="searchDown"></span></div>
          <div class="f-searchXl" v-if="this.dataHas" v-bind:style="{height:this.searchFous, border:this.searchBorder}">
              <div v-for="item in searchList" v-on:click="choseValue(item)">{{item}}</div>
          </div>
          <div class="f-searchXl" v-else >
              <div>暂无数据</div>
          </div>
      </div>
    </div>
</template>

<script type="text/ecmascript-6">
  export default {
    data() {
      return {
        data: [],
        dataHas: true,
        searchFlag: false,
        searchFous: '0',
        fousFlag: false,
        searchValue: '',
        searchBorder: 'none'
      }
    },
    props: {
      searchList: Array,
      selectValue: Object
    },
    mounted() {
      this.data = this.searchList
    },
    methods: {
      searchDown() {
        this.searchFlag === false ? this.searchFlag = true : this.searchFlag = false
        this.searchFous === '0' ? this.searchFous = 'auto' : this.searchFous = '0'
        this.searchBorder === 'none' ? this.searchBorder = '1px solid #D9D9D9' : this.searchBorder = 'none'
        this.fousFlag === false ? this.fousFlag = true : this.fousFlag = false
      },
      choseValue(value) {
        this.searchValue = value
        this.searchDown()
        this.selectValue.data = '我被修改了'
        this.$emit('selectFunc', value)
      }
    }
  }
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
    .f-search{
        width: 250px;
        height: auto;
        position: relative;
        margin-left: 20px;
        box-sizing: border-box;
    }
    .f-searchIn{
        width: 250px;
        height: 35px;
        line-height: 35px;
        font-size: 0.95rem;
        border-radius: 5px;
        overflow: hidden;
        position: relative;
        background-color: white;
        box-shadow: none;
        box-sizing: border-box;
        color: #000000;
        padding-left: 10px;
        border: 1px solid #A3A3A3;
    }
    .searchInFous{
        border: 1px solid #57C4F6;
        box-shadow: 0px 0px 5px #57C4F6;
    }
    .f-searchIn > span{
        display: block;
        width: 28px;
        height: 28px;
        background-image: url(../../../static/upDown.png);
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-position: 0px -13px;
        position: absolute;
        top: 10px;
        right: 5px;
    }
    .f-searchIn .searchActive{
        background-position: 0px 12px;
        top: -2px;
    }
    .f-search .f-searchXl{
        position: absolute;
        width: 100%;
        height: auto;
        max-height: 220px;
        top: 41px;
        left: -1px;
        border-radius: 5px;
        /*border: 1px solid #D9D9D9;*/
        background-color: white;
        overflow-x: hidden;
        overflow-y: scroll;
    }
    .f-search .f-searchXl > div{
        height: 35px;
        line-height: 38px;
        color: #000000;
        padding-left: 25px;
        font-size: 0.92rem;
    }
    .f-search .f-searchXl > div:hover{
        background-color: #D5F1FD;
    }
</style>
```

## 五、 总结

　　这里主要是总结一下vue组件封装的思路，帮大家梳理一下。很简单，和jQuery插件、react组件一样，所有组件都是一个套路，就是 函数思想。

　　组件就是台做烤肠的机器，我放进去猪肉，再按一下各种开关，然后你给我烤肠。

　　　　1. 定义好 你需要使用者传入的数据

　　　　2. 定义好 你提供给使用者的方法

　　　　3. 写好组件的内部逻辑

这就OK了，一个完美的，可复用的组件就完成了。    os： 在此吐槽一下，那些自认为是优秀的组件，其实，别人拿着是没法用的。 o(╥﹏╥)o

os： 愿大家工作过程中能规范编程习惯，一起为前端代码大社区做贡献。

## 注

os:  2018/06/06

　　鉴于一些朋友的评论，我在这再做一些解答哈，这个言论往深了去不保证准确性，我尽量吧。有问题的地方还是希望大家及时指出。

　　1.  父子组件通信的方式，远不止我说的那两种。但是，通过 $emit 的方式是根正苗红的，不带任何差错的，是封装优秀组件最好的方式()

* （1） 通过ref 通信

父组件设置ref，通过$refs对象来获取子组件的数据

```html
<search ref="refTest3" ></search>
.......
console.log(this.$refs.refTest3)
console.log(this.$refs.refTest3.selectValue.data)
```

其实，很简单。ref 就是直接获取了你的dom节点，如果是div一类的基本dom和js的document.getElementsByTagName()效果一样的，而且这样节省开销。你可以在父组件中直接 this.$refs.refTest3.selectValue.data。直接获取子组件data中的数据，或者别的数据都可以获取。但是，这个不是我们封装组件会用的东西，因为这个用在父组件。组件的思想是 独立的。所以，大家平时用用就好了，如果要封装可复用的组件，这个还是不实用的。  os：可能他有特殊用法是我不清楚的，如果有请大家分享

* （2）通过 vuex 通信

vuex 大家都知道，变量统一管理(方便的很)，╮(╯▽╰)╭  但是用这个来封装组件的完全就是抬杠了。vuex、redux等等这些都是针对组件多层传输数据不便，而做的状态统一管理，说白了是针对大家都要用的数据才会放到vuex中，而组件思想，是封装一个独立的、可复用的功能模块。这根本就是2个理念。希望大家不要被误导。

* （3）.aync 父子组件数据双向绑定

说实话，这也是来抬杠的。说白了，双向绑定不还是 通过  $emit 监听数据更新事件，来调用父组件的方法吗？

这里简单说一下这个数据双向绑定的，还是很常用的方法。不啰嗦，看代码：

```html
<search @selectFunc="selectFunc" :syncTest.sync="syncTest"></search>
.........

this.$emit('update:syncTest', value)
```

其实，很简单。在父组件向子组件props数据的时候，加一个  .sync  修饰符，然后在子组件显示的调用 emit 来修改他。   说白了就是添加这样的一个事件绑定  @update:foo="val => bar = val">

上述的方法就是  父子组件数据双向绑定。子组件实时修改  props 的方法。

欢迎大家提出别的问题和建议
