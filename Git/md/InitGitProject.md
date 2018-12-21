# Git 入门 -- 上传项目至 Git 仓库

|author|Crazywah|
|-----|-------|
|Date|2018-12-21|

前提：有 Git 环境

## 一、配置 Git 的通用设置

Git 的配置都存放在 config 文件中，一共有三个级别的 config：系统级、用户级、仓库级。

1. **系统级**：即使用当前安装了 Git 的系统上所有用户的 Git 配置。
    * 对应信息存放在 `/etc/gitconfig` 文件中
    * 使用 ```git config --system``` 进行读写
2. **用户级**：即登录到当前系统的用户所有 Git 项目的通用配置。
    * 对应信息存放在` ~/.gitconfig` 或 `~/.config/git/config`文件中
    * 使用 ```git config --global``` 进行读写
3. **仓库级**：即当前 Git 项目的配置。
    * 对应信息存放在项目根目录下` .git/config`文件中
    * 使用 ```git config``` 进行读写

***注意下面的 [--system|--global] 的意思是可取这之中的其中一值或都不取。意思分别对应上述的三种级别的配置***

**用户名**：在 Git 中用户名用于刻印在每一次的提交中，主要用于识辨某行代码、某次提交的作者是谁

1. 查看：

```git config [--system|--global] user.name```

2. 修改：

```git config [--system|--global] user.name "name"```

**用户邮箱**：用户邮箱是提供给代码阅读者联系代码作者用的

1. 查看：

```git config [--system|--global] user.email```

2. 修改：

```git config [--system|--global] user.email "email@xx.com"```

**默认编辑器**：设置默认编辑器的目的是在于当有需要输入文字信息的地方，Git 可以调起这个编辑器。（没有 Git 仓库级）

1. 查看：

```git config [--system|--global] core.editor```

2. 修改：

```git config [--system|--global] core.editor [vim|nano|emacs|编辑器名称]```

***查看所有配置：**

```git config --list```

## 二、初始化项目

先进入工程的根目录，在工程根目录下运行 Git 初始化命令 ```git init```

当运行完了这个命令以后，根目录下会生成一个 .git 的隐藏文件夹，这个子目录含有你初始化的 Git 仓库中所有的必须文件，这些文件是 Git 项目管理的核心。

此时，项目仅仅是有了必要文件，你的项目的文件还没开始被 Git 跟踪。

***PS：.git 是一个隐藏文件夹。查看目录下隐藏文件 ```ls -la```***

## 三、添加跟踪文件

为了让 Git 知道我们需要跟踪哪些文件，我们使用：```git add [文件]```来添加跟踪文件

列举一下常用的：

1. 添加单个文件

```git add test.c```

2. 添加所有文件

```git add .``` 或 ```git add *```

3. 添加所有某类型文件

```git add *.c```

4. 修改已跟踪的文件也需要调用 add 命令将文件暂存，暂存以后的文件才能被提交

## 四、提交更新

当我们添加了新的文件或修改了原有文件，想要保存当前工程的文件状态时，我们就需要提交命令了。

```git commit```

此时会调起 shell 环境默认的编辑器（一般为 vim 或 emacs），或者是你在 Git 全局变量 config 中设置好的编辑器。

或者我们可以在提交命令后面添加 -m 指令直接添加提交信息。

```git commit -m '本次提交文件改变的说明'```

在 -m 指令前面添加 -a 即可绕过 add  命令执行

```git commit -a -m '本次提交文件改变的说明'```

**忽略文件的用法后补**

## 五、在 Git 仓库中建立项目

在 Github （或其他服务器上的 Gitlab ）上创建好项目，创建好项目以后复制项目地址：

https协议：```https://github.com/Username/XXXproject.git```

或：

ssh协议：
```git@github.com:Username/XXXproject.git```

***这个两个协议的地址在 Github 或 GitLab 的网站中都有提供；其中若要使用 ssh 协议必须配置 ssh 公钥***

## 六、为工程添加 GitLab 或 GitHub 的远端关联

进行到当前这一步时，本地的 Git 和 远端的仓库都算是建立完成了，我们需要做的就是将两者关联起来。

先给远端链接一个代号，方便使用

使用 `git remote add [代号] 链接地址` 来给远端的链接一个代号名称，

通常：

```git remote add origin git@github.com:Username/XXXproject.git```

其中 origin 可以替换成你喜欢的单词，但是常规上都命名为 origin。

## 七、推送本地提交至远端

将本地的分支推送并关联到远端我们使用 `git push -u [远端代号|远端链接] 分支名 `

如：

```git push -u origin master```

或：

```git push -u git@github.com:Username/XXXproject.git master```

## 参考资料：

[《ProGit》](https://git-scm.com/book/en/v2)

