# Git 总结 Tag 的使用与管理

|author|Crazywah|
|-|-|
|Date|2018.12.24|

## Tag：标签

Tag 的中文意思是标签。即因为有特殊意义（例如发布新版本、重要功能稳定版本）而给当前分支的某次提交做一个标志。表明该次提交以后代码处于某种值得标记的状态。方便我们以后因为某些原因将代码回溯到这个提交上。

标签可以被创建、删除、但建议不修改

## 一、创建标签

在 Git 中有两种 tag，一种是轻量Tag，一种是附注tag。

### 附注标签

附注 Tag 就是一个有附有许多详细信息（打标签的作者、打标签作者的邮箱、打标签时间、Tag 备注信息）的一个 Tag，例如说我们即将上线某某版本，给当前代码打个标签并附注一些版本信息，我们就会使用附注 Tag。

添加附注 Tag 我们使用 `git tag -a [标签名] -m '附注信息'` 命令

如：

```git tag -a v2.0.0 -m '1.上线XXX功能 2. 修复XXX Bug'```

如果不添加 -m 参数的话，只运行 `git tag -a XXX` 命令行会打开文本编辑让你输入附注信息

如：

```git tag -a v1.0.1```

终端会打开命令行编辑器（vim 或 nano 等文本编辑器）

```

#
# Write a message for tag:
#   v1.0.1
# Lines starting with '#' will be ignored.
~
~
~
~
~
~
~
~
~
~
~
"~/Documents/Demo/Git/.git/TAG_EDITMSG" 5L, 84C
```

编辑完成以后再保存，附注 Tag 就添加完成了

### 轻量标签

轻量 Tag 即不需要太多信息的一个 Tag，仅仅是需要一个 Tag 标注当前代码状态。可能是某次提交完毕了以后代码处于一个比较好的状态，但是还没悉数完成版本功能，想临时保存当前代码状态以防后面开发出问题可以回溯到当前状态，我们就给当前代码打一个轻量 Tag

打轻量 Tag 我们使用`git tag [名称]`

如：

```git tag finish_watermark```

### 给过去的提交记录打标签

当我们想给准确的某个提交打上 Tag 时，我们需要做两件事情：

1. 使用 log 找出我们想要添加 tag 的提交的校验和：

```git log --pretty=oneline```

我们能看到提交的日志：

```
eee24d49a094eca565142d34dc6cfb67d10b128e (HEAD -> feature/1.0.0) add python execute system command
061e2ddb95552769ec8329c788da0071d9b36ad9 add three new line
d48bc8eb2b334f4c0daaad30c0c8cea5374fd900 add a line call hahahah
db99e6f220d5231d2ffcd8759d2e7b76f7b5e732 
```

能看到，每条提交记录的最前面都有属于它自己的校验和，将它复制下来为下一步铺路

2. 用命令 `git tag [名称] [校验和]` 来给具体的某个提交添加 Tag

如我们要给上面的 “add a line call hahahah” 那次提交添加 Tag：

```git tag first_commit d48bc8eb2b334f4c0daaad30c0c8cea5374fd900```

如果你觉得整个校验和太长，你可以只选取其中的一小段：

```git tag first_commit d48bc8e```

当然，这个也支持附注 Tag：

```git tag -a second_commit_1.0.0 d48bc8e -m 'this is the second time commit in this project'```

这时候我们再 log 一次看看：

```
eee24d49a094eca565142d34dc6cfb67d10b128e (HEAD -> feature/1.0.0) add python execute system command
061e2ddb95552769ec8329c788da0071d9b36ad9 (source/feature/1.0.0) add three new line
d48bc8eb2b334f4c0daaad30c0c8cea5374fd900 (tag: second_commit_1.0.0, tag: first_commit) add a line call hahahah
db99e6f220d5231d2ffcd8759d2e7b76f7b5e732
```

对应的提交记录上多了我们添加的两个 tag

**注意：名字都是可以随便填的，符合你的实际需求即可**

## 二、同步标签至远端

普通的 `git push` 并不会把标签推送到远端，如果需要把标签推送至远端我们需要一个标签一个标签地去推送，就像是把本地分支关联到远端一样。

使用 `git push [远端代号|远端链接] [tag名称]`

如：


```git push origin v1.0.0```

如果我们想要一次推送所有不在远端的标签到远端我们可以使用：

```git push --tags```

推送完毕以后我们来查看一下远端的标签

```git ls-remote --tags```

从以下返回信息中可以看出，v1.0.0 已经被推至了远端

```
From git@github.com:XXX/XXX.git
db99e6f220d5231d2ffcd8759d2e7b76f7b5e732	refs/tags/v1.0.0
```

## 三、删除标签

### 删除本地标签

有时候出于某些原因（或打错标签、或标签不想要了）我们需要删除某个标签，此时我们鸠需要使用 `git tag -d [标签名]` 的命令了

如删除本地名为 v1.0.0 的标签

```git tag -d v1.0.0```

### 删除远端标签

上述命令只能删除本地标签，如果我们执行 `git ls-remote` 命令我们可以发现其实远端还是有 v1.0.0 标签，如果我们想要把远端的标签也删除掉的话则需要使用 `git push [远端代号|远端链接] -d [标签名]` 这条命令。

如我们要把远端的分支 v1.0.0 删除掉的话：

```git push origin -d v1.0.0```

再查询远端的情况我们可以发现 v1.0.0 标签已经被删除了

## 四、修改标签

### 修改本地标签附注

当我们想要修改某个标签的时候给 `git tag` 添加 `-f` 参数

假设我们现在有这样的一个标签

```
Author: OuFungWah <diegobruce@163.com>
Date:   Sun Dec 23 22:26:43 2018 +0800

    add python execute system command

diff --git a/first.py b/first.py
index cc26e28..a5f7e07 100644
tag v1.0.0
Tagger: OuFungWah <diegobruce@163.com>
Date:   Tue Dec 25 21:42:53 2018 +0800

hahahhahaha

commit eee24d49a094eca565142d34dc6cfb67d10b128e (HEAD -> feature/1.0.0, tag: v1.0.0, aos/feature/1.0.0)
Author: OuFungWah <diegobruce@163.com>
Date:   Sun Dec 23 22:26:43 2018 +0800

    add python execute system command
```

如我们想要修改名为 v1.0.0 且附注信息为：“hahahhahaha”的这个标签：

```git tag -f v1.0.0 -m 'this is the right annotation'```

而后我们再用 `git show v1.0.0` 查看该标签时可以发现附注已经改变为我们新修改的内容了

### 覆盖远端标签：

因为当远端已经存在同名标签时，从本地推送已经修改过的标签上去远端简单地用 `git push` 会被远端拒绝的，原因是重名了。这时候我们就需要添加 `-f` 参数，将远端的
标签给覆盖掉

例如我们要将远端的 v1.0.0 标签覆盖掉：

`git push -f origin v1.0.0`

这样就可以成功覆盖远端的标签了

## 五、查看标签

### 查看本地标签

```git tag```

```git log```

```git show [标签名]```

### 查看远端标签

```git ls-remote -t```

## 六、检出标签

检出（checkout）标签的意思是回溯代码状态至打标签时的状态。因为标签只是一个指向当前分支某次具体提交的一个指针，它不能被改变，当我们想回溯到这个标签的代码状态的时候，只能在这个标签指向的提交上新建立一个分支。

我们使用 `git checkout -b [分支名] [标签名]` 来检出一个标签

如：

```git push -b v1_0_0 v1.0.0```