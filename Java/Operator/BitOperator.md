# 位操作符

|Author|区枫华|
|-----|-----|
|Date|2015-04-14|

## 位操作符

位操作符即按照数据中的**二进制位操作**。

```
135与100进行按位与运算

135：1000 0111
100：0110 0100

按位与运算结果：

12：0000 1100

```

## 按位操作符

### ‘&’ 按位与

按位与，即操作数与被操作数按位进行与运算，运算位上同为1或同为0则结果为1，如果运算位上各不相同则结果为0。

如：

```
按位与：
    1001 0110
&   0111 0111
=   0001 1110
```

应用：

* 检测数据是否能被2整除

```
6与1 按位与运算

    0000 0110
&   0000 0001
=   0000 0000

结果为 0，所以6能被2整除
```

Java 代码：

```java
    if( x & 1 == 0){
        //能被二整除
    }else{
        //不能被二整除
    }
```

*为什么不使用`x % 2 == 0`来检查呢？因为计算机的底层就是用的位运算，所以执行位运算的效率会比其他运算的效率高得多*

* 对 2 的次方数求余

```
15 对 8（2 的 3 次方）求余，即（15 & (8 - 1)）

    0000 1111
&   0000 0111
=   0000 0111

结果为 7，即 15/8 余 7

```

* 消去二进制中最后一位的1

x & (x - 1)即可消去最后一位的1

```

    1011 1000
-1  1011 0110
&   1011 0000

可见最后 1011 1000 的最后一位1在操作完成后被消除了。

```

### ‘|’ 按位或

按位或，即操作数与被操作数进行按位或运算，运算位上其中一个为1，结果都为1，反之则为0。

如：

```
    1001 0110
|   0111 0111
=   1111 0111
```

应用：

### ‘^’ 按位异或

按位异或，即操作数与被操作数进行按位亦或运算，运算位各不相同则为1，相同则为0。

如：

```
    1001 0110
^   0111 0111
=   1110 0001
```

应用：

* 在一堆两两重复的数字里面找一个出不重复的

利用 `x ^ x = 0` 的特点和 `x ^ 0 = x` 的特点

```java
    // [1,2,3,1,2]

    int result = 0;
    for(int num : nums){
        result ^= num;
    }

    // 最后输出 result 就是 3
```

* 不借助辅助空间交换两个整型

```java
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
```

### ‘~’ 按位非（按位取反，一目运算符）

按位取反，即操作数自己对其每一个二进制位进行按位取反，如果二进制位本身为1则结果为0，如果二进制为0则结果为1。

```
~   1001 0110
=   0110 1001
```

## 移位操作符

### ‘<<’ 左移操作符

将原数据的二进制全部左移N（当N为负数时则是右移 (总位长度 + N)）位，若为正数则左边的二进制位补0；若为负数则左边的二进制位补1。

```
<<3     1001 0110
=       1011 0000
```

### ‘>>’ 右移操作符

将原数据的二进制全部右移N（当N为负数时则是右移 (总位长度 + N)）位，若为正数则左边的二进制位补0；若为负数则左边的二进制位补1。

```
>>3     1001 0110
=       0001 0010
```

### ‘>>>’ 无符号右移

无符号右移则是在游右移的基础上忽略掉符号的因素直接右移，而左边空出来的二进制位统一补0。

*[更多位运算的应用](https://www.zhihu.com/question/38206659/answer/158068857)*