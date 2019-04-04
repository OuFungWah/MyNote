# Java 多线程

## 1、Java 多线程的实现：

自定义一个实现 Runnable 的类定义线程要运行的代码块。

```java
Runnable runnable = new Runnable(){

    @Override
    public void run(){
        // todo 这里实现线程的运行内容
    }

}

```

将定义好的 Runnable 对象传入 Thread。

```java

Thread thread = new Thread(runnable);
thread.start();

```

此时线程就运行起来了。

## 2、使用线程池

Executor 采用了命令模式

```java

Executors.newCachedThreadPool();
Executors.newFixedThreadPool(5);
Executors.newSingleThreadExecutor();
Executors.newScheduledThreadPool(5);

```

常用的有四种线程池 
* CachedThreadPool

    缓存线程池，为所需的任务（Runnable）新建线程，只有在回收就线程资源时才会停止创建新线程

* FixedThreadPool

    可复用线程池，线程池中只有限定好的数量，任务会被安排进去，线程池中的线程数不够分配时，等待有空闲线程在分配进去复用线程

* SingleThreadExecutor

    单线程线程池，线程池中只有一个线程可用，任何任务只能等前面的任务执行完毕才能进入线程中运行

* ScheduledThreadPool

    可计划运行线程的时间的线程池

## 3、 解决资源共享

### 3.1、synchronized 关键字

在方法前面添加 synchronized 关键字可以保证某方法在同一时间内只有一个线程调用，其他线程会进入等待。保证该方法必定会在某线程执行完才会轮到其他线程调用。

```java 

// 此类型亦称为对象锁，同一对象
public synchronized void f(){

}

```

或只锁住方法的某一块

```java

// 此类型锁为类锁
public void f(){
    synchronized(XX.class){
        // TODO do something
    }
}

```


### 3.2、volatile 关键字

该关键字用于修饰用于同步的变量，它能保证所有对变量的修改能即时地被其他访问该变量的线程看到，即所有的修改都可以即时地反映到其他读取中。

一般用于没有被 synochronized 修饰其修改与读取的变量上。


### 3.3、sleep 与 wait 区别

sleep() 只让出了CPU时间，而不释放锁，待时间过完随即继续完成任务

wait() 将会让出资源锁并将当前线程挂起，待有其notify() 或 notifyAll() 调用时才会重新请求资源锁并继续完成任务。

```java

public class SleepWaitTest {

    public static void main(String[] args) {
        Thread a = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (SleepWaitTest.class) {
                    System.out.println("线程 a 要开始了");
                    System.out.println("线程 a 发现无法处理，先挂起, 等待 b 线程处理，我先释放 SleepWaitTest 锁");
                    try{
                        SleepWaitTest.class.wait();
                    }catch (Exception e){
                        e.printStackTrace();
                    }
                    System.out.println("线程 a 重新获得了 SleepWaitTest 锁");
                    System.out.println("线程 a 处理完毕");
                }
            }
        });
        Thread b = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized (SleepWaitTest.class) {
                    System.out.println("线程 b 要开始了");
                    System.out.println("线程 b 困了要睡觉");
                    try{
                        Thread.sleep(4000);
                    }catch (Exception e){
                        e.printStackTrace();
                    }
                    System.out.println("线程 b 睡完觉了");
                    System.out.println("线程 b 处理完毕！ 告诉线程 a 可以了");
                    SleepWaitTest.class.notify();
                }
            }
        });
        a.start();
        try {
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        b.start();
    }

}


```