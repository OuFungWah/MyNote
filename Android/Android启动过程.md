# Android 启动过程

## 1、Android 系统启动过程

1. 开机：bootloader 启动**内核**和**init进程**
2. **init进程**分裂出更多的 **deamons（守护进程）**，用于处理底层硬件（USB、Android debug等）相关接口
3. **init进程启动 Zygote 进程**。这个进程初始化了第一个 VM 并预加载了 framework 和众多 App 多需要的资源，然后开启一个 socket 接口监听新建 App 进程的请求，一旦收到请求就会基于已加载的VM孵化出新的 VM 出来管理 App。
4. **init进程启动 runtime 进程**
5. **启动 SystemServer**。Zygote 孵化出一个超级管理进程 **System Server**，负责启动所有的系统核心服务（ 例如Activity Manager Service, 硬件相关的Service等）。
6. 启动第一个 App 手机的 Home App

## 2、Android App 启动过程

1. 某处事件触发 startActivity
2. 通过 Binder IPC 机制将意图传递到 ActivityManagerService 并执行以下操作：
    1. 通过 resolveIntent() 收集 Intent 的信息
    2. 指向信息存储到一个 intent 中
    3. 通过 grantUriPermissionLocked() 方法验证是否有足够权限打开目标 Activity
    4. 如果有权限，在新的 task 中启动目标 Activity
    5. 检查目标 Activity 的 ProcessRecord 是否存在 不存在则新建进程来实例化目标 Activity
    6. 调用 startProcessLocked() 方法来创建新的进程
3. 创建进程：
    1. 通过 socket 创建新进程的消息传到 Zygote 进程，Zygote 调用 ZygoteInit.main() 方法实例化 ActivityThread 并返回新进程的 id
    2. ActivityThread 通过 Looper.prepare() 和 Looper.loop() 开启消息循环
    3. 将生成的 ActivityThread 和对应的 Application 绑定起来。ActivityThread 对象调用 bindApplication() 方法，然后发送 BIND_APPLICATION 消息到消息队列，最终通过 handleBindApplication() 方法处理，然后调用 makeApplication() 方法来加载 App 的 class 到内存中