# Android-RecyclerView

## 基本使用

### 在布局文件中声明 RecyclerView 标签

```xml
    <android.support.v7.widget.RecyclerView
        android:id="@+id/recyclerview"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
```

### 自定义 ViewHolder 继承 RecyclerView.ViewHolder

自定义的 ViewHolder 中主要需要重写构造函数然后进行初始化。

一般我们会把 View 和数据绑定的方法写到 ViewHolder 里面，然后在 Adapter 中调用绑定的相关方法并传入必要的数据完成对应的数据设置

```java
    public class MyViewHolder extends RecyclerView.ViewHolder {

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            //此处进行必要的初始化：获取子 View 对象（findViewById）、设置基本样式参数等
        }

        public void onBindData(/*必要的数据*/){
            //对 View 进行设置
        }

    }
```

### 自定义 Adapter 继承 RecyclerView.Adapter
自定义的 Adapter 中需要重写以下方法：

1. `public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int type)`<br>
    该方法根据传入的 type 进行分类初始化 View 并绑定至，如果所有 item 都是一种类型则不需要区别化处理
2. `public void onBindViewHolder(@NonNull RecyclerView.ViewHolder viewHolder, int i)`<br>
    该方法根据传入的 item 位置 --- position，对绑定在该位置 ViewHolder 的 view 进行相应的属性设置
3. `public int getItemCount()`<br>
    该方法返回一个决定 RecyclerView item 数目的 int 值
4. `public int getItemViewType(int position)`<br>
    如果有多种类型的 View 可以使用该方法返回对应的类型 int 值用于区分，只有一种类型 item 时可不复写该方法

**示例代码：**

```java
public class MyAdapter extends RecyclerView.Adapter {

    //常用 List 类型来装载所有 item 的数据
    List<String> mlist;

    //通过构造函数传入数据
    public MyAdapter(List<String> mlist) {
        this.mlist = mlist;
    }

    @NonNull
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int type) {
        /* 单一类型 item */
        //此处为 item 对应的 View 初始化并绑定至 ViewHolder 的操作
        TextView textView = new TextView(viewGroup.getContext());
        textView.setLayoutParams(new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        textView.setTextSize(40);
        return new MyViewHolder(textView);

        /* 多种类型 item */
        /*如果要根据不同的类型进行区分初始化可以使用 switch case 进行区别处理*/
        switch(type){
            case 1:
                ...
                return new OneViewHolder(oneView);
            case 2:
                ...
                return new TwoViewHolder(twoView);
            default:
                ...
                return new DefaultViewHolder(defaultView);
        }

    }

    @Override
    public void onBindViewHolder(@NonNull RecyclerView.ViewHolder viewHolder, int position) {
        //为当前位置的 View 进行对应的属性设置
        /* 单一类型 item */
        ((TextView) viewHolder.itemView).setText(mlist.get(position));

        /* 多种类型 item */
        if(viewholder istanceof OneViewHolder){
            ...
        }else if(viewholder istanceof TwoViewHolder){
            ...
        }else{
            ...
        }
    }

    @Override
    public int getItemCount() {
        //一共有多少条 item 数据
        return mlist.size();
    }

    @Override
    public int getItemViewType(int position) {
        //根据 item 的位置进行判断返回对应的 类型值
        switch(mlist.get(position)){
            case "TYPE1":
                return 1;
            case "TYPE2";
                return 2;
            default:
                return -1;
        }
    }
}
```

### 最后在 Activity 中声明并设置 数据 List、RecyclerView、Adapter 和对应的 LayoutManager 即可

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        for(int i = 0;i<50;i++){
            mlist.add("ITEM "+i);
        }

        recyclerView = findViewById(R.id.recyclerview);
        myAdapter = new MyAdapter(mlist);
        linearLayoutManager = new LinearLayoutManager(this);
        recyclerView.setAdapter(myAdapter);
        recyclerView.setLayoutManager(linearLayoutManager);

    }
```

## 运行机理

### RecyclerView
### Adapter
### LayoutManager