# ActionBar
* Author:CrazyWah
* Date:2018.05.29
* CopyRight:crazywah.com

## 1、CoordinatorLayout

### 1.1、概述：

<!-- CoordinatorLayout is a super-powered FrameLayout.<br/> -->
CoordinatorLayout 是一个加强版的FrameLayout

<!-- CoordinatorLayout is intended for two primary use cases: -->
CoordinatorLayout 被预期在以下两种基本的情况使用的：

<!-- As a top-level application decor or chrome layout
As a container for a specific interaction with one or more child views
By specifying Behaviors for child views of a CoordinatorLayout you can provide many different interactions within a single parent and those views can also interact with one another. View classes can specify a default behavior when used as a child of a CoordinatorLayout using the CoordinatorLayout.DefaultBehavior annotation. -->
* 将 CoordinatorLayout 用作最顶层的布局或第二层的布局。CoordinatorLayout 作为在特殊交互中的协调者，你可以通过给 CoordinatorLayout 的子 View 指定特定的 Behavior 来让在 CoordinatorLayout 里面的子 View 两两之间相互影响。
<!-- Behaviors may be used to implement a variety of interactions and additional layout modifications ranging from sliding drawers and panels to swipe-dismissable elements and buttons that stick to other elements as they move and animate. -->
* Behaviors 或许会被用在交互的多样化上；作为除了侧拉栏之类的滑动消失的控件以外的一个交互系列；把按钮依附在其他控件上以达至按钮能相应它们的滑动或动画。
<!-- Children of a CoordinatorLayout may have an anchor. This view id must correspond to an arbitrary descendant of the CoordinatorLayout, but it may not be the anchored child itself or a descendant of the anchored child. This can be used to place floating views relative to other arbitrary content panes. -->

CoordinatorLayout 的子 View 一般会有一个锚点。这个锚点 View 的必须是 CoordinatorLayout 的子 View ，但是不允许是子 View 自己本身或者是 CoordinatorLayout 的子 View 的子 View 。这个锚点的设置可以使一个浮动的 View 与其他内容关联起来。

<!-- Children can specify insetEdge to describe how the view insets the CoordinatorLayout. Any child views which are set to dodge the same inset edges by dodgeInsetEdges will be moved appropriately so that the views do not overlap. -->

子 View 可以通过设置 insetEdge 来描述该 View 是怎么内嵌与 CoordinatorLayout 的。任何通过设置 dodgeInsetEdge 来嵌入 CoordinatorLayout 的 View 都会被适当地移动，以防止子 View 之间重叠、遮挡

实现更多酷炫的效果可以通过自定义 Behavior 来实现

### 1.2、基本使用

## 2、AppBarLayout

### 2.1、概述：

<!-- AppBarLayout is a vertical LinearLayout which implements many of the features of material designs app bar concept, namely scrolling gestures. -->

AppBarLayout 是一个实现了许多 Material AppBar 概念的垂直方向的线性布局，即各种滑动手势。

<!-- Children should provide their desired scrolling behavior through setScrollFlags(int) and the associated layout xml attribute: app:layout_scrollFlags. -->

在 AppBarLayout 中的各个子 View 应该通过 setScrollFlags(int) 或者 app:layout_scrollFlags 来提供它们所想要实现的滑动方式对应的 Behavior

<!-- This view depends heavily on being used as a direct child within a CoordinatorLayout. If you use AppBarLayout within a different ViewGroup, most of it's functionality will not work. -->

这个 View 大量依赖于用作 CoordinatorLayout 的直接子 View，如果你把 AppBarLayout 用于其他 ViewGroup 中，它许多的功能将会失效

<!-- AppBarLayout also requires a separate scrolling sibling in order to know when to scroll. The binding is done through the AppBarLayout.ScrollingViewBehavior behavior class, meaning that you should set your scrolling view's behavior to be an instance of AppBarLayout.ScrollingViewBehavior. A string resource containing the full class name is available. -->

AppBarLayout 同样需要一个分开的滑动同级 View（即同样是 CoordinatorLayout 的直接子 View ）来告知它何时滑动。对这个同级 View 的绑定需要通过 AppBarLayout.ScrollingViewBehavior 完成。

