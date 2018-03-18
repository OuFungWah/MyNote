# Android Activity 显式调用与隐式调用
Android的Activity调用方式分为两种：显示和隐式
## 显式调用
显式调用即在Intent中加入明确跳转意图的Component（构件）
### 代码示例：
#### 一、于构造函数中加入Component的参数(常用方法)
```Java

Intent intent = new Intent(this,TargetActivity.class);
startActivity(intent);

```
#### 二、Intent创建后再加入Component
```Java

Intent inetnt = new Intent();
ComponentName componentName = new ComponentName(this,TargetActivity.class);
intent.setComponent(componentName);
startActivity(intent);

```

#### 三、设置setClass()或setClassName()方法
```Java

Intent intent = new Intent();
intent.setClass(this,TargetActivity.class);
//第二个参数为Activity所在的完整包名
//intent.setClassName(this,"com.crazywah.TargetActivity.class")
//intent.setClassName(this.getPackageName(),"com.crazywah.TargetActivity.class")

```

## 显示调用的特点
