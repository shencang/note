# Vue（结合springboot版）

## Vue 入门

### 1. [官方入门](https://cn.vuejs.org/)

### 2. [element](https://element.eleme.cn/#/zh-CN/component/carousel)

### 3. [vue-cli 3.x 配置Axios(proxyTable)跨域代理](https://www.cnblogs.com/focusoldman/p/10281293.html)

### 4.[vue.config.js 配置](https://www.jianshu.com/p/b358a91bdf2d)

### 5.[白卷-项目实战教程](https://blog.csdn.net/Neuf_Soleil/article/details/88925013)

## Vue-全局变量和方法

### 一、单文件引入

#### 1、创建存放全局变量和方法的vue文件

```js
<script>
  const userName = 'yangjing';
  function add(a,b) {
    return a+ b
  }
  export default {
    userName,
    add
  }
</script>
```

#### 2、在需要使用的组件（A组件和B组件）中引入Common.uve

```js
<template>
  <div>
    <h2 @click="changeName">{{name}}</h2>
    <h2 @click="add">3+6 = {{num}}</h2>
  </div>
</template>

<script>
  import Common from '@/components/Common'
  export default {
    name: "Details",
    data () {
      return {
        name: Common.userName,
        num: ''
      }
    },
    methods: {
      add() {
        this.num = Common.add(3,6)
      }
    }
  }
</script>
```

```t
在A组件中修改全局变量userName时在B组件中可以看到userName是更新了的
```

### 二、全局引入 全局变量模块挂载到vue原型中

```t
如果再项目中在多个地方使用全局变量和方法用第一种方式引入肯定是相当繁琐的，因为需要在使用的地方都要引入一次；那么为了提高效率现在在main.js中引入一次然后挂载到vue原型上（Vue.portotype）
```

#### 1、在main.js中引入文件，并挂载到Vue原型上

```js
import Common from '@/components/Common'
Vue.prototype.Common = Common;
```

#### 2、在需要使用的组件中使用 this

```js
<template>
  <div>
    <h2 @click="changeName">{{name}}</h2>
    <h2 @click="add">3+6 = {{num}}</h2>
  </div>
</template>

<script>
  export default {
    name: "Details",
    data () {
      return {
        name: this.Common.userName,
        num: ''
      }
    },
    methods: {
      add() {
        this.num = this.Common.add(3,6)
      }
    }
  }
</script>
```

``拓展：``

### 三、使用Vue中的状态管理Vuex

```t
如果数据量小则不推荐使用Vuex，杀鸡就不用宰牛刀了吧。
```

[详细使用](https://www.cnblogs.com/yangchin9/p/11003791.html)

### 四、使用本地存储（webstorage）存放全局变量

本地存储分两种 ``localStorage`` 和 ``sessionStorage``

``localStorage``：永久性，一直存在于浏览器中，除非用户手动清除localStorage；一般为5M浏览器不同有些许区别；不参与和服务器的通信。

``sessionStorage``：在当前会话下有效，关闭页面和浏览器清除后失效；一般为5M浏览器不同有些许区别；不参与和服务器的通信。

* API：二者的api形式相同

```js
localStorage.setItem("key","value");  //以“key”为名称存储一个值“value”

localStorage.getItem("key");  //获取名称为“key”的值

localStorage.removeItem("key");  //删除名称为“key”的信息。

localStorage.clear();  ​//清空localStorage中所有信息
```

### 五、使用Cookie存储

```t
这种方式极不推荐，毕竟大小限制，还需要设置过期时间。
cookie在过期时间之前一直有效即使窗口或浏览器关闭；存放数据大小为4k左右；有个数限制（随浏览不同）一般不能超过20个；与服务端通信，每次都会携带在HTTP头中，如果使用cookie保存过多数据会带来性能问题。
```

[参考链接](https://www.cnblogs.com/yangchin9/p/11002636.html)
