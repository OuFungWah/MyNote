# Java 修饰词 Modifier
|Author|CrazyWah|
|---|---|
|Date|2018.03.17|
|CopyRight|crazywah.com|

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

一般情况下，当创建类时就是在描述该类型的对象的外观和行为，除非使用new创建该类的对象，否则，实际上并没有获得任何对象。执行new创建对象时，数据存储空间才被分配，其方法才供于外界调用。但是静态就不一样了，有静态修饰即可以不需要对象也可以访问数据或调用方法了。

### 1.1、静态变量（类变量）：*(Static Variables)*

使用`static`修饰的变量，常用于创建独立于所有该类对象以外的变量。不管这个类的对象有多少，`static`修饰的变量的副本都只有一个。

`static`修饰的变量也就是我们常说的类变量，方法中的变量不可以被`static`修饰。

`static`修饰的变量将存放于方法区

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

使用`static`修饰的方法会独立存在于任何该类的对象以外。

`static`修饰的方法不能调用任何在当前这个类中定义的值或对象。只能依靠参数传入的数据并对这些数据进行处理，而不引用该类定义的变量，除了类中静态修饰的成员变量。

类变量和类方法都可以通过类名+'`.`'来调用。

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
### 2.2、终态方法 *(Final Methods)*
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

### 2.3、终态类 *(Final Classes)*

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

```java
abstract class Test{

}
```

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

Synchronized关键字是用于限制某一区域在任意一个时刻只允许一个线程访问，是一个给代码块上锁的过程

使用Synchronized做同步锁有两种方法：类锁与对象锁

看着很抽象，我们看看例子：

### 4.1、类锁

#### 4.1.1、类锁的示例代码

如果不加类锁：

```Java

public class SynchronizedClassLockTest {

    private int index = 0;

    public static void main(String[] args){
        //新建两个对象
        SynchronizedClassLockTest test1 = new SynchronizedClassLockTest();
        SynchronizedClassLockTest test2 = new SynchronizedClassLockTest();
        //在两个不同的线程中调用add()方法
        new Thread(new Runnable() {
            @Override
            public void run() {
                while(true){
                    if (test1.index>30)
                        break;
                    test1.add("A = ");
                }
            }
        }).start();
        new Thread(new Runnable() {
            @Override
            public void run() {
                while(true){
                    if (test2.index>30)
                        break;
                    test2.add("B = ");
                }
            }
        }).start();
    }

    public void add(String string){
        //输出当前调用add()的线程和对象的index
        System.out.println(string+"调用add() :");
        index++;
        System.out.println(string+index);
    }
}
```

在执行以上代码的时候，我们可以预期输出效果应该是

```
...
A = 18
A = 调用add() :
A = 19
A = 调用add() :
...
```

但是这之中出了叛徒

```
...
A = 调用add() :
B = 调用add() :
B = 1
B = 调用add() :
A = 28
B = 2
...
```

明明应该是`A调用add()`之后是应该输出`A = 28`的，而`B = 调用add() : B = 2`亦是如此。其实这个问题虽然是偶然事件，但它的出现就体现出来了多线程环境底下的不确定性。如何消除这种不确定性，这时候就该使用到类锁了：

```java
  ...
    public void add(String string){
      synchronized(SynchronizedClassLockTest.class){
        //输出当前调用add()的线程和对象的index
        System.out.println(string+"调用add() :");
        index++;
        System.out.println(string+index);
      }
    }
  ...
```

使用类锁锁住这部分代码以后就可以保证这部分的代码在同一时刻只允许一个线程访问，而不会在代码未执行完却因线程的时间片轮转完而让其他线程执行该部分。

注意一点：如果类锁锁住的只是`synchronized(){}`大括号括住的部分,如果上面的代码改成

```java
  ...
    public void add(String string){
      //输出当前调用add()的线程和对象的index
      System.out.println(string+"调用add() :");
      synchronized(SynchronizedClassLockTest.class){
        index++;
        System.out.println(string+index);
      }
    }
  ...
```

如果这样，最开始的问题依旧会出现。

### 4.2、对象锁
#### 4.2.1、对象锁的代码示例

