# Android Service

服务是 Android 四大空间之一，多用于后台处理业务。

## 1、Service 的生命周期：

对于 Service 来说，不同的启动方式有不同的生命周期

### 1.1、startService

* context.startService()
* onCreate()
* onStartCommand()
* context.stopService()
* onDestory()

用此方法启动的 Service 只有在它自己调用了 stopSelf() 或外界调用 stopService 才会停止，否则会一直运行至内存不足被收走

### 1.2、bindService

* bindService()
* onCreate()
* onBind()
* unbindService()
* onUnbind()
* destory()

用此方式启动的服务会在所有绑定该服务的组件解绑后销毁，调用 stopService 也没有用

### 1.3、 混合型  

先 bind 再 start ，会在 start 后执行一次 startCommand() 不会再次执行 onCreate()

不管先 bind 还是 先 start，只要 start 了，服务就只能自己 stopSelf 或 stopService 才能停下来

