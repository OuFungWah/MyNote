# Python

## Python 关键字

```
>>> import keyword
>>> print keyword.kwlist
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## 编译 Python：

两方式：

### 1、终端直接编写加编译

1. 在命令行中输入 python 进入 python 编写状态：

```
MacBook-Pro-2:$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

2. 写入 python 语句：

```
MacBook-Pro-2:$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>print("Hello World!");
```

3. 回车确认：

```
MacBook-Pro-2:~ crazywah$ python
Python 2.7.10 (default, Oct  6 2017, 22:29:07) 
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.31)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World!");
Hello World!
```


### 2、在文档中编写在终端中编译

1. 新建一个 .py 后缀的 python 文件：

在新建的 test.py 文件中写入 Python 代码：

```python
#!usr/bin/python3
# -*- coding: UTF-8 -*-

print("Hello World");

print("你好呀");
```

2. 在终端中输入 python + XXX.py 编译并运行 Python

输入的指令为 python + 文件路径（如果当前终端所处文件夹为文件的文件夹则不需要加） + 文件全称

```
MacBook-Pro-2:~ crazywah$ python /Users/crazywah/Documents/Development/Programming/Python/test.py
Hello World
你好呀
```

## Python 标识符：

1. 以单下划线开头 `_foo` 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入
2. 以双下划线开头的 `__foo` 代表类的私有成员
3. 以双下划线开头和结尾的 `__foo__` 代表 Python 里特殊方法专用的标识，如 `__init__()` 代表类的构造函数

## Python 行和缩进
在 Python 中使用缩进来区分代码快

```python
if True:
    print("This is True");
    print("This is True ,too");
else:
    print("This is False");
    print("This is False, too")
```

## Python 输出

```Python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
```

## Python 注释：

### 单行注释：

在要注释的那一行前面加上 #

```python
# 这是一行注释
```

### 多行注释:

三个单引号 `'''` 开始和结束 或者 三个双引号 `"""` 开始和结束


```python
'''
多行注释之一
多行注释之一
'''

“”“
多行注释之一
多行注释之一
”“”
```

## Python 弱类型变量
变量赋值只需要 `变量名 = 某类型` 即可

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print counter
print miles
print name
```

## Python 多变量赋值

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = b = c = 1

a, b, c = 1, 2, "john"
```

## 标准数据类型
在内存中存储的数据可以有多种类型。

例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。

Python 定义了一些标准类型，用于存储各种类型的数据。

Python有五个标准的数据类型：

* Numbers（数字）
* String（字符串）
* List（列表）
* Tuple（元组）
* Dictionary（字典）

## Python数字
数字数据类型用于存储数值。

他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。

当你指定一个值时，Number对象就会被创建：

```python
var1 = 1
var2 = 10
```
您也可以使用del语句删除一些对象的引用。

del语句的语法是：

```del var1[,var2[,var3[....,varN]]]]```
您可以通过使用del语句删除单个或多个对象的引用。例如：

```
del var
del var_a, var_b
```

Python支持四种不同的数字类型：

int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）

## Python 字符串

字符串或串(String)是由数字、字母、下划线组成的一串字符。

一般记为 :

```s="a1a2···an"(n>=0)```
它是编程语言中表示文本的数据类型。

python的字串列表有2种取值顺序:

* 从左到右索引默认0开始的，最大范围是字符串长度少1
* 从右到左索引默认-1开始的，最大范围是字符串开头

从字符串中截取一段字符：
x[start,end]
包括 start 到 end（end 本身不包括）。返回的是一个新的对象

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = 'Hello World!'
 
print str           # 输出完整字符串
print str[0]        # 输出字符串中的第一个字符
print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
print str[2:]       # 输出从第三个字符开始的字符串
print str * 2       # 输出字符串两次
print str + "TEST"  # 输出连接的字符串
```

结果

```
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
```

## Python 列表

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 [ ] 标识，是 python 最通用的复合数据类型。

列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表
```

```
['runoob', 786, 2.23, 'john', 70.2]
runoob
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['runoob', 786, 2.23, 'john', 70.2, 123, 'john']
```

******

***思考：字符串和列表类型的操作已经形式十分相似？字符串是否只是一个特殊的列表（装载字符的list）***

******

## Tuple（元组）

元组与列表类似，都是数据的集合。不同之处在于，元组内容不可被修改（类似于枚举类型？）。

如果非要修改就会报错```TypeError: 'tuple' object does not support item assignment```

