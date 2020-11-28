# Iview

[iview官网](http://v1.iviewui.com/docs/introduce)

## Iview组件-tree 远程加载

```js
<Tree v-show="curType=='archive'"  :data="archiveTree" :load-data="loadData" @on-select-change="selectChange" :show-check="false"> </Tree>
data () {
    return {
      archiveTree:[],树的集合
      id:-1,//根节点
      }}
mounted() {//生命周期函数，页面刷新时调用此方法初始化树
       this._loadData(this.id,(array) =>{
           this.archiveTree=array
       })
     },
      methods: {
     loadData (item, callback) {//异步加载的方法
       this._loadData(item.id,callback)
       },
       _loadData(code,callback){ //发送请求并且对后台的数据进行处理
         this.$axios.get('/api/cate/SelectNode?pcode='+code).then((res)=>{
           const array=[] //创建一个数组
           console.log(res.data)
           for(let i=0;i<res.data.length;i++){
             let item=res.data[i]  
             array.push(item={id:item.id,title:item.title,loading:false,children:[],source:item})//将返回值赋值给新数组在这里可以给json对象添加属性
             if(item.source.leaf) delete item.loading
          }
          callback(array) /返回新数组
         })
       },
       selectChange(selectedList){
         //获取当前点击的节点
         const node = selectedList[selectedList.length - 1]
        this.$axios.post('/api/cate/SelectTrss',
               this.qs.stringify({
                   id: node.id
                }))
               .then(res => {
                  const  list=[]
                  for(let i=0;i<res.data.length;i++){
                    let items=res.data[i]
                    list.push(items={title:items.name,type:'text'})
                  }
                   console.log(list)
                 this.fields= list;
              })
         if(node){
           this._loadData(node.id,(res)=>{
             if(!res)return //没有子节点则返回
             let array=[]
             res.forEarch(item => {//遍历子节点然后在各子节点上递归调用请求下一层后代
             array.push(item)
             this._loadData(item.id,()=>{
             })
             node.children=array //挂载子节点
             node.expand=true    //展开子节点
             })
           })
         }
       },

```
