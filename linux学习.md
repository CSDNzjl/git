# linux学习

## CMake

[Linux下CMake简明教程_linux cmake-CSDN博客](https://blog.csdn.net/whahu1989/article/details/82078563)

- 开源、跨平台的构建工具，可以通过编写简单的配置文件（独立于运行平台和编译器）生成本地的Makefile
- 优点：不用亲自编写Makefile，配置文件移植性好

### elf文件

- 在Linux系统中，当你编译一个C或C++程序时，编译器（如gcc）会生成一个ELF格式的可执行文件。这个文件包含了程序的二进制代码和所有必要的元数据，使得操作系统的加载器可以正确地加载和执行程序。（make之后生成的）

### CMake .   CMake ..区别

- CMake .当前目录运行CMake，在**当前目录**搜索CMakeLists.txt文件
- CMake ..当前目录运行CMake，在**当前目录的父目录**搜索CMakeLists.txt文件
  - CMake ../..   在父目录的父目录搜索

### ./加与不加

- ./表示当前目录，不加./系统会在环境变量定义的目录中搜索
- 向环境变量PATH增加路径
  - `nano ~/.bashrc`打开配置文件
  - `export PATH=$PATH:/home/luffy/桌面/User/build`（build的完整路径）添加路径到PATH变量，按 `Ctrl+O` 保存更改，然后按 `Ctrl+X` 退出编辑器
  - `source ~/.bashrc`让更改立即生效
  - `echo $PATH`查看环境变量是否添加（重启后依然生效）

### 头文件定义

```c
/*
** testFunc.h
*/
#ifndef _TEST_FUNC_H_
#define _TEST_FUNC_H_
void func(int data);
#endif
```

### 指令集

#### 总结

1. cmake_minimum_required	指定版本要求
2. project    工程名
3. add_executable    生成可执行程序
4. aux_source_directory    所有源文件存储在变量中
5. set    定义变量与对应的内容
6. include_directories    包含头文件
7. add_subdirectory    添加源代码子目录
8. add_library    生成库文件
9. set_target_properties    修改库文件名称
10. find_library    查找库并存储在变量中
11. target_link_libraries    连接目标文件和库文件

#### 具体内容

- `cmake_minimum_required (VERSION 2.8)`   指定cmake最低版本要求
- `project (demo)`  工程名
- `add_executable(main main.cpp)`   最终要生成的elf名称与源文件
- ![](https://i-blog.csdnimg.cn/blog_migrate/8b3e07ea9e191e0da1d1532b713fa06a.jpeg)**同一目录下多个源文件**
  - 修改`add_executable(main main.cpp)` 为`add_executable(main main.c testFunc.c)`
  - 源文件较多时，`aux_source_directory(dir var)`将指定目录下的所有==源文件==存储在一个变量中`aux_source_directory(. SRC_LIST)``add_executable(main ${SRC_LIST})`
  - 指定部分源文件`set( SRC_LIST  ./main.c  ./testFunc1.c  ./testFunc.c)``add_executable(main ${SRC_LIST})`
- ![](https://i-blog.csdnimg.cn/blog_migrate/bdeba3087852fdda33d8126e57ebe094.jpeg)**不同目录下多个源文件**
  - `include_directories (test_func test_func1)`指定==头文件.h==的搜索路径
- ![](https://i-blog.csdnimg.cn/blog_migrate/a12a02b995926b888586c88713021c75.jpeg)**正规一点的组织结构**
  - src源文件，include头文件，build生成的对象文件，bin输出的elf文件
  - `add_subdirectory (src)`添加源代码子目录，同时src目录下也需要有一个CMakeLists.txt
  - `set (EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)`
    - EXECUTABLE_OUTPUT_PATH ：目标二进制可执行文件的存放位置
    - PROJECT_SOURCE_DIR：工程的根目录

[静态库与动态库的区别与优缺点_静态库和动态库的优缺点-CSDN博客](https://blog.csdn.net/weixin_51483516/article/details/120837316)

- 静态库的扩展名一般为“.a”或“.lib”；动态库的扩展名一般为“.so”或“.dll”。
- 静态库和动态库最本质的区别就是：**该库是否被编译进目标（程序）内部。**
- ![](https://i-blog.csdnimg.cn/blog_migrate/51e6014d970a9bfd07c518212741d226.png)
  - `add_library (testFunc_shared SHARED ${SRC_LIST})`  生成动态库
  - `add_library (testFunc_static STATIC ${SRC_LIST})` 生成静态库
  - `set_target_properties (testFunc_shared PROPERTIES OUTPUT_NAME "testFunc")`设置最终生成的库的名称（只使用add_library名字不能一样，最后生成的名字是`libtestFunc`）
  - `set (LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)`库文件的默认输出路径

- ![](https://i-blog.csdnimg.cn/blog_migrate/e374b35d8366b190c1d63f680c82f783.png)对库进行连接
  - `find_library(TESTFUNC_LIB testFunc HINTS ${PROJECT_SOURCE_DIR}/testFunc/lib)`查找指定库并保存在变量中，第一个参数是变量名称，第二个参数是库名称，第三个参数是HINTS，第4个参数是路径,默认查找动态库，指定命令为`find_library(TESTFUNC_LIB libtestFunc.so ...`或者`find_library(TESTFUNC_LIB libtestFunc.a ...`
  - `target_link_libraries (main ${TESTFUNC_LIB})`把目标文件和库文件链接
  - 查看可执行程序用了哪些库：readelf -d ./xx

## Make

- 相当于将终端的命令集中在Makefile文件中，根据不同的指令运行不同的命令

### 示例：

```makefile
# 默认目标是 "all"，它依赖于 "test" 目标。
all: test
# "test" 目标依赖于两个对象文件 "test.o" 和 "anotherTest.o"。
# 下面的命令使用 gcc 编译器将这两个对象文件链接成可执行文件 "test"。
test: test.o anotherTest.o
    gcc -Wall test.o anotherTest.o -o test
# "test.o" 目标依赖于源文件 "test.c"。
# 下面的命令使用 gcc 编译器编译 "test.c" 源文件生成对象文件 "test.o"。
test.o: test.c
    gcc -c -Wall test.c 
# "anotherTest.o" 目标依赖于源文件 "anotherTest.c"。
# 下面的命令使用 gcc 编译器编译 "anotherTest.c" 源文件生成对象文件 "anotherTest.o"。
anotherTest.o: anotherTest.c
    gcc -c -Wall anotherTest.c 
# "clean" 是一个伪目标，用于清理所有编译生成的==对象文件和可执行文件==。
clean: 
    rm -rf *.o test
```

-  make 命令不会编译那些自从上次编译之后就没有更改的文件，可以使用 `make -B` 强制编译所有的目标文件以及最终的执行文件。
- -C 改变目录，`make -C ../make-dir/ `

- -d打印调试信息，`make -d | more`
- -f将其他名称的Makefile文件视为Makefile，`make -f my_makefile`