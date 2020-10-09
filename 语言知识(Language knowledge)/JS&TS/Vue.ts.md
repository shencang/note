# Vue.ts

[引用文章](https://blog.csdn.net/duola8789/article/details/103979022?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduend~default-1-103979022.nonecase&utm_term=ts%E5%A6%82%E4%BD%95%E5%AE%9A%E4%B9%89vue%E4%B8%AD%E7%9A%84data&spm=1000.2123.3001.4430)

[markdown文件生成目录的方式](https://www.jianshu.com/p/b0a18eb32d09)

[实用帖 | 如何为 Markdown 文件自动生成目录？](https://www.jianshu.com/p/4721ddd27027)

## Vue-CLI支持

Vue-CLI内建了TypeScript工具支持，在新建项目时可以选择使用TypeScript扩展，包括了针对Vue Core的官方类型声明，还包括了Vue Router和Vuex提供了相应的声明文件

使用Vue-CLI会自动创建`tsconfig.json`文件，基本上使用默认的配置文件就可以满足要求。

## 改造组件

使用TypeScript编写Vue单文件组件有两种方式，一种是通过`Vue.extend()`方法，另一种是基于类的Vue组件（在使用Vue-CLI创建项目的时候可以选择），我选择使用了后者，可以提供更优雅、更类似于JSX的书写体验。

需要安装[vue-class-component](https://github.com/vuejs/vue-class-component)用来将Vue组件改写为基于Class的形式，也可以选择使用[vue-property-decorator](https://github.com/kaorun343/vue-property-decorator)，后者依赖于前者，而且提供了额外的装饰符，让编写更简单。

使用的时候，将原来导出的类型由对象改为了Class，并且使用`@Component`装饰符，如果有要引入的其他子组件，也放到`@Component`中。

```ts
@Component({
  components: {
    Child
  }
})
export default class HelloVue extends Vue {
  // 组件内容
}
```

要注意，虽然使用了`export default`，但是Class的名字还是最好准确定义，这样便于IDE和Lint工具进行追踪、提示。

### 组件属性顺序

没有发现Lint和Prettier规则来强制规定组件内的属性顺序，所以约定好一个书写顺序，作为最佳实践

要注意，组件引用、Mixin和Filters都放到了组件外部。总体的顺序分为了三部分：

数据（ `Inject` → `Prop` → `Data` → `Computed` → `Model` → `Vuex-State` → `Vuex-Getter` → `Proivde` ）
方法（Vuex-Mutation → Vuex-Action → Methods → Watch）
钩子函数（生命周期钩子 → 路由钩子）
完整的组件如下，具体写法后面单独列出来（不包含Mixin）：

```ts
@Component({ components: { Child } })
export default class App extends Vue {
  // 数据 (Inject → Prop→ Computed → Model → Vuex-State → Vuex-Getter → Proivde)
  // 使用祖先组件注入的数据
  @Inject() readonly value1!: string;
  
  // 组件的 Data
  value = 'hello';
  
  // 父组件传入 Prop
  @Prop(Number) readonly value2!: number;
  
  // 计算属性
  get value3(): string {
    return this.value1;
  }
  
   // 定义 组件的 Model 属性
  @Model('change', { type: Boolean, default: false }) checked!: boolean;
  
  // Vuex Store 中定义的 state，作为计算属性定义在组件内
  @State value4!: string;
  
  // Vuex Store 中定义的 getter，作为计算属性定义在组件内
  @Getter value5!: string;
  
  // 为子孙组件提供数据
  @Provide() root = 'Root';
  
  /* ----------------------------------------------- */
  // 方法 (Vuex-Mutation → Vuex-Action → Methods → Watch)
  // Vuex Store 中定义的 Mutation，作为方法定义在组件内
  @Mutation(UPDATE_TITLE_MUTATION) updateTitle!: (payload: { title: string }) => void;
  
  // Vuex Store 中定义的 Action，作为方法定义在组件内
  @Action(UPDATE_TITLE_ACTION) updateTitleSync!: () => void;
  
  // 组件内的 Method
  get foo(): string {
    return this.isCollapse ? 'collapsed-menu' : 'expanded-menu';
  }
  
  // 组件内的 Watch
  @Watch('value1', { immediate: true, deep: true })
  onDataChanged(newVal: string, oldVal: string): void {
    this.foo();
  }
  
  /* ----------------------------------------------- */
  // 钩子函数 (生命周期钩子 → 路由钩子)
  beforeCreated()
  
  created()
  
  beforeMount()
  
  mounted() {}
  
  beforeUpdate() {}
  
  updated(){}
  
  activated(){}
  
  deactivated(){}
  
  beforeDetory(){}
  
  destoryed(){}
  
  errorCaptured(){}
  
  beforeRouteEnter(){}
  
  beforeRouteUpdate(){}
  
  beforeRouteLeave(){}
}
```

## 相关API

### Data

直接在Class定义即可（实际上就是[Class的新语法](https://es6.ruanyifeng.com/#docs/class#%E5%AE%9E%E4%BE%8B%E5%B1%9E%E6%80%A7%E7%9A%84%E6%96%B0%E5%86%99%E6%B3%95)，与在Class的`constructor`中定义相同）

```ts
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
export default class YourComponent extends Vue {
  msg: number = 123;
}
```

### 计算属性

计算属性采取使用`getter`的形式定义，在Class内部可以使用`get`和`set`关键字，设置某个属性的存值函数和取值函数：

```ts
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
export default class YourComponent extends Vue {
  num: number = 1;
  
  get: value: string() {
    return this.num + 1;
  }
}
```

同时定义`set`实现了对计算属性的赋值。

### @Prop

@Prop接受的参数就是原来在Vue中`props`中传入的参数

```ts
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
export default class YourComponent extends Vue {
  @Prop(Number) readonly propA: number | undefined
  @Prop({ default: 'default value' }) readonly propB!: string
  @Prop([String, Boolean]) readonly propC: string | boolean | undefined
}
```

### @PropSync

`@PropSync`与`Prop`类似，不同之处在于`@PropSync`会自动生成一个计算属性，计算属性的`getter`返回传入的Prop，计算属性的`setter`中会执行Vue中提倡的更新Prop的`emit:updatePropName`

```ts
import { Vue, Component, PropSync } from 'vue-property-decorator'

@Component
export default class YourComponent extends Vue {
  @PropSync('name', { type: String }) syncedName!: string
}
```

相当于：

```ts
export default {
  props: {
    name: {
      type: String
    }
  },
  computed: {
    syncedName: {
      get() {
        return this.name
      },
      set(value) {
        this.$emit('update:name', value)
      }
    }
  }
```

使用时需要配合`.sync`修饰符使用（即在组件上定义对应的更新方法）：

```ts
<hello-sync :my-prop.sync="syncValue" />
<!-- 相当于 -->

<hello-sync :my-prop="syncValue" @update:name="(name) => syncValue = name" />
```

### 定义方法

定义方法与Data类型，直接在Class中定义方法即可：

```ts
@Component
export default class HelloChild extends Vue {
  sayHi(): string {
    return 'hello'
  }
}
```

### @Watch

使用`@Watch`定义侦听器，被装饰的函数就是侦听器执行方法：

```ts
@Component
export default class HelloChild extends Vue {
  @Watch('msg', { immediate: true, deep: true })
  onMsgChanged(newVal: string, oldVal: string): void {
    this.oldMsg = oldVal;
  }
}
```

### @Emit

想要触发父组件中定义在组件实例上的方法，需要使用`@Emit`装饰符。`@Emit`接受一个参数，是要触发的事件名，如果要出发的事件名和被装饰的方法同名，那么这个参数可以省略。`@Emit`返回值就是传递给事件的参数。

```ts
@Component
export default class HelloChild extends Vue {
  @Emit()
  sayHi(): string {
    return 'hello'
  }
  
  @Emit('go')
  goHere(): string {
    return 'gogogo'
  }
}
```

相当于：

```ts
export default {
  sayHi() {
    this.$emit('sayHi', 'hello')
  },
  
  goHere() {
    this.$emit('go', 'gogogo')
  }
}
```

### @Model

一般用来在自定义的组件上使用`v-model`，自定义组件中包含可交互元素（例如`<input>`或者`<checkbox>`），当组可交互元素绑定的值发生变化（`oninput`、`onchange`）时，会传递到父组件绑定的`v-model`属性上。

关于自定义组件`v-model`的介绍可以参考[官方文档](https://cn.vuejs.org/v2/guide/components-custom-events.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E7%BB%84%E4%BB%B6%E7%9A%84-v-model)。

```ts
<template>
  <el-checkbox :checked="checked" @change="changeHandler" />
</template>

<script lang="ts">
import { Component, Vue, Model, Emit } from 'vue-property-decorator';

@Component
export default class HelloVModel extends Vue {
  @Model('change', { type: Boolean, default: false }) checked!: boolean;

  @Emit('change')
  changeHandler(checked: boolean) {
    return checked;
  }
}
</script>
```

使用的时候：

```ts
<hello-v-model v-model="componentVModel" />
```

自定义组件利用了@Model，定义了checked属性，并且利用了@change事件，当checkbox发生了change事件后，父组件中的componentVModel就会随之发生变化。

实际上Modal和.sync修饰符都是Vue为了方便子组件同步数据到父组件而实现的语法糖

### @Ref

当使用`ref`属性标记一个子组件或者HTML元素的时候，需要使用`@Ref`修饰符来找到标记的组件或元素。例如：

```ts
<div ref="someRef"></div>
<hello-ref ref="hello" />
```

如果我们需要获取`ref`引用时：

```ts
import { Component, Vue, Watch, Ref } from 'vue-property-decorator';
import HelloRef from '@/views/baseKnowledge/hello-vue/components/HelloRef.vue';

@Component({
  components: {
    HelloChild,
    HelloSync,
    HelloVModel,
    HelloRef
  }
})
export default class HelloVue extends Vue {
  @Ref() readonly hello!: HelloRef;
  @Ref() readonly someRef!: HTMLDivElement;
}
```

`@Ref`后面跟的参数就是对应的`ref`的值，需要为其指定类型，如果是原生的元素，可以使用对应的与内置原生元素类型，如果是自定义组件，那么可以将引入的组件作为类型

如果在`HelloRef`中定义了一个`notify`方法，我们就可以按照如下调用：

```ts
this.hello.notify()
```

但是现在应该是Vue-Cli内置的Vue类型系统有一个Bug，始终会报如下的错误：

```ts
Error:(141, 16) TS2551: Property 'notify' does not exist on type 'Vue'. Did you mean '$notify'?
```

我的处理方法时，在为`hello`定义类型时，手写类型，传入我们需要的方法类型就OK了

```ts
@Ref() readonly hello!: { notify: (from?: string) => {} };
```

### Mixins

`vue-property-decorator`的`Mixins`方法完全来源于`vue-class-component`，使用方法如下。首先创建一个Mixin：

```ts
// visible-control-mixin.ts
import Vue from 'vue';
import Component from 'vue-class-component';

@Component
export default class MyMixin extends Vue {
  visible = false;

  get buttonText(): string {
    return this.visible ? 'Close' : 'Open';
  }

  toggleVisible() {
    this.visible = !this.visible;
  }
}
```

然后在组件中引入，这时候我们就不再需要组件继承自`Vue`了，而是继承自Mixin后的组件，`Mixins`方法可以接受个参数，作为混入的Mixin：

```ts
import { Component, Mixins } from 'vue-property-decorator';
import VisibleControlMixin from '@/mixins/visible-control-mixin';

@Component
export default class MixinExample extends Mixins(VisibleControlMixin) {}

```

### @Inject/@Provide

`provide`和`inject`主要的目的就是透传属性，从一个根节点`provide`一个属性，无论多远的一个子节点都可以通过`inject`获得这个属性，与React的Context特性非常类似

虽然可以通过使用这两个属性，实现全局的数据共享，但是Vue的文档提示，这两个属性主要为高阶插件和组件库提供用例，并不直接推荐用于应用程序代码中，所以简单了解即可。

在根组件中使用`@Provide`提供数据：

```ts
import { Component, Vue, Provide } from 'vue-property-decorator';
import Child from '@/views/baseKnowledge/inject-provide/components/Child.vue';

@Component()
export default class InjectProvide extends Vue {
  @Provide() root = 'Root';
  @Provide('parent') readonly parentValue = 'Grandpa';

  // 相当于
  //  provide() {
  //   return {
  //     root: 'Root Initial Value',
  //     parent: this.parentValue
  //   }
  // }
}
```

在子组件中使用`@Inject`获取数据：

```ts
import { Component, Vue, Inject } from 'vue-property-decorator';

@Component()
export default class InjectProvideChild extends Vue {
  @Inject() readonly root!: string;
  @Inject() readonly parent!: string;
}
```

要注意，`provide`和`inject`绑定并不是可响应的。这是刻意为之的。然而，如果传入了一个可监听的对象，那么其对象的属性还是可响应的。

`vue-property-decorator`也提供了响应式插入数据的装饰器`@ProvideReactive`和`@InjectReactive`，但是有两个问题：

无法与`@Inject`/`@Provide`在同一个组件中同时工作
当从一个其他组件跳转到使用了`@ProvideReactive`和`@InjectReactive`后，会很有大概率报错`Error in nextTick: "TypeError: Cannot redefine property: parent"`导致渲染出错
所以暂时不推荐使用这两个装饰器。

## 改造Vue Router

使用Vue CLI创建的TypeScript项目，Vue Router与TypeScript配合基本不再需要进行额外的处理，除了对组件内的路由钩子方法需要提前进行注册。

使用`vue-class-component`提供的`Component.registerHooks`方法来提前注册，要注意，注册需要在引入路由之前完成

```ts
// ./src/components/class-component-hooks.ts

// 在此注册其他插件提供的钩子函数，用来在 Vue Class 组件中使用
// 例如 Vue Router 提供的钩子函数
// 必须在 router 之前引入
import Component from 'vue-class-component';

// Register the router hooks with their names
Component.registerHooks(['beforeRouteEnter', 'beforeRouteLeave', 'beforeRouteUpdate
```

在`main.ts`中引入：

```ts
import '@/components/class-component-hooks';
import router from './router';
```

## 改造VueX

Vuex与TypeScript配合会复杂一些，并且体验也不算太好，需要安全额外的包实现与TypeScript的配合使用，有三种方案来帮助我们使用TypeScript版本的Vuex

### 使用vue-class-component

第一种方案是使用`vue-class-component`配合以前常常使用`mapState`等帮助方法：

```ts
import { Component, Vue } from 'vue-property-decorator';
import { mapState, mapMutations } from 'vuex'

@Component(
  {
    // Vuex's component binding helper can use here
    computed: mapState(['count']),
    methods: mapMutations(['increment'])
  }
)
export default class App extends Vue {
  // additional declaration is needed
  // when you declare some properties in `Component` decorator
  count!: number
  increment!: () => void
}
```

这种方式的好处是可以通过`mapState`等方法将Store中定义的数据、方法一次性引入组件，确定就是这种『一次性』其实也还需要在组件内部再次定义，并且如果采用这种形式配合`vue-property-decorator`使用时，会将计算属性、方法等逻辑打乱。另外，通过这种方式调用Mutation和Action，也不是类型安全的（即没有办法校验我们传入的参数是否与Store中定义的`payload`类型相匹配

### 使用vuex-class

第二种方案是vuex-class，它与上一种方案相同，并没有对Vuex的Store中的代码进行改造，而是在组件消费Store中的数据、方法时，提供了一些遍历的API，简化使用方法

```ts
import { Component, Vue } from 'vue-property-decorator';
import {
  State,
  Getter,
  Action,
  Mutation,
  namespace
} from 'vuex-class'

const someModule = namespace('path/to/module')

@Component
export class MyComp extends Vue {
  @State('foo') stateFoo
  @State(state => state.bar) stateBar
  @Getter('foo') getterFoo
  @Action('foo') actionFoo
  @Mutation('foo') mutationFoo
  @someModule.Getter('foo') moduleGetterFoo

  // If the argument is omitted, use the property name
  // for each state/getter/action/mutation type
  @State foo
  @Getter bar
  @Action baz
  @Mutation qux

  created () {
    this.stateFoo // -> store.state.foo
    this.stateBar // -> store.state.bar
    this.getterFoo // -> store.getters.foo
    this.actionFoo({ value: true }) // -> store.dispatch('foo', { value: true })
    this.mutationFoo({ value: true }) // -> store.commit('foo', { value: true })
    this.moduleGetterFoo // -> store.getters['path/to/module/foo']
  }
}
```

注意，给`namespace`传入的参数是Vuex中`module`的命名空间，并非模块的目录路径

这种方法虽然不能使用`mapState`等辅助函数，但是好在使用`@State`等装饰符集中导入，也还算清晰明了。但是缺点仍然是没有办法完全进行类型安全的Mutation和Action调用

### 使用vuex-module-decorators

如果想要实现获得完全类型安全的Vuex，那么就需要使用`vuex-module-decorators`，它对Vuex的Store也进行了Class化的改造，引入了`VuexModule`和@Mutation等修饰符，让我们能够使用Class形式来编写Store

使用的时候，按照下面的形式来改写Store：

```ts
import { Module, Mutation, Action, VuexModule } from 'vuex-module-decorators';
import store from '@/store';
import { setTimeoutThen } from '@/utils';

@Module({ dynamic: true, namespaced: true, store, name: 'testStore' })
export default class TestStore extends VuexModule {
  // state
  message: string = '';

  get UpperMessage() {
    return this.message;
  }

  @Mutation
  UPDATE_MESSAGE_MUTATION(title: string): void {
    this.message = title;
  }

  @Action
  async UPDATE_MESSAGE_ACTION(): Promise<string> {
    const result: string = await setTimeoutThen(1000, 'ok');
    this.context.commit('UPDATE_MESSAGE_MUTATION', result);
    return result;
  }
}
```

要注意，改写的Module在`@Module`中传入了几个属性，传入`namesapced`和name来使用Module成为命名空间下的模块，此外还需要传入`dynamic`，让这个模块成为动态注册的模块，同时还需要将完全空白的`store`传入给这个模块

完成改造之后，在使用的时候就可以使用他提供的`getModule`方法获得类型安全了，使用方法：

```ts
import { getModule } from 'vuex-module-decorators';
import TestStore from '@/store/modules/testStore';

const testStore = getModule(TestStore);
testStore.message;
testStore.UPDATE_MESSAGE_MUTATION('Hello');
testStore.UPDATE_MESSAGE_ACTION();
```

### 最终选择vuex-class

我选择了使用第二种方案，相比于第一种方案能够将组件内的逻辑几种，并且通过相关的修饰符能够显示的提醒代码的含义。相比于第三种方案编写复杂度也有了一定降低

对于类型安全我的做法是，当在组件内引入Mutation时再次编写对应的函数接口，在Vuex中编写的时候，通过引入Vuex提供的类型配合自定义类型，保证类型安全。

具体的实践在我们『相关实践』部分会有更具体写的介绍。

## 相关实践

## CLI工具

## 其他
