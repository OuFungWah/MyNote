# Android Context
* Author：CrazyWah
* Date：2018.03.15

## 一、什么是Context
相信有做过`Android`应用开发的各位对`Context`这个类型应该是不陌生的，因为到处都有它的身影。如：
```java
  //View的构造函数
  View(Context context){
    ...
  }

  //新建一个View
  View view = new View(context);
```
**那么到底`Context`是什么呢？**

`Context`的中文意思是：上下文、前后关系。那放回到我们`Android`上是什么呢？因为`Android`的应用程序和普通的`Java`程序不一样，`Android`程序是运行在`DVM ( Dalivk Virtual Mechine )`上的，每一个`Android`程序都运行在自己独立的`DVM`上,一个`DVM`对应一个`Linux`的进程,既然每个`Android`程序都拥有一定的系统资源，`Android`程序就需要对它所分配到资源进行一个管理和掌控，而这个资源管理的类就是我们的`Context`了。

`Context`在源码中是这样描述的：

```Java
/**
 * Interface to global information about an application environment.  This is
 * an abstract class whose implementation is provided by
 * the Android system.  It
 * allows access to application-specific resources and classes, as well as
 * up-calls for application-level operations such as launching activities,
 * broadcasting and receiving intents, etc.
 */
```

`Context`一个由`Android`系统提供实现的，拥有应用所处的运行环境的所有信息、能获取到各种应用特有资源和类、能做各种应用层操作操作的接口类

**一个形象生动的理解：** 引用自文章[《Context都没弄明白，还怎么做Android开发？》](https://www.jianshu.com/p/94e0f9ab3f1d)

一个`Android`应用程序，可以理解为一部电影或者一部电视剧，`Activity`，`Service`，`Broadcast Receiver`，`Content Provider`这四大组件就好比是这部戏里的四个主角：胡歌，霍建华，诗诗，Baby。他们是由剧组（系统）一开始就定好了的，整部戏就是由这四位主演领衔担纲的，所以这四位主角并不是大街上随随便便拉个人（new 一个对象）都能演的。有了演员当然也得有摄像机拍摄啊，他们必须通过镜头（`Context`）才能将戏传递给观众，这也就正对应说四大组件（四位主角）必须工作在`Context`环境下（摄像机镜头）。那`Button`，`TextView`，`LinearLayout`这些控件呢，就好比是这部戏里的配角或者说群众演员，他们显然没有这么重用，随便一个路人甲路人乙都能演（可以new一个对象），但是他们也必须要面对镜头（工作在`Context`环境下），所以`Button mButton=new Button（Context）`是可以的。虽然不很恰当，但还是很容易理解的，希望有帮助。

**那么Android中有多少组件是Context呢？**

我们来看一下`Context`的类关系图

![Context类关系图](https://github.com/OuFungWah/FungWahToolsDemo/blob/master/Tutorial/Picture/Context.png)

眼厉的小伙伴应该就看到了熟悉的身影了：`Application`、`Service`和`Activity`。这些都是`Context`，由`Android`系统负责创建的，我们能做的只是提醒`Android`系统我们要用到什么`Context`了，然后系统负责创建。其中的`Application`对象是唯一的，一个应用只有一个`Application`对象

## 二、Context有什么用？
既然通过上面的叙述我们知道`Context`是拥有系统资源的，既然我们都有资源了，那当然是可以“为所欲为”了~~

由于用法众多，这里仅仅举出常用的简单的例子：
```java
  Context context = 获取当前上下文资源对象(根据情况更换为Activity、Service 或 Application) ;
  //创建UI控件
  Button btn = new Button(context);
  //创建跳转意图
  Intent intent = new Intent(context,TargetActivity.class);
  //获取共享偏好设置对象
  SharedPreferences s = context.getSharedPreferences("test",context.MODE_PRIVATE);
  //跳转Activity
  context.startActivity(intent);
  //etc
  ......

```

除了以上给出的例子以外，`Context`还可以发送广播、绑定服务、与当前应用相关的文件操作等等

## 三、总结
这篇文章的主旨意在记录下自己对`Android`中`Context`的思考和理解。希望也可以对各位读到本文章的小伙伴有帮助。
