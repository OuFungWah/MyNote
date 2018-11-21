* `startActivity(Intent intent)` ->
* `startActivity(Intent intent, @Nullable Bundle options)` ->

    默认 requestCode 为 -1

* `startActivityForResult(@RequiresPermission Intent intent, int requestCode,@Nullable Bundle options)` ->

    判断是否为嵌套的 Activity 的子 Activity <br>
    如是:则将 start 动作交给 mParent<br>

* `mParent.startActivityFromChild(this, intent, requestCode, options);`

    如否：将请求交给 mInstrumentation，并在 Application 的主线程中执行

* `mInstrumentation.execStartActivity(this, mMainThread.getApplicationThread(), mToken, this,intent, requestCode, options);`

    mInstrumentation 是 Instrumentation 的一个实例，该对象的实例化优先于App 的任何代码。负责监控 App 和 系统的所有交互

* 在 mInstrumentation 内部，mInstrumentation 内部开始对所有已经注册了的，在本设备上的所有 App 的监视器对象开始匹配，找到指定 Action、Category、Activity 的 Activity。

实际上当启动一个 app 的时候都会实例化一个 Instrumentation 对象，且 Instrumentation 在每个 Activity 跳转的时候都会用到且其内部类 ActivityMonitor 会监控 activity 的，并且生命周期是由 ActivityMonitor 调用的