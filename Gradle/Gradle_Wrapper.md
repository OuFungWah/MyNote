# Gradle Wrapper 相关配置

***@Author oufenghua***

## 0、前言

> 使用 ```gradle wrapper``` 命令行可以新建一个标准的 Gradle 工程

## 1、命令行的可用选项

### 选项1: ```--gradle-version [version]```

示例：以下代码代表将会使用 2.4 版本的 Gradle 进行 Wrapper 的构建
```
gradle wrapper --gradle-version 2.4
```

所以 ```[version]``` 代表的就是希望使用的 Gradle 的版本。

*具体的版本数字可以到[官网](https://gradle.org/releases/)上查看*


### 选项2: ```--gradle-distrubution-url [url]```

示例：以下代码代表将会通过 [https://services.gradle.org/distributions/gradle-6.4-rc-3-bin.zip](https://services.gradle.org/distributions/gradle-6.4-rc-3-bin.zip) 下载 Gradle 并创建 Wrapper

```
gradle wrapper --gradle-distrubution-url https://services.gradle.org/distributions/gradle-6.4-rc-3-bin.zip
```

以上的 Url 是从 Gradle 的[官方 distribution](https://services.gradle.org/distributions/) 中获取的，如果大家有需要可以到上面找自己合适的版本。**而这个配置选项的本意是如果 Gradle 官方地址万一遭遇封禁可以试着用其他可以访问到的路径进行下载**。

## 2、Gradle Wrapper 的配置文件 gradle-wrapper.properties 的内容

打开刚创建的 Wrapper 工程中的 gradle-wrapper.properties 文件我们可以看到以下内容：

```
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-6.3-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

解释：

|字段|说明|备注|
|--|--|--|
|distributionBase|下载 Gradle 压缩包后解压的主目录|-|
|distributionPath|相对于 distributionBase 的解压后的压缩包路径|-|
|**distributionUrl**|**用于下载 Gradle 压缩包的 Url**|**比较常修改的部分**|
|zipStoreBase|存放 Zip 包根目录目录|-|
|zipStorePath|存放 Zip 包相对于 zipStoreBase 的相对目录|-|
