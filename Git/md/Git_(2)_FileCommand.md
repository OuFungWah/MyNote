# Git（二）文件操作

|Author|2015-区枫华|
|------|----------|
|Date|2019-05-06|

在[Git（一） 基础知识]()中提到了，Git 的文件管理包括了：文件跟踪、文件暂存、文件提交以及文件推送。本文章将详细讨论与这些操作相关的常用的命令

## 一、Git 工作流程与命令行

### 1.1、获取一个代码仓库

可以是通过初始化获得也可以是从远端仓库拷贝下来的代码仓库。如果是下拉的代码仓库，我们能看见的文件就都已经是从代码仓库复制到工作区的快照了。

为本地项目创建 Git 仓库：

 `git init <参数>` 

从远端仓库拷贝代码仓库：

 `git clone <参数>` 

### 1.2、查看当前工作空间文件状态（非必要、可在任何时候执行）

使用以下命令**获取当前工作区的文件的状态**。

`git status [选项] <参数>`

<!--输入命令行后我们能看到类似于这样的输出：

```
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   md/VersionControl.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   "../Tentcoo/Tentcoo-Studio-Android-\347\253\257\345\237\271\345\205\273\350\256\241\345\210\222.md"

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        md/Branch.md
        md/src/
        ../Plan/

```

我们来一段一段分析 `git status` 所获取到的信息：

```
On branch master
Your branch is up to date with 'origin/master'.
```

⬆️这一段告诉我们，当前工作区的文件是来自于哪个分支，该分支对应远端的哪一个分支。

```
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   md/VersionControl.md
```

⬆️这一段主要告诉我们当前已经暂存了哪些文件。

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   "../Tentcoo/Tentcoo-Studio-Android-\347\253\257\345\237\271\345\205\273\350\256\241\345\210\222.md"
```

⬆️这一段显示的是当前已修改但是还没暂存的文件。

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        md/Branch.md
        md/src/
        ../Plan/
```

⬆️这一段显示的是当前还没有开始跟踪的文件。

**相信眼利的小伙伴已经发现了，每一个文件状态列表开始之前都有一个小括号（）提醒，里面描述的命令行就是该种状态下文件可以执行的操作**
-->

### 1.3、跟踪文件

当我们在项目中**新建了某些文件**，Git 并不会自动帮我们把这些文件纳入到跟踪范围内 *（高级的编译器会自动帮我们跟踪新建的文件，如：Android Studio、Eclipse等等）*。这时候就需要我们自己手动告诉 Git 我想跟踪某某文件的状态。**使用以下命令就可以让 Git 跟踪指定文件**。

 `git add [选项] <参数>` 

<!--举几个例子：

* `git add *`: 跟踪当前目录下所有文件

* `git add .md`:跟踪当前目录下所有的 .md 后缀的文件。还可以`git add *.md`，效果相同。

* `git add dic`:跟踪名为 dic 的文件夹

* `git add README.md`:跟踪名为 README.md 的文件-->

### 1.4、暂存文件

基本不可能在一次工作过程中一个文件都不修改，如果都不修改那就不是工作，而是查阅。而**修改过的文件是处于已修改状态**，所有的**要提交到 Git 仓库的文件都必须先添加到暂存区**。暂存文件用的依旧是 `git add` 命令。其实 `git add` 是一个多功能命令，对于未跟踪的文件，add 是跟踪该文件；对于已修改文件，add 是暂存该文件。

**注意**：暂存了的文件如果再次修改，其状态会回到已修改，需要再次用命令行来暂存已修改文件。

### 1.5、提交文件

当文件都已经暂存好了以后我们就可以开始提交文件到 Git 仓库了。**提交文件使用以下命令行**：

`git commit [选项] <参数>`

<!--当然，其实我们还可以偷懒，直接在 commit 的时候顺便将所有的已修改文件暂存起来。在上面的命令中添加一个 `-a`，这样就会自动将所有更改过的文件添加到暂存区并提交。

`git commit -a -m <commit 的信息>`

举几个例子：

* `git commit -m '修改了XXX文件'`:提交我们使用 git add 暂存的文件'

* `git commit -a -m '修改了XXX文件；添加相关图片'`:提交所有修改过、新增加或者已删除的文件。 -->

### 1.6、推送提交至远端仓库（非必要）

如果这个项目是一个远端项目，做完本地修改并已经推送到了本地 Git 仓库后还应该将文件同步到远端服务器，此时只需要使用推送提交的命令行即可（设置远端源、远端追踪以及多分支合并与推送等复杂操作在后面的总结中再讨论）。

推送代码到远端（前提已设置远端并已跟踪远端分支）：

`git push [选项] <参数>` 


## 一、文件跟踪|暂存文件 `git add`

所有需要提交到版本仓库的文件都是必须先添加到暂存区的，而不管跟踪新文件还是暂存已修改文件 add 都是将文件添加到暂存区。命令行 `git add` 是一个多功能命令，对于未跟踪的文件，该命令是将未跟踪文件纳入 Git 版本管理；对于已跟踪并已修改的文件则是将该文件添加到暂存区。

命令格式:

`git add [选项] <参数>`

下面将详细介绍该命令的常用选项以及参数

### 1.1、参数

#### 1.1.1、<文件的相对路径>

暂存/跟踪 某个具体的文件到暂存区

`git add <文件的相对路径>`

例如：

* 暂存/跟踪 本目录下的 README.md 文件：<br>`git add README.md`

* 暂存/跟踪 本目录下某 src 文件夹中的 README.md 文件：<br>`git add src/README.md`

#### 1.1.2、<文件夹的相对路径>

暂存/跟踪 文件夹中所有未 暂存/跟踪 的文件

`git add <文件夹名>`

例如：

* 暂存/跟踪本目录下的 src 文件夹中所有未暂存/跟踪的文件：<br>`git add src`

#### 1.1.3、<*> (通配符)

暂存/跟踪 所有匹配的文件

`git add <*>`

例如：

* 暂存/跟踪 所有文件:<br>`git add *`

* 暂存/跟踪 所有的Java格式文件:<br>`git add *.java`

### 1.2 选项

#### 1.2.1、预览(--dry-run)

展示将会暂存/跟踪的文件或被忽略文件，并不实际暂存/跟踪。

`git add [-n|--dry-run] <参数>`

例如：

* 展示本次即将缓存的所有文件<br>`git add -n *`

```
➜  Git git:(master) ✗ git add -n *
add 'Git/md/Git_(1)_Basic.md'
add 'Git/md/Git_(2)_FileCommand.md'
```

#### 1.2.2、强行(--force)

强行 暂存/跟踪 文件，不管 .gitignore 是否无视了该文件。

`git add [-f|--force] <参数>`

例如：

* 强行 暂存/跟踪 一个名为 README.md 的文件<br>`git add -f README.md`

#### 1.2.3、交互式（--interactive）

该命令将打开命令行中的交互 add 工具，我们只要再按照显示的指令来进行操作即可。

`git add --interactive`

显示：

```
➜  Git git:(master) ✗ git add --interactive 
           staged     unstaged path
  1:    unchanged        +1/-1 Git/md/Git_(1)_Basic.md
  2:       +10/-0       +74/-1 Git/md/Git_(2)_FileCommand.md

*** Commands ***
  1: status	  2: update	  3: revert	  4: add untracked
  5: patch	  6: diff	  7: quit	  8: help
What now>
```

## 二、