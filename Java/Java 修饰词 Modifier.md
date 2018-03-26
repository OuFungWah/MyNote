# Java 修饰词 Modifier
* Author:CrazyWah
* Date:2018.03.17
* CopyRight:crazywah.com

写这篇总结有两个原因：
1. 今天去笔试了，发现自己的Java基础有一些细节忘掉了，所以决定同时`Android`、`Java`双开（希望肝不会爆。。。）
1. 其实`Java`基础对于`Android`开发起着至关重要的作用，所以把它好好整理整理是非常有必要的。

## 目录
1. 静态修饰词 *(The Static Modifier)*
2. 终态修饰词 *(The Final Modifier)*
3. 抽象修饰词 *(The Abstract Modifier)*
4. 同步修饰词 *(The Synchronized Modifier)*
5. 临时修饰词 *(The Transient Modifier)*

## 1、静态修饰词 *(The Static Modifier)*
一般情况下，当创建类时就是在描述类的对象的外观和行为，除非使用new创建那个类的对象，否则，实际上并没有获得任何对象。执行new创建对象时，数据存储空间才被分配，其方法才供于外界调用。但是静态就不一样了，有静态修饰即可以不需要对象也可以访问数据或调用方法了。
### 1.1、静态变量（类变量）：*(Static Variables)*
使用`static`修饰的变量，常用于创建独立于所有该类对象以外的变量。不管这个类的对象有多少，`static`修饰的变量的副本都只有一个。

`static`修饰的变量也就是我们常说的类变量，方法中的变量不可以被`static`修饰。

**正确** 定义代码示例：
```java
class Test{
  //this is allowed
  public static int index = 0;

}
```
**错误** 定义代码示例：
```Java
class Test{

  void test(){
    // this is illegal
    static int index = 0;
  }
}
```

**正确** 调用示例：
```java
  //this is allowed
  Test.index = 0;

  //this is allowed, too
  Test test = new Test();
  test.index = 0;
```

### 1.2、静态方法（类方法）：*(Static Methods)*
使用static修饰的方法会独立存在于任何该类的对象以外。

static修饰的方法不能调用任何在当前这个类中定义的值或对象。只能依靠参数传入的数据并对这些数据进行处理，而不引用该类定义的变量，除了静态的。

类变量和类方法都可以通过类名+'.'来调用。

**正确** 定义例子：
```Java
class Test{
  // this is allowed
  static int max(int x,int y){
    return x>y?x:y;
  }
}
```

**错误** 定义例子:
```Java
class Test{
  float PIE = 3.14f;
  //this is illegal, because the reference of variable defined in this class
  static float circumference(int r){
    return PIE*r*2;
  }
}
```

**正确** 调用示例：

```java
  //this is allowed
  Test.max(4,5);

  //this is allowed, too
  Test test = new Test();
  test.max(4,5);
```

## 2、终态修饰词 *(The Final Modifier)*
### 2.1、终态变量（常变量） *(Final Variables)*
当一个变量被`final`修饰时只能被初始化一遍。声明为`final`的引用变量永远不能被重新分配以引用不同的对象。

无论如何，对象里面的数据可以改变，但是对对象的引用则不可改变。

对于变量，使用`final`修饰的变量通常与`static`搭配使用，使常量作为类变量。

**正确** 代码示例:
```java
class Test{
  //this is allowed
  private final String TAG = "HelloWorld";
  //this is illegal, because we should give the value to the variable when initialized
  private final int index;
  //more usually like this
  public static final float PIE = 3.14f;
}

  //this is illegal, because the variable defined final can never be reassigned to refer to an different object.
  PIE = 3.00f;
```
**错误** 代码示例：
```Java
  //another example
  class Node{
    int value = 0;
    String descrition = null;
  }

  final Node node = new Node();
  //this is allowed
  node.value = 10;
  //but this is illegal, because the state of the object can be changed but not the reference
  node = new Node();  //    <----这一句错误

```
### 2.1、终态方法 *(Final Methods)*
被final修饰的方法不可以被它的子类重写。正如前面提到的，final修饰词使用于预防子类重写父类方法的一种方式

使用final修饰方法的主要目的在于不想方法中的内容被其他任何其他地方修改。

**正确** 代码示例：
```java
class Test{
  //this is allowed
  public final void say(){
    System.out.println("Hello");
  }
}
```
**错误** 代码示例：
```Java
class Test{
  public final void say(){
    System.out.println("Hello");
  }
}
class SubTest extends Test{
  //this is illegal, because the Methods defined Final can not be Override
  @Override
  public void say(){
      System.out.println("Morning");
  }
}
```
### 2.1、终态类 *(Final Classes)*
使用final来修饰一个类最主要的目的就是防止这个类产生子类。如果一个类被final修饰的话，没有任何其他类可以继承它。
**正确** 代码示例：
```Java
//this is allowed
final class Test{
  public void say(){
    System.out.println("Hello");
  }
}
```
**错误** 代码示例：
```java
final class Test{
}
//this is illegal, because the final class can not be inherited
class SubTest extends Test{

}
```
## 3、抽象修饰词 *(The Abstract Modifier)*
### 3.1、抽象类 *(Abstract Classes)*
一个抽象类永远都不可以实例。如果一个类被abstract修饰，它的唯一目的就是这个类是用于扩展的。

一个类不允许同时被final和abstract修饰，因为final表示不可扩展。如果一个类里面有抽象方法，那么这个类一定要是抽象类。否则会编译错误。

一个抽象类可以同时拥有抽象方法和普通方法

An abstract class can never be instantiated. If a class is declared as abstract then the sole purpose is for the class to be extended.

A class cannot be both abstract and final (since a final class cannot be extended). If a class contains abstract methods then the class should be declared abstract. Otherwise, a compile error will be thrown.

An abstract class may contain both abstract methods as well normal methods.
### 3.2、抽象方法 *(Abstract Methods)*
使用abstract修饰的方法即是一个里面没有任何实现的方法。这个方法的实现由它的子类提供。抽象方法不可以同时被final、static或者synchronized修饰。

一个类如果继承了抽象类，那么必须把抽象类中的抽象方法实现了，除非这个类也是一个抽象类。

如果一个类中有一个或以上的抽象方法，该类必须定义为抽象类。但是，抽象类可以没有任何抽象方法。

抽象类的定义以分号`;`结尾

**正确** 代码示例：
```Java
abstract class Test{
  //this is allowed
  public abstract void say();
}

//a class without any abstract method is allowed, too.
abstract class Test2{
  public void say(){
    System.out.println("Hello");
  }
}

//a class extends an abstract class must provide the implementation of all abstract methods
class SubTest extends Test{
  @Override
  public void say(){
    System.out.println("Hello");
  }
}

//Otherwise it is an abstract class, too.
abstract SubTest2 extends Test{

}
```
**错误** 代码示例：
```java
//this is illegal
abstract static void sayHello();
//this is illegal, too.
abstract synchronized void sayHello();
//this is also illegal
abstract final void sayHello();
```

## 4、同步修饰词 *(The Synchronized Modifier)*
## 5、临时修饰词 *(The Transient Modifier)*
## 6、总结
## 参考文献
