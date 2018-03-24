# Android Handler+Looper+MessageQueue
## 1、机制简述
## 2、源码分析
## 3、总结

## Handler（处理器）
* 每个Handler对象对应一个相关联的线程（Thread）和一个相关的消息队列（MessageQueue）。
* 处理器会捆绑在创建它的线程上
* Handler会将Message和Runnable交付到对应的MessageQueue上运行

* Handler有两个主要用途
	1. 统筹调度即将要执行的Runnable和Messages
	2. 将要跨线程执行的动作加入队列

* 我们可以通过`post(Runnable)`, `postAtTime(Runnable, long)`, `postDelayed(Runnable, Object, long)`, `sendEmptyMessage(int)`, `sendMessage(Message)`, `sendMessageAtTime(Message, long)`, 和 `sendMessageDelayed(Message, long)`方法来安排Message加入队列中。post开头的这些方法是用于指定你自己定义的Runnable加入队列中的。send开头的这些方法是用于你将数据封装到Bundle中并绑定在Message对象中然后由Handler中的handleMessage()方法进行处理。（当然，你必须先实现Handler的这个方法）

当应用的进程创建时，它的主线程，即用于管理最高级应用对象（如：activity、broadcast、service等）和任何由这些对象所创建的视窗的线程将用于运行MessageQueue消息队列。（说白了就是MessageQueue默认时运行在UI线程上的）。你可以通过Handler进行子线程和UI线程之间的通信。只需要在你的子线程上调用handler的send或post方法即可。你发送至Handler的Message或者Runnable将会在合适的时候被调度至消息队列并且处理。

```java

	//立即发送消息
	public final boolean sendMessage(Message msg)
    {
        return sendMessageDelayed(msg, 0);
    }

    //定时发送Handler信息
    public final boolean sendMessageDelayed(Message msg, long delayMillis)
    {
        if (delayMillis < 0) {
            delayMillis = 0;
        }
        //当前时间+延迟时间 = 目标发送时间
        return sendMessageAtTime(msg, SystemClock.uptimeMillis() + delayMillis);
    }

	//发送消息至Handler，在毫秒级别的时间点准时发送消息：uptimeMillis
    public boolean sendMessageAtTime(Message msg, long uptimeMillis) {
        MessageQueue queue = mQueue;
        if (queue == null) {
            RuntimeException e = new RuntimeException(
                    this + " sendMessageAtTime() called with no mQueue");
            Log.w("Looper", e.getMessage(), e);
            return false;
        }
        return enqueueMessage(queue, msg, uptimeMillis);
    }

    //将Message加入MessageQueue
    private boolean enqueueMessage(MessageQueue queue, Message msg, long uptimeMillis) {
        msg.target = this;
        if (mAsynchronous) {
            msg.setAsynchronous(true);
        }
        return queue.enqueueMessage(msg, uptimeMillis);
    }

	public final boolean post(Runnable r)
    {
       return  sendMessageDelayed(getPostMessage(r), 0);
    }

    public final boolean postAtTime(Runnable r, long uptimeMillis)
    {
        return sendMessageAtTime(getPostMessage(r), uptimeMillis);
    }

    public final boolean postAtTime(Runnable r, Object token, long uptimeMillis)
    {
        return sendMessageAtTime(getPostMessage(r, token), uptimeMillis);
    }

    public final boolean postDelayed(Runnable r, long delayMillis)
    {
        return sendMessageDelayed(getPostMessage(r), delayMillis);
    }

    public final boolean postAtFrontOfQueue(Runnable r)
    {
        return sendMessageAtFrontOfQueue(getPostMessage(r));
    }

	//该方法用于组装Message对象
    private static Message getPostMessage(Runnable r) {
    	获取
        Message m = Message.obtain();
        m.callback = r;
        return m;
    }

    public final boolean sendMessageDelayed(Message msg, long delayMillis)
    {
        if (delayMillis < 0) {
            delayMillis = 0;
        }
        return sendMessageAtTime(msg, SystemClock.uptimeMillis() + delayMillis);
    }

    public boolean sendMessageAtTime(Message msg, long uptimeMillis) {
        MessageQueue queue = mQueue;
        if (queue == null) {
            RuntimeException e = new RuntimeException(
                    this + " sendMessageAtTime() called with no mQueue");
            Log.w("Looper", e.getMessage(), e);
            return false;
        }
        return enqueueMessage(queue, msg, uptimeMillis);
    }
```

获取Message对象
```java
	private static Message getPostMessage(Runnable r) {
        Message m = Message.obtain();
        m.callback = r;
        return m;
    }
```

A Handler allows you to send and process Message and Runnable objects associated with a thread's MessageQueue. Each Handler instance is associated with a single thread and that thread's message queue. When you create a new Handler, it is bound to the thread / message queue of the thread that is creating it -- from that point on, it will deliver messages and runnables to that message queue and execute them as they come out of the message queue.

There are two main uses for a Handler: (1) to schedule messages and runnables to be executed as some point in the future; and (2) to enqueue an action to be performed on a different thread than your own.

Scheduling messages is accomplished with the `post(Runnable)`, `postAtTime(Runnable, long)`, `postDelayed(Runnable, Object, long)`, `sendEmptyMessage(int)`, `sendMessage(Message)`, `sendMessageAtTime(Message, long)`, and `sendMessageDelayed(Message, long)` methods. The post versions allow you to enqueue Runnable objects to be called by the message queue when they are received; the sendMessage versions allow you to enqueue a Message object containing a bundle of data that will be processed by the Handler's handleMessage(Message) method (requiring that you implement a subclass of Handler).

When posting or sending to a Handler, you can either allow the item to be processed as soon as the message queue is ready to do so, or specify a delay before it gets processed or absolute time for it to be processed. The latter two allow you to implement timeouts, ticks, and other timing-based behavior.

When a process is created for your application, its main thread is dedicated to running a message queue that takes care of managing the top-level application objects (activities, broadcast receivers, etc) and any windows they create. You can create your own threads, and communicate back with the main application thread through a Handler. This is done by calling the same post or sendMessage methods as before, but from your new thread. The given Runnable or Message will then be scheduled in the Handler's message queue and processed when appropriate.

## Looper
## MessageQueue