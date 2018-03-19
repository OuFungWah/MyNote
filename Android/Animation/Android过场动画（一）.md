# Android过场动画（一）
未经修改的app，`Android`自己有默认的过场动画。但是有时候开发者遇到的开发需求没有这么的简单，需要改变一些入场和出场的动画，这时候就需要我们通过代码来实现了。
## Tween动画
使用Tween动画定义过场动画
### 一、Tween过场动画的基础使用
#### 1）定义好Tween的xml动画
* 定义一个当前`Activity`跳出的动画xml文件
```xml
<!-- zoom_out.xml -->
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <scale
        android:duration="1000"
        android:fromXScale="1.0"
        android:fromYScale="1.0"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toXScale="0.0"
        android:toYScale="0.0" />
</set>
```
* 定义进入下一个`Activity`的动画xml文件
```xml
<!-- zoom_in.xml -->
<?xml version="1.0" encoding="utf-8"?>
<set xmlns:android="http://schemas.android.com/apk/res/android">
    <scale
        android:duration="1000"
        android:fromXScale="0.0"
        android:fromYScale="0.0"
        android:pivotX="50%"
        android:pivotY="50%"
        android:toXScale="1.0"
        android:toYScale="1.0" />
</set>
```
<br/>*因为这个定义动画的过程在前面的文章中已经介绍过了，所以就不详述了*

#### 2）调用设置转跳动画的方法
在适当的地方：如`startActivity()`或`finish()`方法后面调用
```java
  //转跳到指定的Activity
  startActivity(new Intent(this,SecondActivity.class));
  //设置页面转跳时的入场和出场动画
  overridePendingTransition(R.anim.zoom_in, R.anim.zoom_out);
```
*PS：如果是想在结束页面时设置动画，即在调用finish()的后面加入overridePendingTransition()设置动画*

### 二、方法详解
#### 设置`Activity`转跳入场与出场动画`void overridePendingTransition (int enterAnim,int exitAnim)`

```java
  //设置页面转跳时的入场和出场动画
  overridePendingTransition(R.anim.zoom_in, R.anim.zoom_out);
```
##### 参数`int enterAnim`：
  * 该参数为入场动画的xml文件资源
  <br/>*PS：若无动画效果则传0*

##### 参数`int exitAnim`：
  * 该参数为退场动画的xml文件资源
  <br/>*PS：若无动画效果则传0*

### 三、总结：
使用Tween动画做`Activity`的跳转动画就和直接用Tween做动画效果一样，使用方便，但是灵活性有所欠缺，是一个折中的方案

## Android5.0以上动画
上面介绍的是使用Tween动画进行自定义过场动画，但是能做出来的效果有限，在Android5.0以后，Google为开发者提供了一些新的炫酷的过场动画使用
### 一、基础使用
#### 1）定义好`Activity`
按照自己的需要将`Activity`定义好。这里使用`FirstActivity`和`SecondActivity`。
#### 1.SP）*如果是Share模式还需要在xml中做一些操作*
如果是使用`Share`的转跳模式，我们需要为被共享的控件定义一个`transtionName`
```xml
<!-- FirstActivity的布局中 -->
<ImageView
        android:id="@+id/img"
        android:layout_width="150dp"
        android:layout_height="150dp"
        android:layout_alignParentBottom="true"
        android:layout_alignParentRight="true"
        android:layout_margin="10dp"
        android:src="@mipmap/icon"
        android:transitionName="img" />

<!-- SecondActivity的布局中 -->
<ImageView
      android:layout_width="150dp"
      android:layout_height="150dp"
      android:layout_alignParentRight="true"
      android:layout_marginRight="25dp"
      android:layout_marginTop="175dp"
      android:src="@mipmap/icon"
      android:transitionName="img" />
```
*PS：共享的控件，第一个页面的控件必须有id，第二个页面则按自己的需求，没有硬性规定；必须拥有相同的transtionName，其他参数可按需要决定随意*
#### 2）在当前`Activity`定义`ActivityOptions`
因为这些都是Android5.0过后才引入到API中的，所以需要在使用之前加入版本判断
```java
    //判定版本是否为Android5.0以上
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP){
      //新建动画ActivityOptions
      ActivityOptions activityOptions = ActivityOptions.makeSceneTransitionAnimation(getActivity());
    }
```
#### 3）新建转跳页面的Intent
```java
    //新建转跳页面的意图
    Intent intent = new Intent(FirstActivity.this,SecondActivity.class);
```
#### 4）转跳页面
把我们前面定义好的`intent`和`activityOptions`的信息传到下一个`Activity`
```java
    //调用Activity的转跳Activity方法
    startActivity(intent,activityOptions.toBundle());
```

