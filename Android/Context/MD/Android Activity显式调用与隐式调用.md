# Android Activity 显式调用与隐式调用
* Author:CrazyWah
* Date:2018.01.24
* CopyRight:crazywah.com

Android的Activity调用方式分为两种：显示和隐式
## 1、显式调用
显式调用即在Intent中加入明确跳转意图的Component（构件）
### 1.1、代码示例：
#### 1.1.1、于构造函数中加入Component的参数(常用方法)
```Java

Intent intent = new Intent(this,TargetActivity.class);
startActivity(intent);

```
#### 1.1.2、Intent创建后再加入Component
```Java

Intent inetnt = new Intent();
ComponentName componentName = new ComponentName(this,TargetActivity.class);
intent.setComponent(componentName);
startActivity(intent);

```

#### 1.1.3、设置setClass()或setClassName()方法
```Java

Intent intent = new Intent();
intent.setClass(this,TargetActivity.class);
//第二个参数为Activity所在的完整包名
//intent.setClassName(this,"com.crazywah.TargetActivity.class")
//intent.setClassName(this.getPackageName(),"com.crazywah.TargetActivity.class")

```

### 1.2、显式调用的特点
显式调用最大的特点是其调用的目标Activity是明确的，即在新建Intent的过程之中该Activity已经是指定好的，适用于转跳向明确目标的Activity，如：点击登陆按钮转跳向登陆页面等场景。

## 2、隐式调用
隐式调用即在Intent中不指明跳转意图的Component，而是给Intent添加Action，让有对应Action的Activity响应这个意图

### 2.1、代码示例：
我们在创建意图的同时需要指定Action，希望具有什么Action的Activity可以响应我们的意图

#### 2.1.1、于构造函数指定Action
```Java
  //Action的内容可自定，只要在Activity中的Intent-filter有相同Action即可
  Intent intent = new Intent("send");
  startActivity(intent);
```

#### 2.1.2、新建意图后再指定Action
```java
  //Action的内容可自定，只要在Activity中的Intent-filter有相同Action即可
  Intent intent = new Intent();
  intent.setAction("send");
  startActivity(intent);
```

#### 2.1.3、manifest文件中有对应intent-filter的Activity（或者可以是其他应用提供有对应的Activity）
```xml
  <activity
    android:name=".activity.MainActivity">
    <intent-filter>
      <action android:name="send"/>
      <category android:name="android.intent.category.DEFAULT"/>
    </intent-filter>
  </activity>
```

### 2.2、匹配原则

#### action的匹配：（action是隐式intent中必须携带的一个属性）
action的匹配原则：只需要intent中的所有action和IntentFilter的action中的其中一个完全匹配即可完成匹配
##### action 在 manifest文件中声明
```xml

<activity android:name=".TargetActivity">
    <intent-filter>
        <!-- name属性的值可以是任意有意义的字符串 -->
        <action android:name="com.crazywah.exmple.itent.move"/>    
        <!--这个是由于category的匹配规则导致必须加入的部分-->
        <category android:name="android.intent.category.DEFAULT"/>
    </intent-filter>
</activity>

```
##### 在需要隐式调用的地方
```java

    Intent intent = new Intent();
    intent.setAction("com.crazywah.exmple.itent.move");
    startActivity(intent);

```
#### category的匹配：（intent中可以没有该属性）
category的匹配原则为：。当intent中有intent可以不携带category的值去匹配，因为系统在调用时自动给intent添加一个默认的category--android.intent.category.DEFAULT。由于这个原因，Activity在用到IntentFilter的时候必须添加一个值为android.intent.category.DEFAULT的category标签。

##### category在manifest中的声明
```xml

<activity>
    <intent-filter>
        <action android:name="com.crazywah.exmple.itent.move"/>    
        <!--这个是由于category的匹配规则导致必须加入的部分-->
        <category android:name="android.intent.category.DEFAULT"/>
        <!--自定义的category-->
        <category android:name="com.crazywah.exmple.category.a"/>
    </intent-filter>
</activity>

```
##### 在需要隐式调用的地方
```java

    Intent intent = new Intent();
    intent.setAction("com.crazywah.exmple.itent.move");
    intent.addCategory("com.crazywah.exmple.category.a");
    startActivity(intent);

```
#### data的匹配：（指定用于操作的数据类型）
我们需要先了解到data的构成
```
<scheme>://<host>:<port>/[<path>|<pathPrefix>|<pathPattern>]
```

组件 | 意义 | 内容
--- | --- | ---
Scheme|URI的模式|如：http、file、content
Host|URI的主机名|如：www.baidu.com
Port|URI中的端口号|如：80
Path|完整路径信息|如：abc、img/abc
pathPattern|路径信息|同上，但增加一个表示一个或任意多个的通配符*
pathPrefix|路径前缀|

data匹配原则：要求Intent中必须含有data数据。

### 2.3、隐式调用的特点
隐式调用最大的特点就是不需要明确地知道目标Activity的名字，我们自需要发出Action等待它来响应就好了，适用于转跳不明确或不需明确相应功能的Activity，如：调用系统发短信的Activity等第三方Activity等场景

## 3、总结
两种方式相对比：
显式调用强调的是转跳至明确目标Activity
隐式调用强调的是转跳至实现相应功能的Activity
