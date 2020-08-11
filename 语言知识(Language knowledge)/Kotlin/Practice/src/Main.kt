//顶层变量：
val Pi = 3.14159265358979
var temp = 0
fun main(){
    //定义只读局部变量使⽤关键字 val 定义。只能为其赋值⼀次
    val a: Int = 1 // ⽴即赋值
    val b = 2 // ⾃动推断出 `Int` 类型
    val c: Int // 如果没有初始值类型不能省略
    c = 3 // 明确赋值
    var edge = a*b*c
    println("S-P-D-B")
    println(sum(a,b))
    edge*=2
    println(sum1(b,c))
    println(sum2(a,c))
    println(sum3(b,c))
    println("sum:${sum(edge,edge)}")

    println(incrementX())
    println(maxOf(a,b))
}

//带有两个 Int 参数、返回 Int 的函数
fun sum(a:Int,b:Int):Int{
    return a+b
}
//将表达式作为函数体、返回值类型⾃动推断的函数
fun sum1(a:Int,b:Int)= a+b

//函数返回⽆意义的值：
fun sum2(a:Int,b:Int):Unit{
    println("sum of $a and $b is ${a+b}")
}

//Unit 返回类型可以省略：
fun sum3(a:Int,b:Int){
    println("sum of $a and $b is ${a+b}")
}

fun incrementX():Int{
    temp +=9
    temp *=temp
    println(Pi)

    val sz = "temp is $temp"
    temp = 10086
    println(sz)
    val so = "${sz.replace("is","was")},but new is $temp"
    println(so)
    return temp
}

fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}


