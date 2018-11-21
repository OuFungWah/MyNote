# Cpp 学习之路

## Cpp的基本样子

```Cpp
#include <iostream>         //C++标准库

int main(int argc, const char *argv[])      //main函数
{
    using namespace std;

    cout << "Are you Ok?\n";
    cout << endl; // endl == 换行
    cout << "Are you Ok?\n"
         << endl;
    cin.get();

    return 0;
}
```

## Main函数

C++ 标准写法是 ```int main()```

main 函数由编译器的启动代码调用，参数也由编译器传入（一般可在IDE中设置）

参数列表可有可无： ```int main(void)``` 或 ```int main(int arg)``` 都可以

```void main()``` 逻辑上是可以的，但是非标准写法，某些系统无法运行，不推荐

