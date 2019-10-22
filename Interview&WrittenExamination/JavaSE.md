# javaSE

* 1.如果一个进程在运行过程中占用的内存无限制上升，那么该进程有内存泄漏

* 2.访问修饰符作用范围由大到小排列:public>protected>default>private
    
      default：包内的任何类，重点突出包
      protected：包内的任何类及包外继承了该类的子类，重点突出继承
      
* 3.Java中的异常:可不检测（unchecked）异常:包括运行时异常（RuntimeException与其子类）和错误（Error）。
       
      异常可以分为检查异常和非检查异常.
      检查异常顾名思义就是需要进行检查的异常, 需要使用try catch捕获或者throws抛出. (除去runtimeException及其子类的exception及其子类)
      非检查异常 : runtimeException 及其子类, 还有Error(Error也属于异常, 并且属于非检查异常)
      
* 4.在数据库系统中，产生不一致的根本原因是：
* 并发控制不当
* 数据冗余
* 未对数据进行完整性控制