## 3、ToolBar

### 3.1、概述：

<!-- A standard toolbar for use within application content. -->

一个用于 App 内容的标准工具栏（即常用的顶栏）

<!-- A Toolbar is a generalization of action bars for use within application layouts. While an action bar is traditionally part of an Activity's opaque window decor controlled by the framework, a Toolbar may be placed at any arbitrary level of nesting within a view hierarchy. An application may choose to designate a Toolbar as the action bar for an Activity using the setActionBar() method. -->

ToolBar 是对一个 App 的 ActionBar 该有的内容的归纳。当一个 Action Bar 作为传统的由整个框架控制 Activity 的不透明的一部分，它可以内嵌于整个 View 嵌套系统的任意一层（即 ToolBar 并没有特定地放置要求，可以随意放置）。一个 App 可以通过调用 setActionBar() 方法来选择特定的 ToolBar 作为 Activity 的 ActionBar。

<!-- Toolbar supports a more focused feature set than ActionBar. From start to end, a toolbar may contain a combination of the following optional elements: -->

ToolBar 提供了比 ActionBar 更多的特性来设置。从开头到尾段，一个 ToolBar 可能包括一下可选元素：

<!-- A navigation button. This may be an Up arrow, navigation menu toggle（棒形纽扣、切换键）, close, collapse（折叠、崩塌、毁坏）, done or another glyph（象形文字） of the app's choosing. This button should always be used to access other navigational destinations within the container of the Toolbar and its signified content or otherwise leave the current context signified by the Toolbar. The navigation button is vertically aligned within the Toolbar's minimum height, if set. -->

* 一个否定按钮。这可以是一个向上箭头、否定的菜单切换按钮、关闭按钮、折叠按钮、完成或者其他代表关闭 App 的象形文字。该按钮应该总是用于访问 ToolBar、包含该 ToolBar 或离开当前内容一类的否定的目的（即常见的返回键）。如果设置了这个否定按钮，它将会垂直于整个 ToolBar 的最小高度
<!-- A branded logo image. This may extend to the height of the bar and can be arbitrarily（武断的、随意的） wide. -->
* 一个 App 的 logo（标志图标）。这个可能因 ToolBar 的高度而扩增，而宽度可以是随意的。
<!-- A title and subtitle. The title should be a signpost for the Toolbar's current position in the navigation hierarchy（等级制度） and the content contained there. The subtitle, if present（在场的，礼物） should indicate（指示，暗示，标示） any extended information about the current content. If an app uses a logo image it should strongly consider omitting（忽略） a title and subtitle. -->
* 一个标题和副标题。标题应该是当前内容的一个标示。如果有副标题，那么它应该是进一步概括当前页面的内容。如果一个 App 使用了 logo 图标，那么它非常应该忽略掉标题和副标题。
<!-- One or more custom views. The application may add arbitrary child views to the Toolbar. They will appear at this position within the layout. If a child view's Toolbar.LayoutParams indicates（指示，暗示，标示） a Gravity value of CENTER_HORIZONTAL the view will attempt（尝试，企图） to center within the available（可获得） space remaining in the Toolbar after all other elements have been measured. -->
* 一个或多个的内嵌 View。一个应用可以添加任意子 View 到 ToolBar。它们会出现在 Toolbar 的这个位置。如果子 View 的 Toolbar.LayoutParams 设置了重心值为 CENTER_HORIZONTAL，该子 View 会尝试获得 ToolBar 在计算完其他控件以后的剩余空间的中心。
<!-- An action menu. The menu of actions will pin to the end of the Toolbar offering a few frequent（惯有的，频繁的）, important or typical actions along with an optional overflow menu for additional actions. Action buttons are vertically aligned（校准，使...一直线） within the Toolbar's minimum height, if set. -->
* 一个操作菜单。该菜单依靠在 Toolbar 的末端并在菜单内额外提供了一些频繁使用、重要的或典型的操作。如果设置了的话，菜单内的每个选项高度由 ToolBar 的最小高度决定，