如果不加对象锁

```java
package modifier;

public class SynchronizedObjectLockTest {

    private int index = 0;

    public static void main(String[] args){
        SynchronizedObjectLockTest test1 = new SynchronizedObjectLockTest();
        new Thread(new Runnable() {
            @Override
            public void run() {
                while(true){
                    test1.add("A = ");
                    if (test1.index>50)
                        break;
                }
            }
        }).start();
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true){
                    test1.add("B = ");
                    if (test1.index>50)
                        break;
                }
            }
        }).start();
    }

    private void add(String str){
        System.out.print(Thread.currentThread()+" :  ");
        index++;
        System.out.println(str+index);
    }
}

```

输出会出现不确定性

```
...
hread[Thread-0,5,main] :  A = 11
Thread[Thread-0,5,main] :  A = 12
Thread[Thread-0,5,main] :  A = 13
Thread[Thread-1,5,main] :  Thread[Thread-0,5,main] :  B = 14
A = 15
Thread[Thread-1,5,main] :  B = 16
Thread[Thread-0,5,main] :  Thread[Thread-1,5,main] :  B = 18
A = 17
Thread[Thread-1,5,main] :  Thread[Thread-0,5,main] :  A = 20
B = 19
...
```

我们加上对象锁：

```java
...
  private void add(String str){
    //对象锁
      synchronized (this){
          System.out.print(Thread.currentThread()+" :  ");
          index++;
          System.out.println(str+index);
      }
  }
...
```

此时就完满了

### 4.3、类锁和对象锁的区别

但是严厉的小伙伴应该发现了，在我的例子里面，两个例子里面，最大的区别仅仅在于synchronized后面的括弧里面内容不一样而已：

类锁：

```java
  ...
  synchronized(SynchronizedClassLockTest.class){
      ...
  }
  ...
```

对象锁：

```java
  ...
  synchronized(this){
    ...
  }
  ...
  public synchronized void method(){

  }

```

虽然看似区别不大，但是在运行起来操作起来就有很明显的不同

1. 类锁：只要是被类锁锁住的部分，不管是哪个对象（或是类方法）要对该区域进行访问，在任何一个时刻只允许一个线程访问
2. 对象锁：对于一个对象，被对象锁锁住的部分同一时刻只允许一个线程访问的，但是不影响其他对象对同一区域的访问。

## 5、临时修饰词 *(The Transient Modifier)*
和这个关键字十分相关的一个技术点，那就是序列化(直接存储一个对象为二进制数据)，在序列化一个对象的时候，其中的成员亦会被序列化，这是序列化的一个特点。被`transient`关键字修饰的成员变量，在序列化对象时该成员变量不会被序列化。

我们先来看正常的序列化过程：

```java
public class SerializableTest {

    public static void main(String[] args) {
        try {
            //输出对象
            ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream("cache.txt"));
            outputStream.writeObject(new Bean(10, 99));
            //读取对象
            ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream("cache.txt"));
            Bean bean = (Bean) inputStream.readObject();
            System.out.println("bean : ");
            System.out.println("index : " + bean.index);
            System.out.println("a : " + bean.a);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

}

class Bean implements Serializable {

    private static final long serialVersionUID = 1L;

    public Bean(int index, int a) {
        this.index = index;
        this.a = a;
    }

    public int index = 1;

    public int a = 0;

}
```

如上代码做了两件事，将`index = 10`和`a = 99`的对象存到了cache.txt文件中，然后重新从cache.txt中读取我们之前存储的对象，然后输出读取到的对象中的信息，可以预见的是，输出应该是：

```
bean :
index : 10
a : 99
```

当我们给a添加`transient`关键字以后：

```java
  ...
  public transiment int a = 0;
  ...
```

其余代码不变，结果将是对象的a变量没有被序列化，所以从cache.txt中获取的对象的a变量将是一个该类型的默认值（String为null，int为0等等）

```
bean :
index : 10
a : 0
```

## 6、总结
Java为我们提供了许多的关键字，什么情况下需要使用什么关键字我们还需要多加使用练习才能作出准确的判断，如果有什么地方有问题或错误，还望各位指出
