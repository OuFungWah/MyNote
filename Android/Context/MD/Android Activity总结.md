# `Activity`
## `Activity` 介绍
`Activity`作为Android的四大组件之一，其重要性已经不需要强调了，是使用最频繁的组件之一。<br/>
`Activity`说白了就是用户能看见的界面

## `Activity`生命周期
我们先来看看生命周期的图<br/>
![Android_lifecycle](src/activity_lifecycle.png)

* `onCreate()`:表示Activity正在被创建，一般在这个方法里面我们会进行一些初始化操作
* `onReStart()`:表示Activity正在重启，一般为当前Activity从不可见重新变成可见，当用户切回桌面，Activity的onPasue()和onStop()就会被执行，再回到页面时就会执行onReStart()的内容
* `onStart()`:表示Activity正在创建，页面已经可见，但是还没出现在前台，无法与用户交互，用户也无法看见
* `onResume()`:表示Activity已经可见，而且已经在前台运行
* `onPause()`：表示Activity正在停止，必须是onPause()紧接着就调用onStop(),但如果立即返回到Activity就会返回到onResume()方法重新执行生命周期（难以人手操作达到）
* `onStop()`：表示Activity已经退出前台，执行必要的清除工作（尽量不耗时）
* `onDestroy()`：表示Activity被销毁时执行的方法

## 特别情况下的`Activity`生命周期：
### 情况一：系统参数发生改变
当系统中的参数发生改变，导致Activity的UI需要更新时
* 当前Activity：
  1. `onPause()`
  2. `onSaveInstanceState()`：存储当前Activity的状态信息
  3. `onStop()`
  4. `onDestroy()`
* 新的Activity
  1. `onCreate()`
  2. `onReStart()`
  3. `onStart()`
  4. `onRestoreInstanceState()`：读取被销毁的Activity的状态信息
  4. `onResume()`

### 情况二：内存不足导致优先级低的Activity被销毁
Activity的优先级：
1. 前台Activity---正在运行，与用户直接交互中的Activity
2. 可见但是非前台Activity---比如Activity弹出了一个对话框，虽然无法与用户交互，但是依旧可见
3. 后台Activity---已被暂停的Activity，比如执行了onStop()的Activity

*PS：其生命周期过程与第一种情况相同*

## Activity的启动模式
Activity的启动模式有四种：standard(标准模式)、singleTop(栈顶复用模式)、singleTask(栈内复用模式)、singleInstance(单例模式)
### standard(标准模式)
标准模式即Activity的默认启动模式，特点为**无论当前需要启动的Activity是否已经有实例存在于任务栈中，系统都创建一个新的Activity实例压进任务栈中**
![标准模式图示](src/diagram_backstack.png)

### singleTop(栈顶复用模式)
栈顶复用模式即**当要新建的Activity已经处于栈顶的时候即重用这个栈顶的Activity**，即Activity将不需要调用onCreate()和onStart()等方法（因为实例已经存在，不需重建）。其他非栈顶Activity依旧需要新建。

### singleTask(栈内复用模式)
与栈顶模式相似，但是栈内复用即**当需要创建新Activity的时候，先搜索当前栈中是否已存在该Activity的实例，如果存在则不重新创建，而是把原有的实例调至栈顶然后调用其onNewIntent()方法刷新其参数**。如果没有则创建一个新的该Activity实例并压至栈顶。注意，但需要复用的Activity不在栈顶时，该任务栈中在该Activity之上的所有Activity将出栈

**例如：<br/>现在又A、B两个Activity，A为singleTask模式，B为standard模式<br/>启动应用，任务栈新建Activity A，栈内为“A”，然后我们用startActivity的方式跳转到B，此时栈内为“AB”<br/>当我们在B中使用startActivity的方式跳转到A时，因为A是singleTask模式，所以栈内已经有A的实例时我们就需要把A以上的所有Activity进行出栈操作，此时栈内情况为“A”**

### singleInstance(单例模式)
与栈内复用模式相类似，但是单例更加强势，**单例模式则是在所有任务栈中，同一个Activity的实例只允许有一个，并且该Activity独占一个任务栈**

### 修改Activity启动模式的方法
#### 一、修改Mainifest文件中的标签属性
```xml
<manifest>
  <application>
    <activity
      android:name=".activity.SecondActivity"
      android:allowTaskReparenting="true"
      android:launchMode="singleTask"
      android:taskAffinity="com.crazyWah.task1"/>
  </application>
</manifest>
```
* 在需要修改启动模式的Activity的对应标签里面添加指定 launchMode属性
* taskAffinity 属性是为activity指定它所在的栈，默认情况下，所有的Activity都是运行在以应用包名为名的任务栈中的
* allowTaskReparenting 属性是指当前这个Activity如果被其他app所启动而运行在其他app的任务栈时，当用户启动当前的app时，该Activity实例会转移回到当前app的任务栈中复用

#### 二，在新建转跳意图时指定Activity的启动模式
```Java
staryActvity(new Intent(this,SecondActivity.class).addFlag(Intent.FLAG_ACTIVITY_NEW_TASK));
```

***重要的FLAG的作用总汇***
* `FLAG_ACTIVITY_NEW_TASK`:指定singleTask启动模式
* `FLAG_ACTIVITY_SINGLE_TOP`:指定singleTop模式
* `FLAG_ACTIVITY_CLEAR_TOP`:一般与singleTask配套使用。如果被启动的Activity实例已经存在则将其上方的所有Activity都出栈
* `FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS`:具有此标志的Activity将不会出现在历史记录仲（即平时按多任务键以后的应用列表）

### 两种启动模式修改方法的区别
1. 使用Intent修改的方法优先级比manifest修改的优先级高，即两种同时存在时，以Intent中的FLAG为准
2. Intent修改的方式无法指定singleInstance模式
3. manifest修改的方式无法指定clearTop模式
