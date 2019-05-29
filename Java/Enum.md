# 枚举类型 enum

|Author|区枫华|
|------|-----|
|Date|2019-05-16|

枚举类型，多使用于表示某种标识。枚举类型中所有的实例都是常量。以此取代使用 int 常量作为标识的做法。

## 一、简单使用

例如说我们在 Person 类中加入几个身份标识分别为：学生、老师、管理员

```java
class Person{

    enum IDENTIFY{
        STUDENT,    //学生
        TEACHER,    //老师
        ADMINISTER  //管理员
    }

    private IDENTIFY identify;

    public Person(IEDNTIFY identify){
        this.identify = identify;
    }

}
```

由于枚举类型里面的实例都是常量，所以也可以直接套用到 switch - case 的选择结构当中

```java
class Person{
    
    ...//上面的代码

    public boolean deletePerson(int id){
        switch(identify){
            case IDENTIFY.STUDENT:  
                //  学生无权限删除
                return false;
            case IDENTIFY.TEACHER:
                //  老师无权限删除
                return false;
            case IDENTIFY.ADMINISTER:
                //  管理员可以删除
                return deletePersonById(id);
            default:
                return false;
        }
    }

}
```

## 二、枚举类型的理解

**枚举类型（enum）其实是类（class）的一种特例**，就像当年我们理解 Java 的接口（interface）是全是抽象方法和公共常量实例的类一样。枚举类型也可以理解为可以定义常量的类，其与普通的类一样，可以声明成员变量、可以声明方法、可以声明构造函数等等。enum 甚至可以实现接口，但是**不能继承或被继承**。

创建 enum 时，编译器会帮我们生成一个对应的类，该类继承了 Enum 类并提供一些相关方法。

一些枚举类型的方法(使用上面的 TYPE 作为例子)：

* `TYPE.STUDENT.ordinal();` 获取该枚举实例在 enum 中的声明顺序，返回一个 int 值。
* `TYPE.values();` 获取所有枚举实例，返回 TYPE 数组
* `TYPE.valueof("STUDENT");` 获取名为 STUDENT 的枚举实例，返回单个枚举实例。

## 三、组织枚举类型

枚举类型的组织方式有两种：实现接口，枚举数组。

### 3.1、实现接口

因为 Java 支持单继承，所以默认继承 Enum 类的枚举类型无法再去继承其他类，我们可以改用实现接口的方法来实现枚举类型的归类。

```java
// 使用 PersonType(人物类型) 接口统一所有的人物相关的枚举类型
interface PersonType{
    // PersonType(人物类型) 之下的 STUDENT(学生) 小分类
    enum STUDENT implements PersonType {
        PRIMARY,
        SENIOR
    }
    // PersonType(人物类型) 之下的 TEACHER(老师) 小分类
    enum TEACHER implements PersonType {
        MATH,
        CHINESE,
        ENGLISH,
        PE
    }    
    // PersonType(人物类型) 之下的 ADMINISTRATOR(管理员) 小分类
    enum ADMINISTRATOR implements PersonType{
        NORMAL,
        MASTER
    }
}
```

*当然，分类必须要基于需求，避免过度设计*

### 3.2、枚举数组

枚举数组就是在枚举里面声明一个已经声明好的枚举类型数组

```java
    // 餐
    enum MEAL{
        // 新建 TYPE_COFFCE 枚举实例并传入 Drink.COFFCE 以获取其枚举实例数组
        TYPE_COFFCE(Drink.COFFCE.class),
        // 新建 TYPE_CARBONATED 枚举实例并传入 Drink.CARBONATED 以获取其枚举实例数组
        TYPE_CARBONATED(Drink.CARBONATED.class);
        // 存放枚举常量的成员数组
        private Drink[] values;
        // MEAL 枚举类型的构造函数，接收实现了 Drink 接口的枚举类
        MEAL(Class<? extends Drink> type){
            // 获取传入的枚举实例
            values = type.getEnumConstants();
        }

        public Drink[] getValues(){
            return values;
        }
    }

    // 
    interface Drink{
        enum COFFCE implements Drink{
            AMERICAN,
            LATTE,
            ESPRESSO
        }
        enum CARBONATED implements Drink{
            COLE,
            PESSI,
            SPRITE
        }
    }

```

## 四、枚举的其他实用类

### 4.1、EnumSet

enum 固然是声明常量的好方法，但是其中的常量实例不方便增加或删除。这时就应该要使用 EnumSet 了，EnumSet 是集合了 enum 和 Set 集合的一个类，主要就是为了解决枚举类型不能插入删除操作的问题。

```java

    // EnumSet 是不可以直接实例化的，需要通过其给出的静态方法获取其实例
    EnumSet<Drink.COFFCE> set = EnumSet.noneOf(Drink.COFFCE.class);
    // 获取 EnumSet 实例后就可以操作 Set 一般地去操作 EnumSet 的实例了
    set.add(Drink.COFFCE.ESPRESSO);
    set.add(Drink.COFFCE.AMERICAN);

```

#### 4.1.1、EnumSet 获取实例的静态方法