#### 5）目标`Activity`的操作
其实各个动画变化的重点决定性因数都在转跳目标的`Activity`里面,在这个`Activity`里面是决定使用何种动画方式转跳的。<br/>可以使用的转跳类有`Fade`(渐变)，`Slide`(各元素从下至上地飞入)，`Explode`(各元素从四面八方飞入)。`Share`(两个`Activity`共享控件)的方式会比较特别。
```java
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //判断手机版本是否适合
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            //设置转跳效果为淡入淡出（Fade）
            getWindow().setEnterTransition(new Fade());
        }
         setContentView(getLayoutId());
   }
```
*PS：注意必须在Activity的setContentView()调用之前调用设置进入动画的方式*

#### 5.SP）*特别的：Share的转跳方式*
在要用`Share`方式转跳到的`Activity`中设置视窗特点.*注意，需要在创建ActivityOptions的时候必须携带上两个Activity共享的*
```java
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //判断手机版本是否适合
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            //设置视窗特点为内容动画
            getWindow().requestFeature(Window.FEATURE_CONTENT_TRANSITIONS);
        }
         setContentView(getLayoutId());
   }
```

### 二、方法详解
在`Lollipop`的动画里面主要使用到的方法就是设置转跳参数和设置`Activity`的进入动画等的方法
#### 1）设置`ActivityOptions`的参数<br/>`ActivityOptions makeSceneTransitionAnimation (Activity activity, Pair...<View, String> sharedElements)`
该方法主要是传递参数用的，如果是Share方法的话需要加上转跳的共享组件元素作为参数传递
```java
  //不带共享元素作为参数
  ActivityOptions activityOptions = ActivityOptions.makeSceneTransitionAnimation(FirstActivity.this);
  //携带共享元素作为参数
  ActivityOptions activityOptions = ActivityOptions.makeSceneTransitionAnimation(FirstActivity.this,Pair.create((View)img,"img"),Pair.create((View)tv,"tv"),Pair.create(view,"view"));
```
##### 参数`Activity activity`
  * 当前的`Activity`的资源对象

##### 参数` Pair...<View, String> sharedElements`
  * 绑定需要共享的各个元素控件本身和他们对应的String类型的`transitionName`<br/>如：`Pair.create((View)img,"img")`创建img控件和其transtionName对应的Pair对象
  * *PS：`...`是Java中的数组的一种表示方法,作为参数时，数组长度按照传入的相应对象个数决定*

#### 2）转跳Activity`void startActivity (Intent intent,Bundle options)`
携带参数跳转到`Intent`中指定的`Activity`
```Java
  //携带activityOptions信息跳转Activity
  startActivity(intent, activityOptions.toBundle());
```

##### 参数`Intent intent`
  * 前面定义好准备的转跳`Intent`（意图）

##### 参数`Bundle options`
  * 前面定义好的`ActivityOptions`转成常用于`Activity`之间通讯的`Bundle`的形式，此参数可以为空

#### 3）设置视窗的进入动画`void setEnterTransition (Transition transition)`
设置视窗的入场动画
```java
//设置入场动画为淡入淡出
getWindow().setEnterTransition(new Fade());
```
##### 参数`Transition transition`
  * 此参数为继承了`Transition`类的类的对象，可以是Google定义好的`Fade`类，`Slide`类，`Explode`类，也可以是自定义的继承Transition的类对象。

#### 3.SP）*特别用于Share转跳类型的方法* 设置视窗特性`boolean requestFeature (int featureId)`
```java
//设置视窗特性为内容动画
getWindow().requestFeature(Window.FEATURE_CONTENT_TRANSITIONS);
```
##### 参数`int featureId`
  * 此参数为`Window`类中定义好的`int`类型常量（当然也可以自己传个1或其他int类型数据，但不推荐）

### 三、总结
Lollipop的转场动画，无论是自定义的自由性，还是Google定义好的Transition的子类都比起Tween动画更加的灵活和炫酷
