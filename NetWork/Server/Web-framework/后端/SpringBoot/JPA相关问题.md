# JPA相关问题

## SpringBoot2.0 (Spring-Data-Jpa) findById(findOne())和Optional的使用

### 1、findOne()方法的替代方法findById()

2.0版本，Spring-Data-Jpa修改findOne()。

* 1）2.0版本之前

```java
T findOne(ID primaryKey);
```

* 2）2.0版本

```java
  Optional<T> findById(ID id);
```

### 2、Optional Optional的使用

文档：Optional

container对象，可能包含也可能不包含非null值。如果存在值，则isPresent()将返回true，get()将返回该值。提供依赖于是否存在包含值的其他方法，例如orElse()（如果值不存在则返回默认值）和ifPresent()（如果值存在则执行代码块）。

```java
Optional<T> findById(ID id)
```

中Optional的一些用法：

* 1）如果没找到指定实体，则返回一个默认值。

```java

Foo foo = repository.findById(id).orElse(new Foo());

```

或者

```java
Foo foo = repository.findById(id).orElse(null);

```

* 2）如果找到实体返回它，否则抛出异常

```java
return repository.findById(id)
        .orElseThrow(() -> new EntityNotFoundException(id));
```

* 3）假设希望根据是否找到实体来应用不同的处理（无需抛出异常）

```java
Optional<Foo> fooOptional = fooRepository.findById(id);
if (fooOptional.isPresent()){
    Foo foo = fooOptional.get();
   // 处理 foo ...
}
else{
   //另一种情况....
}
```

### Spring-Data-Jpa的Sort排序时遇到的问题 has private access in 'org.springframework.data.domain.Sort'

springboot2.2.1（含）以上的版本Sort已经不能再实例化了，构造方法已经私有

![image.png](https://i.loli.net/2020/03/06/o36CiPeL517fWlQ.png)

![image.png](https://i.loli.net/2020/03/06/sm1e2lghd35IOn8.png)

改用Sort.by获得Sort对象

![image.png](https://i.loli.net/2020/03/06/vPjKirqOkAd1zCp.png)

```java
@GetMapping("/test2")
    public String find3() {
        List<Book> book = bookDao.findAll(Sort.by(Sort.Direction.DESC, "bookId"));
        for (Book book1 : book) {
            System.out.println(book1);
        }
        return "success";
    }

```

Sort.by()可以一个或多个字段排序
