# Android Fragment

## 生命周期

```java

onAttach();
onCreate();
onCreateView();
onStart();
onResume();
onPause();
onStop();
onDestoryView();
onDestory();
onDetach();

```

### 初次启动

1. A-onCreate()
2. A-onStart()
3. F-onAttach()
4. F-onCreate()
5. F-onCreateView()
6. F-onStart()
7. A-onResume()
8. F-onResume()

总的来说，先 A-onStart() 再跑 F-onAttach()、F-onCreate()、F-onCreateView()、F-onStart() 最后先 A-onResume()、F-onResume()

```
08-21 16:16:26.882 14680-14680/? D/MainActivity: onCreate: Activity executed
08-21 16:16:27.089 14680-14680/? D/MainActivity: onStart: Activity executed
08-21 16:16:27.094 14680-14680/? D/MyFragment: onAttach: MyFragment executed
08-21 16:16:27.094 14680-14680/? D/MyFragment: onCreate: MyFragment executed
08-21 16:16:27.095 14680-14680/? D/MyFragment: onCreateView: MyFragment executed
08-21 16:16:27.096 14680-14680/? D/MyFragment: onStart: MyFragment executed
08-21 16:16:27.101 14680-14680/? D/MainActivity: onResume: Activity executed
08-21 16:16:27.101 14680-14680/? D/MyFragment: onResume: MyFragment executed
```

### 按下 Home 键

A-onPause()、F-onPause()、A-onStop()、F-onStop()

```
08-21 16:27:47.887 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MainActivity: onPause: Activity executed
08-21 16:27:47.888 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onPause: MyFragment executed
08-21 16:27:47.905 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MainActivity: onStop: Activity executed
08-21 16:27:47.905 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onStop: MyFragment executed
```

### 从后台恢复（未销毁）

1. A-onRestart();
2. A-onStart()
3. F-onStart()
4. A-onResume()
5. F-onResume()

```
08-21 16:29:37.718 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MainActivity: onRestart: Activity executed
08-21 16:29:37.720 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MainActivity: onStart: Activity executed
08-21 16:29:37.720 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onStart: MyFragment executed
08-21 16:29:37.721 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MainActivity: onResume: Activity executed
08-21 16:29:37.722 14680-14680/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onResume: MyFragment executed
```

### 销毁
```
08-21 16:36:09.941 14659-14659/com.example.crazywah.fragmentlivecycledemo D/MainActivity: onDestroy: Activity executed
08-21 16:36:09.941 14659-14659/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onDestroyView: MyFragment executed
08-21 16:36:09.946 14659-14659/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onDestroy: MyFragment executed
08-21 16:36:09.946 14659-14659/com.example.crazywah.fragmentlivecycledemo D/MyFragment: onDetach: MyFragment executed
```