使用括号声明 `（）` 

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
list = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinylist = ([)123, 'john')
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表
```

## Python Set 集合

集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 `{ }` 或者 `set()` 函数创建集合，***注意：创建一个空集合必须用 `set()` 而不是 `{ }`，因为 `{ }` 是用来创建一个空字典。***

创建格式：

```python
#!/usr/bin/python3
 
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
 
print(a - b)     # a和b的差集
 
print(a | b)     # a和b的并集
 
print(a & b)     # a和b的交集
 
print(a ^ b)     # a和b中不同时存在的元素
```

## Python Dictionary 字典

字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

```python
#!/usr/bin/python3
 
dict1 = {}
dict1['one'] = "1 字典一号"
dict1[2]     = "2 字典二号"
 
dict2 = {'name': 'fenghua','age':19, 'graduate':2019}
 
 
print (dict1['one'])       # 输出键为 'one' 的值
print (dict1[2])           # 输出键为 2 的值
print (dict2)          # 输出完整的字典
print (dict2.keys())   # 输出所有键
print (dict2.values()) # 输出所有值
```

## Python 数字与运算符

### Python 数据类型的转换

|函数	|描述|
|--|--|
|int(x [,base])|将x转换为一个整数|
|float(x)|将x转换到一个浮点数|
|complex(real [,imag])|创建一个复数|
|str(x)|将对象 x 转换为字符串|
|repr(x)|将对象 x 转换为表达式字符串|
|eval(str)|用来计算在字符串中的有效Python表达式,并返回一个对象|
|tuple(s)|将序列 s 转换为一个元组|
|list(s)|将序列 s 转换为一个列表|
|set(s)|转换为可变集合|
|dict(d)|创建一个字典。d 必须是一个序列 (key,value)元组。|
|frozenset(s)|转换为不可变集合|
|chr(x)|将一个整数转换为一个字符|
|ord(x)|将一个字符转换为它的整数值|
|hex(x)|将一个整数转换为一个十六进制字符串|
|oct(x)|将一个整数转换为一个八进制字符串|

### Python 运算符

|运算符	|描述	|实例|
|----|---|---|
|+	|加 - 两个对象相加|	a + b 输出结果 31|
|-	|减 - 得到负数或是一个数减去另一个数|	a - b 输出结果 -11|
|*	|乘 - 两个数相乘或是返回一个被重复若干次的字符串|	a * b 输出结果 210|
|/	|除 - x 除以 y|	b / a 输出结果 2.1|
|%	|取模 - 返回除法的余数|	b % a 输出结果 1|
|**	|幂 - 返回x的y次幂|	a**b 为10的21次方|
|//	|取整除 - 返回商的整数部分|	9//2 输出结果 4 , 9.0//2.0 输出结果 4.0|

### Python 比较运算符

|运算符	|描述	|实例|
|---|---|---|
|==	|等于 - 比较对象是否相等	(a == b)| 返回 False。|
|!=	|不等于 - 比较两个对象是否不相等	(a != b) |返回 True。|
|>	|大于 - 返回x是否大于y|	(a > b) 返回 False。|
|<	|小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。|	(a < b) 返回 True。|
|>=	|大于等于 - 返回x是否大于等于y。|	(a >= b) 返回 False。|
|<=	|小于等于 - 返回x是否小于等于y。|	(a <= b) 返回 True。|

### Python 赋值运算符

|运算符	|描述	|实例|
|---|---|---|
|=	|简单的赋值运算符|	c = a + b 将 a + b 的运算结果赋值为 c|
|+=|	加法赋值运算符|	c += a 等效于 c = c + a|
|-=|	减法赋值运算符|	c -= a 等效于 c = c - a|
|*=|	乘法赋值运算符|	c *= a 等效于 c = c * a|
|/=|	除法赋值运算符|	c /= a 等效于 c = c / a|
|%=|	取模赋值运算符|	c %= a 等效于 c = c % a|
|**=|	幂赋值运算符|	c **= a 等效于 c = c ** a|
|//=|	取整除赋值运算符|	c //= a 等效于 c = c // a|

### Python 位运算

|运算符|	描述|	实例|
|---|---|---|
|&|	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	|(a & b) 输出结果 12 ，二进制解释： 0000 1100|
|`|`|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	|(a | b) 输出结果 61 ，二进制解释： 0011 1101|
|^	|按位异或运算符：当两对应的二进位相异时，结果为1|	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001|
|~|	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1|	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。|
|<<|	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。|	a << 2 输出结果 240 ，二进制解释： 1111 0000|
|>>|	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	|a >> 2 输出结果 15 ，二进制解释： 0000 1111|

### Python 逻辑运算符

|运算符|	逻辑表达式|	描述|	实例|
|---|---|---|---|
|and	|x and y	|布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。|ß	(a and b) 返回 20。|
|or|	x or y|	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	|ß(a or b) 返回 10。|
|not|	not x|	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。|ß	not(a and b) 返回 False|

### Python 成员运算符

|运算符	|描述	|实例|
|in|	如果在指定的序列中找到值返回 True，否则返回 False。|	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。|
|not in|	如果在指定的序列中没有找到值返回 True，否则返回 False。|	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。|

### Python 身份运算符：

|运算符|	描述	|实例|
|---|---|---|
|is|	is 是判断两个标识符是不是引用自一个对象|	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False|
|is not	|is not 是判断两个标识符是不是引用自不同对象	|x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。|

注： id() 函数用于获取对象内存地址。

### Python 数学函数

|函数	|返回值 ( 描述 )|
|--|--|
|abs(x)|	返回数字的绝对值，如abs(-10) 返回 10|
|ceil(x)|	返回数字的上入整数，如math.ceil(4.1) 返回 5|
|cmp(x, y)|如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。|
|exp(x)|	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045|
|fabs(x)	|返回数字的绝对值，如math.fabs(-10) 返回10.0|
|floor(x)|	返回数字的下舍整数，如math.floor(4.9)返回 4|
|log(x)|	如math.log(math.e)返回1.0,math.log(100,10)返回2.0|
|log10(x)|	返回以10为基数的x的对数，如math.log10(100)返回 2.0|
|max(x1, x2,...)|	返回给定参数的最大值，参数可以为序列。|
|min(x1, x2,...)|	返回给定参数的最小值，参数可以为序列。|
|modf(x)|	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。|
|pow(x, y)|	x**y 运算后的值。|
|round(x [,n])|	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。|
|sqrt(x)|	返回数字x的平方根。|

### Python 随机数函数

|函数|	描述|
|--|--|
|choice(seq)|	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。|
|randrange ([start,] stop [,step])	|从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1|
|random()	|需要 `import random` 随机生成下一个实数，它在[0,1)范围内。|
|seed([x])	|改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。|
|shuffle(lst)|	将序列的所有元素随机排序|
|uniform(x, y)|	随机生成下一个实数，它在[x,y]范围内。|

### Python 三角函数

|函数	|描述|
|--|--|
|acos(x)	|返回x的反余弦弧度值。|
|asin(x)|	返回x的反正弦弧度值。|
|atan(x)|	返回x的反正切弧度值。|
|atan2(y, x)|	返回给定的 X 及 Y 坐标值的反正切值。|
|cos(x)|	返回x的弧度的余弦值。|
|hypot(x, y)|	返回欧几里德范数 sqrt(x*x + y*y)。|
|sin(x)|	返回的x弧度的正弦值。|
|tan(x)|	返回x弧度的正切值。|
|degrees(x)|	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0|
|radians(x)|	将角度转换为弧度|

### Python 数学常量

|常量	|描述|
|pi	|数学常量 pi（圆周率，一般以π来表示）|
|e	|数学常量 e，e即自然常数（自然常数）。|

## Python 字符串

### Python 访问字符串中的值
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

Python 访问子字符串，可以使用方括号来截取字符串，如下实例：

实例(Python 3.0+)
```python
#!/usr/bin/python3
 
