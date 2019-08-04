# Android Room 框架
## 概述：

Room 框架是由 Google 提供的、基于 SQLite 定制的一套 Android 本地数据库框架。通过

对比起隐藏 SQLite 的细节，Room 更想去尝试通过给出便利的 API 去让你使用它，并在编译期去验证你的操作。这使得我们可以在使用到全量的 SQLite 的功能的同时又可以获得由 Java SQL 提供的类型安全数据。

## 三个基本要素

- **数据库（Database）**

**Database** --- 代表着数据库中具体的表单，这些类必须继承 RoomDatabase 类且是一个抽象类，抽象类中需要有获取对应 **Dao** 的抽象方法，运行时可以通过 **Room.databaseBuilder** 或 **Room.inMemoryDatabaseBuilder** 去获得其对象。

**Database** 的声明主要配合着 `@Database` 注解使用。

同一个 `@Database` 注解的类中可以同时关联多个 Entity 和多个 Dao，但是各个 **Entity** 和 **Dao** 必须是独立不重复的。

- **实体（Entity）**

**Entity** 对应了数据表中一行数据该有的数据。数据库中的 **entities** 数组持有了对应 **Entity** **类型的引用。Entity** 中的每一个字段除非被 `@Ignore` 注解注释掉了，否则都会保存在数据库。

Entity 的声明主要配合着 `@Entity、@PrimaryKey、@ColumnInfo、@Ignore、@Embedded、@Relation` 等注解进行声明。

每一个 **Entity** 必须包含一个无参构造函数或一个匹配所有字段的构造函数（名字与类型都匹配）。如果构造函数不能对应上所有字段的赋值，那么没对应上的字段必须是 **public** 的或有 **public** 修饰的 **setter**。**Room**会一直使用同一个符合条件的构造函数，如果想 **Room** 不使用某个构造函数，那需要对该构造函数使用 `@Ignore` 注解。

`@Ignore` 同样可以用于注释不需要存储的字段。

- **数据操作类（Dao）**

**Dao** 主要用于与数据库之间的交互。**Dao**类理应是一个抽象类或者是接口，具体的实现将会由 **Room** 在编译期间生成并由 **Database** 返回其对应的引用。

**Dao** 定义了操作数据库的各种方法。**Database** 注解的类中必须含有一个无参数并返回有 `@Dao` 注解的对象的抽象方法。编译期间，Room 会自动生成对应的具体实现。
使用 **Dao** 而不是 `query builder` 或者直接查询可以让你保持不同组件之间的分离，更容易在测试阶段 mock 数据。

**Dao** 的声明主要配合着 `@Dao、@Query、@Delete、@Insert` 等注解进行声明。

## 基本使用 

### 1、添加依赖

添加对应的 Gradle 依赖

```    
    def room_version = "2.2.0-alpha01" // 版本号
    implementation 'androidx.core:core-ktx:1.0.2'
    implementation "androidx.room:room-runtime:$room_version"
```

官方有句特别提醒：

> Note: For Kotlin-based apps, make sure you use kapt instead of annotationProcessor. You should also add the kotlin-kapt plugin. 

大致意思是，如果是一个 Kotlin 的项目，记得要使用 kotlin 的 apt 工具。

引入 Kapt：
```
    apply plugin: 'kotlin-kapt'
    dependencies {
        kapt "android.arch.persistence.room:compiler:1.1.1"
        ···
    }
```

*这里我踩了一个小坑，就是如果没有引入 kapt Room 将无法自动生成代码，编译不通过*

### 2、相关类声明

上面也提到了，Room 有自己的三大要素，**Entity**、**Dao**、**Database**，下面将依次列出对应的要素如何声明

**Entity**：
```
    @Entity
    class User {
        // 主键注解是每个 Entity 必有且仅有一个的注解
        @PrimaryKey(autoGenerate = true)
        var id: Long = 0
        var name: String = ""
        var age: Int = 0
    }
```
**Dao**：

```
    @Dao
    interface UserDao{
        // 查询所有的 User 数据
        @Query("SELECT * FROM user")
        fun findAll(): List<User>
        // 查询符合条件的数据
        @Query("SELECT * FROM user WHERE id IN (:ids)")
        fun findInIds(vararg ids: Int): List<User>
        // 插入数据
        @Insert
        fun insertAll(vararg users: User)
        // 删除数据
        @Delete
        fun delete(user: User)
    }
```

**Database**：
```
    // 注解中主要有两个重要参数，version 数据库版本，entities 数据实体类型数组
    @Database(version = 1, entities = [User::class])
    // 继承自 RoomDatabase
    abstract class UserDatabase: RoomDatabase() {
        // 获取某个 Dao 的抽象方法
        abstract fun userDao(): UserDao
    }
```