* `EnumSet.allOf()` 获取一个用于装载某个枚举类型的 EnumSet 并将改枚举中的所有实例填装到 Set 实例中。

```java
    enum TYPE{
        TYPE1,
        TYPE2;
    }

    ...
    EnumSet<TYPE> set = EnumSet.allOf(TYPE.class);
```

* `EnumSet.noneOf()` 获取一个用于装载某个枚举类型的空 EnumSet。

```java
    enum TYPE{
        TYPE1,
        TYPE2;
    }

    ...
    EnumSet<TYPE> set = EnumSet.noneOf(TYPE.class);
```

* `EnumSet.copyOf()` 拷贝一个已存在的 EnumSet。

```java
    enum TYPE{
        TYPE1,
        TYPE2;
    }

    ...
    EnumSet<TYPE> set = EnumSet.noneOf(TYPE.class);
    // 拷贝已存在的 Set
    EnumSet<TYPE> copySet = EnumSet.copyOf(set);
```

#### 4.1.2、EnumSet 的运作原理（源码分析）

EnumSet 的源码文档注释中有一句话很有意思：“The space and time performance of this
 class should be good enough to allow its use as a high-quality, typesafe
 alternative to traditional int -based "bit flags."”，翻译过来是“EnumSet 是一个时间和空间性能上都足够好允许它作为一个高质量且类型安全的、传统 int 常量标识的替代品”。嗯哼？时间空间上性能都很好？本人是很好奇怎么做到的。

进入到 EnumSet 的那些静态方法的源码中：

```java
    public static <E extends Enum<E>> EnumSet<E> allOf(Class<E> elementType) {
        EnumSet<E> result = noneOf(elementType);
        ...
        return result;
    }

    public static <E extends Enum<E>> EnumSet<E> of(E e1, E e2) {
        EnumSet<E> result = noneOf(e1.getDeclaringClass());
        ...
        return result;
    }

    // 其他的一些静态方法
    ...

    public static <E extends Enum<E>> EnumSet<E> noneOf(Class<E> elementType) {
        ...
    }
```

从源码中我们看到，不管是哪一个静态方法都是由 `EnumSet.noneOf()` 这个静态先获取到 EnumSet 对象再去做操作的，所以我们就先去看看 `EnumSet.noneOf()` 又做了哪些事情。

```java
    public static <E extends Enum<E>> EnumSet<E> noneOf(Class<E> elementType) {
        // 1、获取该枚举类型中的所有枚举实例放入一个数组中
        Enum<?>[] universe = getUniverse(elementType);
        // 2、如果数组为空则抛出异常（因为没有枚举内容）
        if (universe == null)
            throw new ClassCastException(elementType + " not an enum");
        // 3、如果少于 64 个枚举实例则创建一个 RegularEnumSet（常规大小的 EnumSet）；大于 64 个枚举实例则创建一个 JumboEnumSet（大型的 EnumSet）。
        if (universe.length <= 64)
            return new RegularEnumSet<>(elementType, universe);
        else
            return new JumboEnumSet<>(elementType, universe);
    }
```

根据 `EnumSet.noneOf()` 的源码不难看出，它主要根据枚举类型中的枚举实例的数量选择不同的创建 EnumSet 的方案的，那么 RegularEnumSet 和 JumboEnumSet 分别是怎么实现的以及他们的区别应该就是 EnumSet 时间空间复杂度足够好的关键之处了。

`RegularEnumSet` 的作用是存放数量少于等于 64 枚举类型实例的。

```java
    private long elements = 0L;
```

在 `RegularEnumSet` 中没有太多的成员变量，除了从 `EnumSet` 中继承下来的 `elementType`（枚举类型）以及 `universe`（枚举实例数组）以外就只又上面源码中看到的，声明了 `elements` 这个新的成员变量，而这个就是它性能好的关键所在。

只有这个 long 类型怎么保存这些 Enum 的实例呢？我挖了一下那些跟插入删除相关的操作方法的源码：

```java
    // 添加所有枚举实例
    void addAll() {
        if (universe.length != 0)
            // 将 -1 无符号右移至只剩 universe.length 这么多位的 1
            // elements 二进制上 每个 1 代表存放了 枚举
            elements = -1L >>> -universe.length;
    }

    // 添加某个枚举实例
    public boolean add(E e) {
        // 检查枚举类型
        typeCheck(e);

        // 留起原有的 elements 用作等一下比较是否插入成功
        long oldElements = elements;
        // 对数据 1 进行左移 N（该枚举实例在枚举类型对应的位置）位的操作
        // 再对 elements 进行按位或操作，将 elements 的对应二进制位改为 1。
        elements |= (1L << ((Enum<?>)e).ordinal());
        // 如果修改前后一模一样说明该枚举实例原本就添加进去了，则返回 false
        return elements != oldElements;
    }

    // 移除某个枚举实例
    public boolean remove(Object e) {
        // 对象判空与类型安全检查
        if (e == null)
            return false;
        Class<?> eClass = e.getClass();
        if (eClass != elementType && eClass.getSuperclass() != elementType)
            return false;

        long oldElements = elements;
        // 对数据 1 进行左移 N（该枚举实例在枚举类型对应的位置）位的操作
        // 再做按位取反，除了标记出来的位置为0其他都为1
        // 再对刚才处理好的数据和 elements 按位与，因为标记位为0，所以 elements 的对应位就会变成0，达到了删除的目的
        elements &= ~(1L << ((Enum<?>)e).ordinal());
        return elements != oldElements;
    }
```

