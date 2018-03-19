# Android IntentFilter意图过滤器
我们都知道Android的Activity（或service）调用分为显式调用和隐式调用。
* 显式调用即在转跳意图中指明目标Activity的名字（甚至详细至报名，看调用方式）；
* 隐式调用即只需要指明需要的action（动作），data（数据），category（类别） 然后让系统筛选出对应的Activity来匹配，如果有多个Activity匹配则由用户选择由何Activity来响应。

***注意：Android官方不推荐使用隐式调用启动Service，因为Service对用户不可见，不使用隐式调用启动service是为了防止不必要的内存空间的浪费。Android 5.0以后隐式调用Service时会引起异常***
## 显式调用代码实例：
### 一、在构造函数指定目标Activity
（惯用方法）
```java

    Intent intent = new Intent(this,TargetActivity.class);
    startActivity(intent);

```
### 二、先创建intent再设置转跳目标Activity
setComponent()
```java

    Intent intent = new Intent();
    ComponentName componentName = new ComponentName(this,TargetActivity.class);
    //后面两种写法多用于跨应用调用
    //ComponentName componentName = new ComponentName(this,"com.crazywah.exmple.TargetActivity");
    //ComponentName componentName = new ComponentName(this.getPackageName(),"com.crazywah.exmple.TargetActivity");
    intent.setComponent(componentName);
    startActivity(intent);
    
```
setClass() / setClassName()

```java

    Intent intent = new Intent();
    intent.setClass(this,TargetActivity.class);
    //后面两种写法多用于跨应用调用
    //intent.setClassName(this,"com.crazywah.exmple.TargetActivity");
    //intent.setClassName(this.getPackageName(),"com.crazywah.exmple.TargetActivity");
    startActivity(intent);

```
### 三、隐式调用
隐式调用因为牵涉到了action，category和data的匹配问题，所以使用起来相较于显式调用会比较复杂
* action(操作):该元素指明的是该Activity是用于执行何种操作的。会被声明了相应的action的隐式意图匹配
* category(分类)

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