### 3、数据使用：（必须在子线程中）

获取引用

```
    // 获取数据库引用
    var db = Room.databaseBuilder(applicationContext, UserDatabase::class.java, "user").build()
    // 获取对应的 Dao 引用
    var userDao = db.userDao()
    操作数据
    // 查询
    var userList = userDao.finAll()
    // 插入
    userDao.insertAll(User())
```
## 注意问题：
### 关于 Entity 使用构造函数问题：
实践出真知，试一下就知道了
```
    @Ignore
    constructor(){
        Log.d("ofh","使用了 () 构造函数")
    }
    @Ignore
    constructor(name: String): this(){
        Log.d("ofh","使用了 (id: Long) 构造函数")
        this.name = name
    }
    constructor(name: String, age: Int): this(name){
        Log.d("ofh","使用了(name: String, age: Int)构造函数")
        this.age = age
    }
```

对应的日志输出

```
    D/ofh: 使用了(name: String, age: Int)构造函数
    D/ofh: 使用了(name: String, age: Int)构造函数
    D/ofh: 使用了(name: String, age: Int)构造函数
```

换个位置：

```
    @Ignore
    constructor(){
        Log.d("ofh","使用了 () 构造函数")
    }
    constructor(name: String): this(){
        Log.d("ofh","使用了 (id: Long) 构造函数")
        this.name = name
    }
    @Ignore
    constructor(name: String, age: Int): this(name){
        Log.d("ofh","使用了(name: String, age: Int)构造函数")
        this.age = age
    }
```

对应的日志输出

```
    D/ofh: 使用了(name: String)构造函数
    D/ofh: 使用了(name: String)构造函数
    D/ofh: 使用了(name: String)构造函数
```

再换个位置：

```
    constructor(){
        Log.d("ofh","使用了 () 构造函数")
    }
    constructor(name: String): this(){
        Log.d("ofh","使用了 (id: Long) 构造函数")
        this.name = name
    }
    @Ignore
    constructor(name: String, age: Int): this(name){
        Log.d("ofh","使用了(name: String, age: Int)构造函数")
        this.age = age
    }
```

对应的日志输出

```
    D/ofh: 使用了()构造函数
    D/ofh: 使用了()构造函数
    D/ofh: 使用了()构造函数
```

再再换个位置：

```
    @Ignore
    constructor(){
        Log.d("ofh","使用了 () 构造函数")
    }
    constructor(name: String): this(){
        Log.d("ofh","使用了 (id: Long) 构造函数")
        this.name = name
    }
    constructor(name: String, age: Int): this(name){
        Log.d("ofh","使用了(name: String, age: Int)构造函数")
        this.age = age
    }
```

编译错误。

**总的来说：**

有效的构造函数 **Room** 会一直使用，**有无参构造函数优先使用无参构造函数，没有无参构造函数则使用其他有效构造函数**，当类中有多个多参构造函数且多于两个有效没有用 `@Ignore` 注解时，编译会不通过，因为 **Room** 不知该用哪一个构造函数。

### 关于线程的问题

数据库的访问是不允许在主线程当中的，因为在主线程中访问数据库有几率会阻塞线程。
如果想要在 UI 线程可以直接使用数据库可以使用 `allowMainThreadQueries()` 方法。

```kotlin
    Room.databaseBuilder(applicationContext, UserDatabase::class.java, "user").allowMainThreadQueries().build()
```

### 关于升级数据库的问题

升级数据库涉及多处代码的修改

1. 修改实体类

```
    @Entity
    class User {
        @PrimaryKey(autoGenerate = true)
        var id: Long = 0
        var name: String = ""
        var age: Int = 0
        @ColumnInfo(name = "birthday")
        var birthday: Long = 0        //<--- 新增字段

    }
```
2. 数据库相关的内容修改以后必须要升级数据库注解上的版本号。
```@Database(version = 2, entities = [User::class])```
3. 定一个从 版本号为 1 升到 2 的 Migration，以告诉数据库需要如何升级。
```
    val migration1_2 = Migration(1, 2){
        override fun migrate(database: SupportSQLiteDatabase) {
            database.execSQL("ALTER TABLE 'user' ADD COLUMN 'birthday' INTEGER DEFAULT 0 NOT NULL")
        }
    }
```
4. 创建数据库时添加一下 Migration
```
Room.databaseBuilder(activity.applicationContext, UserDatabase::class.java, "user")
    .addMigrations(migration1_2)
    .build()
```
## 其他：
参考文档：Android [官方文档](https://developer.android.com/reference/androidx/room/package-summary)

自写小 [Demo](https://github.com/OuFungWah/AndroidRoomArchitecture)