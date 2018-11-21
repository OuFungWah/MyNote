# Android-Bitmap

## Bitmap 位图

Bitmap 位图、也被称为栅格图。在手机屏幕上我们看到的所有图像都是由一个一个像素点组成的，而一个像素点由RGB（Red，Green，Blue）三个颜色通道组成（小学时候学的电视三原色，可以组合成其他颜色），而位图就是存储了一张图片的每一个像素点的相关信息的一个数据结构

## Android 中 Bitmap 相关的几个类

* Bitmap：位图类
* Bitmap.Config：Bitmap 的位深度（一个像素点的存储颜色值的精确度）
* BitmapFactory：创建 Bitmap 的工具类
* BitmapFactory.Options：创建 Bitmap 时属性项

## Bitmap 的获取

作为一个图像我们第一步首先肯定要考虑如何获取到，才能进行下一步的缩放、质量压缩、格式转换等等的操作。

### 从 View 中获取：
### 从本地文件中获取
### 从网络中获取
### 从相机中获取
### 从相册中获取 