<!-- In modern Android UIs developers should lean more on a visually（视觉上） distinct（清晰的、确定无疑、不同的） color scheme（计划、阴谋、体系） for toolbars than on their application icon. The use of application icon plus title as a standard layout is discouraged（使灰心、阻拦） on API 21 devices and newer. -->
对现代的 Aandroid UI 开发者来说应该多学习视觉上不同的颜色搭配来决定 ToolBar 和 App logo 之间的颜色。

### 基本使用

以下是 Android 官网对 ToolBar 的基本使用的归纳 [传送门](https://developer.android.com/training/appbar/setting-up?hl=zh-cn)

#### 添加依赖包

为项目添加 v7 appcompat 支持库。

#### 继承 AppCompatActivity

为了能更好地配合 ToolBar 的使用，我们选用 AppCompatActivity 作为 Activity 的父类

#### 保证单一 ActionBar

由于 Android 系统默认为每个 App 提供 ActionBar，为了防止同时出现两个 ActionBar 在屏幕上，我们需要把 App 的主题修改为 NoActionBar 把默认的 ActionBar 禁掉

```xml
<application
    android:theme="@style/Theme.AppCompat.Light.NoActionBar"
    />
```

#### 在 layout 文件中添加 ToolBar

在你希望添加 ToolBar 的 Activity 布局中添加 ToolBar 标签，设置你需要的部分属性

```xml

<android.support.v7.widget.Toolbar
   android:id="@+id/my_toolbar"
   android:layout_width="match_parent"
   android:layout_height="?attr/actionBarSize"
   android:background="?attr/colorPrimary"
   android:elevation="4dp"
   android:theme="@style/ThemeOverlay.AppCompat.ActionBar"
   app:popupTheme="@style/ThemeOverlay.AppCompat.Light"/>

```

*Material Design 规范建议应用栏具有 4 dp 的仰角*


#### 在 Activity 里绑定 ToolBar 作为 ActionBar

在 Activity 的 onCreate() 方法中，调用 Activity 的 setSupportActionBar() 方法，然后传递 Activity 的工具栏。该方法会将工具栏设置为 Activity 的应用栏。

```java

@Override
protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_my);
      Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
      //绑定ToolBar为ActionBar
      setSupportActionBar(myToolbar);
    }

```

### ToolBar xml属性详解：

ToolBar的常有属性有以下这些：

#### ToolBar标题

即在ActionBar中表明本页面的主旨的文字

```xml
<android.support.v7.widget.Toolbar
  ...
  app:title="@string/app_name"
  app:titleTextColor="@color/colorPrimary"
  app:titleTextAppearance="@style/CollapsedActionBar"
  />
```

|属性|作用|参数|
|--|--|--|
|app:title="字符串"|标题文字|字符串内容|
|app:titleTextColor="颜色"|标题文字颜色|颜色RBG值/颜色资源|
|app:titleTextAppearance="样式"|标题文字的外观样式|在Style文件里面定义好的样式|

#### Toolbar 标题位置





<!-- Toolbar_title
Toolbar_titleTextAppearance
Toolbar_titleTextColor  -->

<!-- Toolbar的内容重心 -->
<!-- Toolbar_android_gravity
Toolbar_buttonGravity -->

<!-- ???待解决-->
<!-- Toolbar_collapseContentDescription
Toolbar_collapseIcon -->

<!-- 控制ToolBar保留空间的位置控制 -->
<!-- Toolbar_contentInsetEnd
Toolbar_contentInsetEndWithActions
Toolbar_contentInsetLeft
Toolbar_contentInsetRight
Toolbar_contentInsetStart
Toolbar_contentInsetStartWithNavigation -->

<!-- ToolBar的logo图标 -->
<!-- Toolbar_logo
Toolbar_logoDescription -->

<!-- 对所有按钮的约束 -->
<!-- Toolbar_maxButtonHeight -->

<!-- 导航栏按钮 -->
<!-- Toolbar_navigationContentDescription
Toolbar_navigationIcon -->

<!-- 菜单栏的弹出样式 -->
<!-- Specifies the theme to use when inflating popup menus. By default, uses the same theme as the Toolbar itself. -->
<!-- Toolbar_popupTheme -->

<!-- ToolBar副标题 -->
<!-- Toolbar_subtitle
Toolbar_subtitleTextAppearance
Toolbar_subtitleTextColor -->



<!-- ToolBar 标题位置的调整 -->
<!-- Toolbar_titleMargin
Toolbar_titleMarginBottom
Toolbar_titleMarginEnd
Toolbar_titleMarginStart
Toolbar_titleMarginTop
-->

## 4、CollapsingToolbarLayout

### 4.1、概述：

<!-- CollapsingToolbarLayout is a wrapper（包装材料） for Toolbar which implements a collapsing app bar. It is designed to be used as a direct child of a AppBarLayout. CollapsingToolbarLayout contains the following features: -->
CollapsingToolbarLayout 是一个用于包裹 ToolBar 的控件，它是被设计为 AppBarLayout 的直接子 View。CollapsingToolbarLayout 包括一下特点：

<!-- Collapsing（折叠） title
A title which is larger when the layout is fully visible but collapses and becomes smaller as the layout is scrolled off screen. You can set the title to display via（经由，通过） setTitle(CharSequence). The title appearance can be tweaked（扭，拽，拧，对...微调） via the collapsedTextAppearance and expandedTextAppearance attributes. -->
* 折叠标题：一个比这个布局折叠起来以后的标题要大的标题。你可以设置该标题的显示通过 setTitle(CharSequence) 方法。该标题的外观可以通过 collapsedTextAppearance 和 expandedTextAppearance 参数来进行微调
<!-- Content scrim
A full-bleed（印刷术的术语） scrim（薄纱，纱幕） which is show or hidden when the scroll position has hit a certain（确定的，确信的，某，某位，轻微） threshold（门槛，下限，开端，起征点）. You can change this via setContentScrim(Drawable). -->
* 内容幕布：一个当滑动位置达到确定的位置时会出现或隐藏的并且图片绘制超出其大小的部分会被砍掉的幕布。你可以通过 setContentScrim(Drawable) 来修改该幕布中的图片
<!-- Status bar scrim
A scrim which is show or hidden behind the status bar when the scroll position has hit a certain threshold. You can change this via setStatusBarScrim(Drawable). This only works on LOLLIPOP devices when we set to fit system windows. -->
* 状态栏幕布：一个当滑动到特定位置会出现或隐藏的在状态栏后面的幕布，你可以通过 setStatusBarScrim(Drawable) 来改变它。该特性仅支持Android5.0的系统。
<!-- Parallax scrolling children
Child views can opt（选择） to be scrolled within this layout in a parallax fashion. See COLLAPSE_MODE_PARALLAX and setParallaxMultiplier(float). -->
* 视差滚动子 View ：在[视差设计](https://www.unleashed-technologies.com/blog/2013/08/15/what-parallax-web-design-%E2%80%93-definitions-tips-considerations)（大概就是几个图层有差异地滚动）里面，子View可以有选择性地在 CollapsingToolbarLayout 里面滚动。更多可参考官方文档[COLLAPSE_MODE_PARALLAX](https://developer.android.com/reference/android/support/design/widget/CollapsingToolbarLayout.LayoutParams.html#COLLAPSE_MODE_PARALLAX)和[setParallaxMultiplier(float)](https://developer.android.com/reference/android/support/design/widget/CollapsingToolbarLayout.LayoutParams.html#setParallaxMultiplier(float))
<!-- Pinned（固定的、不能动弹的） position children
Child views can opt to be pinned in space globally. This is useful when implementing a collapsing as it allows the Toolbar to be fixed（固定的、使固定的） in place even though this layout is moving. See COLLAPSE_MODE_PIN. -->
* 固定位置的子 View ：子 View 可以有选择性地固定在整个空间的某个位置。当你想要滑动时ToolBar是固定的，这个属性将会非常有用。
<!-- Do not manually（手动地） add views to the Toolbar at run time. We will add a 'dummy（愚蠢的） view' to the Toolbar which allows us to work out the available space for the title. This can interfere（插手，弄坏，弄坏某物，妨碍，干扰，骚扰） with any views which you add. -->

千万不要在运行时动态地往 ToolBar 里面添加 View 。系统会添加一个空白 View 到


## 待解决：

NestedScrollView ,NestedScrollParent ,NestedScrollChild .