var1 = 'Hello World!'
var2 = "OuFungwah"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
```

### Python 转义字符

|转义字符|	描述|
|\(在行尾时)|	续行符|
|\\|	反斜杠符号|
|\'|	单引号|
|\"|	双引号|
|\a|	响铃|
|\b|	退格(Backspace)|
|\e|	转义|
|\000|	空|
|\n|	换行|
|\v|	纵向制表符|
|\t|	横向制表符|
|\r|	回车|
|\f|	换页|
|\oyy|	八进制数，yy代表的字符，例如：\o12代表换行|
|\xyy|	十六进制数，yy代表的字符，例如：\x0a代表换行|
|\other|	其它的字符以普通格式输出|

### Python 字符串运算符

|操作符|	描述	|实例|
|---|---|---|
|+	|字符串连接|	a + b 输出结果： HelloPython|
|*	|重复输出字符串|	a*2 输出结果：HelloHello|
|[]|	通过索引获取字符串中字符|	a[1] 输出结果 e|
|[ : ]|	截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。|	a[1:4] 输出结果 ell|
|in|	成员运算符 - 如果字符串中包含给定的字符返回 True|	'H' in a 输出结果 True|
|not in|	成员运算符 - 如果字符串中不包含给定的字符返回 True|	'M' not in a 输出结果 True|
|r/R|	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。|	|
|%|	格式字符串|	请看下一节内容。|

### Python 字符串格式化

```python
#!/usr/bin/python3
 
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
```

| 符   号|	描述|
|--|--|
|      %c|	 格式化字符及其ASCII码|
|      %s|	 格式化字符串|
|      %d|	 格式化整数|
|      %u|	 格式化无符号整型|
|      %o|	 格式化无符号八进制数|
|      %x|	 格式化无符号十六进制数|
|      %X|	 格式化无符号十六进制数（大写）|
|      %f|	 格式化浮点数字，可指定小数点后的精度|
|      %e|	 用科学计数法格式化浮点数|
|      %E|	 作用同%e，用科学计数法格式化浮点数|
|      %g|	 %f和%e的简写|
|      %G|	 %f 和 %E 的简写|
|      %p|	 用十六进制数格式化变量的地址|

辅助指令

|符号|	功能|
|--|---|
|*|	定义宽度或者小数点精度|
|-|	用做左对齐|
|+|	在正数前面显示加号( + )|
|`<sp>`|	在正数前面显示空格|
|#|	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')|
|0|	显示的数字前面填充'0'而不是默认的空格|
|%|	'%%'输出一个单一的'%'|
|(var)|	映射变量(字典参数)|
|m.n.|	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)|

### Python 三引号

三引号支持字符串换行声明

```Python
#!/usr/bin/python3

