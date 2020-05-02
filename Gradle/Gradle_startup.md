# Gradle 入门

***@Author oufenghua***

## 什么是 Gradle？

Gradle 是一款非常优秀的构建系统工具，在 Android 中主要就是透过 Gradle 来串联所有的模块，所以学习 Gradle 在 Android 中十分的有必要。

**以下提到的命令都是在 Mac 环境下使用的，Windows 可以根据 Windows 配置环境变量的方法**

## 安装配置 Gradle

* 准备好 Java 环境：[教程链接](https://www.jianshu.com/p/de3b2f1a3534)
* 下载合适版本的 Gradle 包：[官网链接](https://gradle.org/releases/)
* 解压下载好的 Gradle 的 zip 包（假设解压后的地址是: /Users/xxx/Documents/tools/gradle-6.3）
* 打开 bash_profile 环境变量文件
```
open ~/.bash_profile 
```
* 配置 .bash_profile 的内容
```
# gradle 相关
GRADLE_HOME=/Users/xxx/Documents/tools/gradle-6.3
PATH=$PATH:${GRADLE_HOME}/bin 
export GRADLE_HOME
export PATH
```
* 刷新 .bash_profile 文件

```
source ~/.bash_profile
```
* 验证 gradle 安装情况

```
gradle -v
```
如果可以看到命令行中输出对应的 gradle 版本等信息时说明我们安装成功了！

## 初始化一个 Gradle 项目

Gradle Wrapper，所谓 wrapper 就是对 Gradle 的一个统一封装，其目的是为了不会出现同一个项目内出现因为 Gradle 版本不一致所导致的麻烦。所以当我们新建一个 Gradle Wrapper 的时候会给整个工程目录指定具体某个版本的 Gradle（版本一般默认当前建立 wrapper 的 gradle 版本，也可以自己指定），整个项目都可以直接使用这个 Gradle 进行配置和执行相关 Gradle 脚本。

### 构建一个 Gradle Wrapper
在 demo 目录下执行以下命令

```
gradle wrapper
```
 该命令会在当前目录下新建以下内容：

``` 
--- demo
    --- gradle
        --- wrapper
            --- gradle-wrapper.jar              <--- gradlew 这个可执行文件只是负责调用，实际的业务逻辑全是调用的这个 jar 里面的内容
            --- gradle-wrapper.properties       <--- 当前 gradle 工程的 gradle 相关配置
    --- gradlew         <--- Linux/Mac 下的可执行文件
    --- gradlew.bat     <--- Windows 下的可执行文件
```

***（Gradle Wrapper 的具体相关内容可以参考[Gradle Wrapper 相关配置](https://github.com/OuFungWah/MyNote/blob/master/Gradle/Gradle_Wrapper.md)）***

至此新的 gradle 项目就可以开始使用了。

### 简单使用示例：

在刚新建的目录的根目录中新添加一个 build.gradle 文件。

PS：build.gradle 是每个 gradle 的 task 集合的文件，所有可执行的 task 都定义在这个文件当中

新建后在里面增加以下代码

```
task firstTask{
    println 'My first gradle code!!'
}
```
在当前目录下执行以下命令（推荐）：
```
./gradlew firstTask
```
或者
```
gradle -q firstTask
```
即可在命令行中看到如下输出：
```
➜  demo git:(master) ✗ ./gradlew firstTask

> Configure project :
My first gradle code!!

BUILD SUCCESSFUL in 899ms
```

到此，我们第一次运行 gradle 脚本就大功告成啦！后面将会详细介绍更多 Gradle 相关的知识。