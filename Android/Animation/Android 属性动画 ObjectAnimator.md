# Android 属性动画 ObjectAnimator
`ObjectAnimator`其实是Google对`ValueAnimator`的一个封装类，它的底层还是用`ValueAnimator`实现的
## 一、`ObjectAnimator` 的Java基础使用
### 1）初始化设置需要`ObjectAnimator`演算的对象`view`
获取调用静态方法返回的`ObjectAnimator`对象。
```Java
  //给ObjectAnimator 绑定控件：view 设定控件内部变化的属性：translationY 设置属性变化起始值：从100到0
  ObjectAnimator objectAnimator = ObjectAnimator.ofFloat(view, "translationY", 100.0f，0.0f);

```
### 2）设置动画相关的属性
调用`ObjectAnimator`里面的相关方法去设置动画的属性值，如：运行时间，更换需要动画对象，更换变化的属性等等
```java

  //设置动画的运行时间为1000ms（1s）
  objectAnimator.setDuration(1000);

```
### 3）开始动画
在需要开启动画的地方调用开始方法即可开始动画
```Java
  //开始动画
  objectAnimator.start();
```

### *PS：可以使用匿名对象简化动画的调用*
由于`ObjectAnimator`内部已经为我们做了许多的优化，所以我们只需要几小段的代码即可完美调用，鉴于此，我们可以把小段的代码结合为一句代码
```Java
  //浓缩版代码，效果和上面的一致
  ObjectAnimator.ofFloat(view, "translationY", 100，0).setDuration(1000).start();
```
## 二、`ObjectAnimator`的`xml`基础使用
### 1）在`res`目录睇下新建`animator`资源文件夹
在 res 文件夹下新建一个 animator 文件夹

![](src/animator文件夹.jpg)

### 2）在`animator`目录下新建`xml`资源文件并设置好属性
```xml
<objectAnimator xmlns:android="http://schemas.android.com/apk/res/android"
    android:duration="1000"
    android:propertyName="translationY"
    android:repeatCount="infinite"
    android:repeatMode="reverse"
    android:valueFrom="0"
    android:valueTo="100"
    android:valueType="floatType" />
```
  * duration = 动画持续时间 [ int ]
  * propertyName = 需要被改变的属性的变量名 [ string ]
  * repeatCount = 动画重复次数 [ int | infinite]
  * repeatMode = 动画重复的方式 [ reverse | restart ]
  * valueFrom = 属性值的起始值 [ int | float | color ]
  * valueTo = 属性值的终止值 [ int | float | color ]
  * valueType = 属性值的数据类型 [ intType | floatType | colorType | pathType ]

### 3）在Java代码中引用
因为我们只是定义了一个`xml`文件，实际上的对象我们还是需要使用`AnimatorInflater`来帮助获取到相应参数的对象
```Java
//使用 AnimatorInflater 的 loadAnimator 方法实现xml中定义好的 ObjectAnimator。需要强制类型转换
ObjectAnimator objectAnimator = (ObjectAnimator) AnimatorInflater.loadAnimator(getContext(),R.animator.object_anim1);
```
### 4）绑定需要实现动画效果的`View`
目前得到得是一个定义好的动画，我们还需要为动画指定一个实施的对象
```java
//将view这个控件绑定到当前定义好的动画上
objectAnimator.setTarget(view);
```
### 5）开始动画
*PS：参照 一、3）*

## 三、`ObjectAnimator`方法参数详解
`ObjectAnimator`中同样定义好了许多的方法以供我们开发者更灵活地做出我们想要的动画效果

### 1）设置动画运行时间 `void setDuration (long duration)`：
```java
//设置动画运行时间为1000ms,即一秒
objectAnimator.setDuration(1000);
```
##### 参数 `long duration`
  * 向方法里面传递的参数为一个long类型值。为动画运行的毫秒数<br/>
   *PS：1000ms = 1s = 1/60 min*

### 2）设置参数变化范围`ObjectAnimator ofFloat (Object target,String propertyName,float... values)`
给ObjectAnimator设置动画的目标对象，对象需要进行动画的属性命，动画变化的数值

```Java
//设置view的透明度由0变化到1
ObjectAnimator.ofFloat(view, "alpha", 0.0f, 1.0f)
```
#### 参数`Object target`
  * 向方法里面传递一个需要进行动画的对象

#### 参数`String propertyName`
  * 对象里面的属性名
  * 例如是View，View中的 translationX 属性，在传递参数时就写成：
  ```Java
    ObjectAnimator.ofFloat(view, "translationX", 100.0f, 200.0f)
  ```
  如此类推
  * *PS：此参数同样适用于自定义 View 或其他自己定义的属性使用，只要参数在类中有相应的get和set方法*

#### 参数`float... values`
  * 数值变化的关键数值点，即设定好属性需要变化的数值点
  * *PS：不懂可以参照折线图来理解这个数值点的概念*

#### 返回值`ObjectAnimator`
  * 返回一个按照以上参数绑定好的`ObjectAnimator`对象

#### *类似方法*
```Java
//专用于改变颜色数值的方法
ofArgb(Object target, String propertyName, int... values);
//专用于int类型数值变化的方法
ofInt(Object target, String propertyName, int... values);
//专用于多个Float数组的数值变化的方法
ofMultiFloat(Object target, String propertyName, float[][] values);
//专用于多个int数组的数值变化的方法
ofMultiInt(Object target, String propertyName, int[][] values);
```
### 3）设置跟随路径移动`ObjectAnimator ofFloat(Object target, String xPropertyName, String yPropertyName, Path path)`
此方法是先定义好一个路径，然后再让对象在定义好的路径上移动
```Java
        //设置好路径
        Path path = new Path();
        path.moveTo(0.0f,0.0f);
        path.lineTo(0.0f,200.0f);
        path.lineTo(200.0f,200.0f);
        path.lineTo(200.0f,0.0f);
        path.lineTo(0.0f,0.0f);
        path.close();
        //对view这个对象进行动画操作
        ObjectAnimator.ofFloat(view,"translationX","translationY",path).setDuration(3000).start();
```

#### 参数`Object target`
  * 需要进行动画的对象，同 2）

#### 参数`String xPropertyName`
  * 需要执行动画的对象的x值的属性名

#### 参数`String yPropertyName`
  * 需要执行动画的对象的y值的属性名

#### 参数`Path path`
  * 动画的路径
  * *PS：如果对Path类不熟悉可以先去了解一下，后面我也会出相应的文章*

#### 返回值`ObjectAnimator`
  * 返回一个按照以上参数绑定好的`ObjectAnimator`对象

#### 注意事项！
*此方法仅适用于高于Android5.0的系统，需要适当的加入判断，以防报错*

#### *类似方法*
```Java
//专用与int类型数值变化的方法
ofInt(Object target, String xPropertyName, String yPropertyName, Path path)
```

## 四、总结
`ObjectAnimator`相对于直接使用`ValueAnimator`来说，使用更加的简洁，更适合项目开发当中，而且也没有了`ValueAnimator`在7.0以上机型无法运行的问题