print """哈哈哈哈哈。。。。
就啊可是打开垃圾
slkajkdjlaksd
卡拉斯京两节课。。。"""
```

这个方式非常有利于写 SQL 语句和 HTML 语句

### Python String内置函数

序号	方法及描述
1	
capitalize()
将字符串的第一个字符转换为大写

2	
center(width, fillchar)


返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
3	
count(str, beg= 0,end=len(string))


返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
4	
bytes.decode(encoding="utf-8", errors="strict")


Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
5	
encode(encoding='UTF-8',errors='strict')


以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6	
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

7	
expandtabs(tabsize=8)


把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
8	
find(str, beg=0 end=len(string))


检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
9	
index(str, beg=0, end=len(string))


跟find()方法一样，只不过如果str不在字符串中会报一个异常.
10	
isalnum()


如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
11	
isalpha()


如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
12	
isdigit()


如果字符串只包含数字则返回 True 否则返回 False..
13	
islower()


如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
14	
isnumeric()


如果字符串中只包含数字字符，则返回 True，否则返回 False
15	
isspace()


如果字符串中只包含空白，则返回 True，否则返回 False.
16	
istitle()


如果字符串是标题化的(见 title())则返回 True，否则返回 False
17	
isupper()


如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
18	
join(seq)


以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
19	
len(string)


返回字符串长度
20	
ljust(width[, fillchar])


返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
21	
lower()


转换字符串中所有大写字符为小写.
22	
lstrip()


截掉字符串左边的空格或指定字符。
23	
maketrans()


创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
24	
max(str)


返回字符串 str 中最大的字母。
25	
min(str)


返回字符串 str 中最小的字母。
26	
replace(old, new [, max])


把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
27	
rfind(str, beg=0,end=len(string))


类似于 find()函数，不过是从右边开始查找.
28	
rindex( str, beg=0, end=len(string))


类似于 index()，不过是从右边开始.
29	
rjust(width,[, fillchar])


返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30	
rstrip()


删除字符串字符串末尾的空格.
31	
split(str="", num=string.count(str))


num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
32	
splitlines([keepends])


按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
33	
startswith(str, beg=0,end=len(string))


检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
34	
strip([chars])


在字符串上执行 lstrip()和 rstrip()
35	
swapcase()


将字符串中大写转换为小写，小写转换为大写
36	
title()


返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37	
translate(table, deletechars="")


根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
38	
upper()


转换字符串中的小写字母为大写
39	
zfill (width)


返回长度为 width 的字符串，原字符串右对齐，前面填充0
40	
isdecimal()


检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

## Python 列表

Python 中的列表类似与 Java 的 List，但是不同之处在于 Python 的 list 不限制存放的数据的类型，不同类型数据可以存放到同一个 list

## Python 元组

Python 的元组与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号，列表使用方括号。

元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

## 安装 beautifulsoup4

python -m pip install beautifulsoup4 --user