根据源码对数据的操作我们可以看出来了，**其实原理就是对 elements 数据的二进制位进行操作，每个二进制位表示枚举类型中对应位置的枚举实例的填装情况**，1 代表已添加到 Set 中，0 代表 Set 中没有该枚举实例。每一次的添加删除操作就是将对应的二进制位改为 1 或者 0 的操作。下面大致地描绘一下

```java
假设有这样的一个枚举类型

    enum TYPE{
        TYPE1,
        TYPE2,
        TYPE3,
        TYPE4
    }

TYPE1、TYPE2、TYPE3、TYPE4 的位置（ .ordinal() 方法获取到的 int 值 ）分别为 0、1、2、3

EnumSet set = EnumSet.noneOf(TYPE.class);   //获取一个 EnumSet

根据前面提到的，这时候就是新建一个 RegularEnumSet。

    set.add(TYPE2);  //往 set 里添加 TYPE2

根据源码有如下操作（正常来说 long 类型应该是 64 位的，但是这里方便展示就仅写出前 8 位）：

* 在 RegularEnumSet 中的 elements 默认为0，二进制为 [0000000]
* 添加 TYPE2，TYPE2 的顺序是 1，所以先把数字 1 左移 1 位
    数字 1      [00000001]
    左移 1 位   [00000010]
* elements 与 上面操作后的数据进行按或
    elements         [0000000]
    左移后的数据       [0000010]
    操作后的 elements [0000010]

到此，add 操作结束，可见在代表 TYPE2 的 1 号二进制位上为 1，表示 TYPE2 已存入。

    set.addAll();   //往 set 里面添加所有的枚举实例

根据源码有如下操作（其中 universe 就是装有该枚举类型的所有枚举实例的数组）：

* 将 -1 无符号右移 -(universe.length) 位。
* 右移 -(universe.length) 位就是右移到原数据只剩 universe.length 位的意思。
* universe.length 就是上面的 TYPE 中所有枚举实例的数量，为 4。
    -1              [11111111]
    无符号右移 -4     [00001111]
    赋给 elements    [00001111]

到此 添加所有枚举实例的操作就结束了，枚举类型中所有枚举实例所对应的二进制位都为1了，即都已存在于 set 中了。
```

前面也有提到过 `RegularEnumSet` 是负责应付枚举实例数量小于等于64的枚举类型，大于64的时候采用的是 `JumboEnumSet`。那么 `JumboEnumSet` 又什么区别呢？其实最大的区别在于，`RegularEnumSet` 是单个 long 成员变量，而 `JumboEnumSet` 使用的是 long 数组成员变量，而其核心的实现方式依旧是对 long 类型的二进制位进行运算。

由于 `EnumSet` 主要是使用 long 类型来存储具体的枚举实例，空间上的花费是比较少的，而每次的的插入删除操作是需要一两次的位运算，所以在时间上效率也非常高，正正是 `EnumSet` 注释中描述的那样。

### 4.2、EnumMap

`EnumMap` 其实就是一个比较特殊的 `Map`。普通的 `Map` 对键值对是没有什么要求的，***而 `EnumMap` 键的部分规定要使用创建时规定的枚举类型的实例***。除此以外，它与普通的 `Map` 使用上没什么太大的区别。

```java
    //假设一个 enum
    enum TYPE{
        TYPE1,
        TYPE2
    }

    // 使用EnumMap来存放过一些字符串
    EnumMap<TYPE,String> testMap = new EnumMap<>(TYPE.class);
    // 往Map中填充数据
    testMap.put(TYPE1,"存储的第一个字符串");
    testMap.put(TYPE2,"存储的第二个字符串");
```

在示范中可见，除了 `EnumMap` 在新建的时候要填入规定的枚举类型以外，其他的地方都基本和普通的 `Map` 是一致的

`EnumMap` 和普通的 `Map` 之间有一个最大的不同之处，那就是 `EnumMap` 的内部其实用的是数组实现的，**一个存储键的数组**和**一个存储值的数组**，两个数组中下标一致的两个实例就是一个键值对。**为什么是用的数组而不是链表呢**？因为枚举类型中的枚举实例都是编译期就已经决定好了的，而 `EnumMap` 规定了每个键值对的键是规定好的枚举类型的枚举实例，所以枚举类型的枚举实例的数量是不可变的，***换言之在创建该 `EnumMap` 之初就已经可以通过枚举实例的数量确定里面的内容能有多少了，而对于固定数量的容器，当然是选择使用数组来实现***。

## 小结

在 Java 中，enum 通常是用来取代传统的 int 类型常量来表示某些标识的，经过学习与分析，也的确体会到了 enum 用作标识时给程序可读性、可维护性以及性能上的提升，所以以后还是要多多利用才行！