# Gradle 基础语法 

***@Author oufenghua***

要能够读懂或者编写 Gradle 脚本，必要的语法基础还是需要先学习一下。

## 一、变量

Gradle 中的变量可以完全等价于 Java 中的变量，只不过 Gradle 所用的 Groovy 语言给 Java 增加了很多的语法糖，使的 Groovy 编写起来会和 Java 有些不一样

### 定义字符串 String

#### 定义

```gradle
def name = "Tom"
def teacherName = 'Amy'
```

以这两种方式创建字符串都是对应到 Java 中的 `java.lang.String` 这个类型的字符串变量。

#### 调用

```gradle
println "name = ${name} teacherName = ${teacherName}"
```

非常类似于 Kotlin 的使用方式

### 集合：List

#### 定义：

```Gradle
def numbers = [1,2,3,4,5]
```

#### 调用：

```Gradle
// 常规用法
println numbers[1] // 访问正序第 2 个元素
println numbers[-1] // 访问倒序第 1 个元素
println numbers[1..3]  // 访问正序第 2 至 4 的所有元素

// 遍历 list （实际上是一个闭包的使用，可以去看闭包的部分）
numbers.each{
    println it // it 相当于 numbers[n]
}

// 以上代码相当于我们常用的 for 循环遍历
for(def n = 0; n < numbers.size(); n++){
    println numbers[n]
}

```

### 集合：Map
#### 定义：

```Gradle
def ageMap = {"Tom": 99, "Amy": 89}
```

#### 调用：

```Gradle
// 取单个值
println ageMap["Tom"]

// 遍历 Map
ageMap.each{
    // it 是一个 Map.Entity，有 key 和 value 两个成员变量
    println "pair: ${it}"
    // 取 Pair 中的 Key
    println "key = ${it.key}"
    // 取 Pair 中的 Value
    println "value = ${it.value}"
}
```

## 二、方法
### 定义

```Gradle
// 常规的方法定义
def method1(int a, int b){
    return a + b
}

// 可省略的 return 关键字
def method2(int a, int b){
    a + b
}
```

### 调用 

```gradle
println method1(1, 2)

println method(2, 3)
```

## 类（JavaBean）

类型的定义在 Gradle 中可以完全理解就是 Java 的类，没有任何分别

### 定义

```gradle
// 定义一个 Person 类型
class Person{
    private String name
    private int age
}
```

### 调用

```gradle
// new 一个对象，同 Java
def p = new Person()
p.name = "Tom"
p.age = 19

// 访问对象中的成员变量
println "we have a person, name is ${p.name}, age is ${p.age}"
```

## 三、闭包（语法重点）

闭包相对于前面的变量和方法是一个比较不常规的概念。比较官方的说法是：闭包其实就是一个代码快....balabala，但是太正规不太好理解，所以稍微通俗一丢丢用我自己的理解来说就是：

>闭包本质上其实就是方法，不过是一个以 ***变量的形式存起来的方法***，可以当作是变量一般 ***赋值、传递或者调用***

### 定义

```gradle
// 定义一个无参数闭包

def closure = {
    println "this is a closure"
}

// 定义一个闭包带参数并指定类型
def closure1 = { int a, String b ->
    println "number ${a} is ${b}"
}

// 定义一个闭包带参数，不指定类型
def closure2 = { a, b ->
    a + b
}

```

### 调用

调用闭包其实就是调用方法，可以理解完全相同

#### 闭包的普通调用

```gradle

closure()

closure1(1, "haha")

// 获取闭包调用后的返回值
def result = closure2(1, 2)
```

#### 闭包当作参数传递，假设当前有这么一个需要闭包作为参数的方法：

```
def method(closure){
    println closure(1, 2)
}
```

1. 常规做法：

```gradle

// 声明一个简单的闭包
def closure = { int a, int b ->
    a + b
}

// 调用方法
method(closure)

```

2. 特殊用法(简易用法)

***PS：特别的，当我们把闭包当作参数传递到某个方法的时候，闭包可以直接简写像这样：***

```gradle
method{ a, b ->
    println a + b
}
```

以上写法其实就是给 method 方法传递了一个匿名的闭包，其实以上写法是等价于以下代码

```gradle
method({ a, b ->
    print a + b
})
```

只不过第一种写法是把打括号外面的一层小括号省略了罢了。

### 番外

看完闭包相关的这些内容我们可以回头去看一下刚才在 List 中介绍的 `numbers.each` 的使用

```gradle
// 遍历 list （实际上是一个闭包的使用，可以去看闭包的部分）
numbers.each{
    println it // it 相当于 numbers[n]
}
```

其实它具体的实现应该是类似于以下这样的：

```gradle
// 集合类型
class Collection{

    // 其他代码
    ...

    // 集合类型的 each 方法，传入一个闭包
    // 当我们每次遍历到一个具体 item 的时候就会调用一下这个传入的闭包中的逻辑
    def each(closure){
        // 常规遍历
        for(def n = 0; n < size(); n++){
            // 获取集合中具体的 item
            def item = get(n)
            // 调用闭包的逻辑并传入 item 
            closure(item)
        }
    }
}
```

*以上代码只是一个猜测的类似代码，并不完全和源码一致，留意*