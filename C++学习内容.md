# C++学习内容

[八个 C++ 开源项目，帮助初学者进阶成长_c++项目-CSDN博客](https://blog.csdn.net/lu_embedded/article/details/121641662)

[huihut/interview: 📚 C/C++ 技术面试基础知识总结，包括语言、程序库、数据结构、算法、系统、网络、链接装载库等知识及面试经验、招聘、内推等信息。This repository is a summary of the basic knowledge of recruiting job seekers and beginners in the direction of C/C++ technology, including language, program library, data structure, algorithm, system, network, link loading library, interview experience, recruitment, recommendation, etc. (github.com)](https://github.com/huihut/interview?tab=readme-ov-file#contributor)

[C++ 面试指北介绍 | 编程指北 (csguide.cn)](https://csguide.cn/cpp/intro.html)

## 7.22 

- hex ： 十六进制	oct ： 八进制

  - cin >> hex >> n  读取十六进制输出十进制

  - ```c++
    std::string hexString = "1A3F"; // 十六进制字符串
    int decimalValue;
    // 使用istringstream读取十六进制字符串并转换为十进制数
    std::istringstream(hexString) >> std::hex >> decimalValue;
    ```

- [C++最全输入方式总结(cin、get、getchar、getline)_c++输入-CSDN博客](https://blog.csdn.net/qq_41687938/article/details/117365211)
  - cin>>  单个字符/数字/字符串，空格/回车/tab结束
  - cin.get()  只能字符，cin.get(字符变量名)；cin.get(数组名，接收字符数目)；cin.get() 舍弃输入流中的一个字符
  - cin.getline()  cin.getline(变量名， 输入大小，自定义结束标志)
  - getline(cin,string s)  清除cin留下的结束符
  - toupper(char)    tolower(char)  返回类型是**int**，需要static_cast<char>(num)转换

> 1.**string末尾无'\0'，字符数组有**，声明字符数组时要比预想的多设一位
>
> 2.字符数组sizeof()（实际大小）比strlen()（只计算字符串的长度）大1
>
> **动态分配的数组**：对于动态分配的字符数组（如`char*`），`sizeof()`返回的是指针的大小，而不是数组的大小。因此，在这种情况下，应该使用`strlen()`来获取字符串的长度。
>
> 3.getline()中的结束符，结束后，结束符不放入缓存区;
>
> ​        cin的结束符，结束后，结束符还在缓存区；

- [C++ OJ在线编程常见输入输出技巧与示例_c++oj-CSDN博客](https://blog.csdn.net/qq_41687938/article/details/116535989?spm=1001.2014.3001.5501)

- [C++中的String的常用函数用法总结_string函数-CSDN博客](https://blog.csdn.net/qq_37941471/article/details/82107077)
  -  string str2("123456789");  //生成"123456789"的复制品
  - **s.size()**  s.length()包含的字符个数  s.capacity()容量
  - A.compare(B)  返回0，1，-1（相等，大于，小于）
  - s1.push_back('a');尾插  s1.insert(s1.begin(),'1');定位前插入
  - s1.append("def");   s2 += s3;
  - **s1.erase(1,6);**   
  - **s.find("chicken")   s.rfind("chicken")**  找不到则返回**std::string::npos**
  - **sort(s.begin(),s.end());**
  -  std::string sub2 = str.substr(0, 5);提取子串

- [C++——string之迭代器_string的迭代器-CSDN博客](https://blog.csdn.net/luzhaoxi/article/details/109600146)

> 正向迭代器（**iterator**）、反向迭代器（**reverse_iterator**）
>
> begin()：指向容器第一个元素的位置（可读可写） 	rbegin()：指向容器最后一个元素的位置（可读可写）
>
> end()：指向容器最后一个元素的下一个位置（可读可写） 	rend()：指向容器第一个元素的前一个位置（可读可写）

- [C++ 数组（vector）常用操作总结_vector操作-CSDN博客](https://blog.csdn.net/Flag_ing/article/details/123380655)
  - vector<T> v3(n, val)  vector<T> v2(v1)
  - v.empty()  v.size()  v.push_back(val)  v.pop_back(val)   
  - auto it = a.begin(); 迭代器  ++it；
  - **reverse(a.begin(), a.end());**  // 原位逆序
  - vec.erase(vec.begin()+5)
  - auto max_it = std::**max_element**(vec.begin(), vec.end()); *max_it就是最大值
- swap（a，b）交换两个变量的值
- [C++ sort()排序详解-CSDN博客](https://blog.csdn.net/qq_41575507/article/details/105936466)
  - **sort(begin, end, cmp)** 
  - 从大到小排序 cmp参数写为`greater<int>()`
  - 自定义排序准则   
- [【C++】static_cast基本用法（详细讲解）_c++ static cast-CSDN博客](https://blog.csdn.net/weixin_44244190/article/details/132239858)   类型转换
  - double d = 5.5; int i = static_cast<int>(d);  


```c++
#include<iostream>
#include<algorithm>
using namespace std;
bool cmp(int x,int y){
	return x % 10 > y % 10;
}
int main(){
	int num[10] = {65,59,96,13,21,80,72,33,44,99};
	sort(num,num+10,cmp);
	for(int i=0;i<10;i++){
		cout<<num[i]<<" ";
	}//输出结果：59 99 96 65 44 13 33 72 21 80
	return 0;
} 
```

## 7.23

- [STL容器——unordered_set的用法_unorderedset用法-CSDN博客](https://blog.csdn.net/qq_44629819/article/details/131294191)

  - `unordered_set`容器，可直译为无序 set 容器，底层实现为哈希表，**不提供下标访问**，可以使用迭代器或直接遍历

  - ```cpp
    #include <unordered_set>
    std::unordered_set<int> set1;
    set1.insert(10);
    set1.find(20)；
    set1.count(30)//计数
    ```

- [一文看懂哈希表并学会使用C++ STL 中的哈希表_哈希表有哪些函数-CSDN博客](https://blog.csdn.net/Peealy/article/details/116895964)

  ```c++
  #include <unordered_map>
  int main() {
      // 创建一个 unordered_map，键为 string，值为 int
      std::unordered_map<std::string, int> map;
      // 插入元素
      map["apple"] = 10;
      map["banana"] = 20;
      map.insert({"orange", 30});
      // 查找元素
      if (map.find("apple") != map.end()) {
          std::cout << "apple found, count: " << map["apple"] << std::endl;
      }
      // 删除元素
      map.erase("banana");
      // 遍历元素
      for (const auto& pair : map) {
          std::cout << pair.first << ": " << pair.second << std::endl;
      }
      return 0;
  }
  
  ```

- [c++类与对象（初学超详细讲解）_c++ 类 对象-CSDN博客](https://blog.csdn.net/qq_51577238/article/details/115256297)

  - 在外部定义成员函数时使用域作用符::

  - 静态数据成员和静态函数成员都**不属于类**

  - 当类中有动态内存成员时，一定要自己编写析构函数，**确保动态内存的释放**

  - **深拷贝与浅拷贝**

  - > 分析浅拷贝报错的原因：两个指针指向同一个内存。由于析构对象时会将两个指针指向的内存都删除，导致一个内存被删除两次
    > 解决方法：将两个指针指向的变为不同的两个内存，但是两个内存中存储的数据相同，即”开辟不一样的地址存储一样的数据“

- [C++：友元（看这一篇就够了）_c++ 友元-CSDN博客](https://blog.csdn.net/weixin_46098577/article/details/116596183)

  - 最关键：在Building类中声明**友元函数**

  - ```c++
    // 房屋类
    class Building
    {
    	// 告诉编译器 laoWang全局函数是 Building类  的好朋友，可以访问Building对象的私有成员
    	friend void laoWang1(Building *building);
    public:
    	Building()
    	{
    		m_SittingRo om = "客厅";
    		m_BedRoom = "卧室";
    	}
    	string m_SittingRoom;	// 客厅
    private:
    	string m_BedRoom;		// 卧室
    };
    void laoWang1(Building *building)
    {
    	cout << "隔壁老王 全局函数 正在访问：（地址传递） " << building->m_SittingRoom << endl;
    
    	cout << "隔壁老王 全局函数 正在访问：（地址传递） " << building->m_BedRoom << endl;
    }
    void test()
    {
    	Building building;
    	laoWang1(&building);
    }
    int main()
    {
    	test();
    }
    
    ```

- [C++运算符重载（类内、外重载）_类外重载运算符++-CSDN博客](https://blog.csdn.net/u014583317/article/details/109217780)

  - **类的有参构造**

  - ```c++
    Point (int x, int y): x(x),y(y){};
    Point(int x, int y) {
            this->x = x;
            this->y = y;
        }
    Point(int xCoord, int yCoord) {
            x = xCoord;
            y = yCoord;
        }
    ```

  - ```c++
     Point operator+(const Point &b){ //类内重载，运算符重载函数作为类的成员函数
            Point ret;
            ret.x = this->x + b.x;
            ret.y = this->y + b.y;
            return ret;
        }
    Point operator+(const Point &a,const Point &b){//类外重载,运算符重载函数作为类的友元函数
        Point ret;
        ret.x = a.x + b.x;
        ret.y = a.y + b.y;
        return ret;
    }
    ```


## 7.24

- [c++：继承（超详解）_c++继承-CSDN博客](https://blog.csdn.net/qq_62718027/article/details/125922249)

- [【C++】C++中的 `this` 指针：深度探索和应用_c++ this-CSDN博客](https://blog.csdn.net/crr411422/article/details/131063469)

- [深入浅出 C++ Lambda表达式：语法、特点和应用_c++ lamda函数作为函数参数-CSDN博客](https://blog.csdn.net/m0_60134435/article/details/136151698)

  - lambda定义并创建**匿名的函数对象**，不需要函数名 返回值用auto接受

  - `[capture list] (parameter list) -> return type { function body }`

  - ```c++
    auto f = [x] (int y) -> int { return x + y; }; // 值捕获 x
    //改变捕获变量的值不影响
    auto f = [&x] (int y) -> int { return x + y; }; // 引用捕获 x
    //改变捕获变量的值会有影响
    
    // 使用 Lambda表达式，根据 Item 中的成员 a 升序排序
        sort(vec.begin(), vec.end(), [] (const Item& v1, const Item& v2) { return v1.a < v2.a; });
        // 使用 Lambda表达式，打印 vec 中的 Item 成员
        for_each(vec.begin(), vec.end(), [] (const Item& item) { cout << item.a << " " << item.b << endl; });
    
    ```

- [C++队列queue用法详解_c++ queue用法-CSDN博客](https://blog.csdn.net/KEPROM/article/details/109744379)

  - ```C++
    queue<int>q1;
    push() 在队尾插入一个元素
    pop() 删除队列第一个元素
    size() 返回队列中元素个数
    empty() 如果队列空则返回true
    front() 返回队列中的第一个元素
    back() 返回队列中最后一个元素
    ```

- [C++：stack 定义，用法，作用，注意点_std::stack-CSDN博客](https://blog.csdn.net/m0_74331272/article/details/133419524)

  - ```c++
    std::stack<DataType> myStack;
    push(val)：将值 val 推入堆栈的顶部。
    pop()：从堆栈的顶部弹出一个元素，但不返回它。
    top()：返回堆栈顶部元素的引用，但不将其从堆栈中移除。//对应queue的front，back
    empty()：检查堆栈是否为空，返回布尔值。
    size()：返回堆栈中元素的数量。
    ```

- **[二叉树的基本操作(C++实现)_二叉树c++实现-CSDN博客]**(https://blog.csdn.net/qq_52109814/article/details/119539568)

  - ```c++
    typedef struct Node
    {
        char data;                    /*数据域*/
        struct Node *lchild, *rchild; /*左子树和右子树*/
    } * BiTree, BiNode;//重命名指针和结构体名称
    
    void CreateBiTree(BiTree &T)
    {
        char ch;
        cin >> ch;
        if (ch == '#')
            T = NULL;
        else
        {
            T = new BiNode; /*创建一个新节点*/
            T->data = ch;
            CreateBiTree(T->lchild);
            CreateBiTree(T->rchild);
        }
        /*递归创建*/
    }
    
    /*求树的深度*/
    int Depth(BiTree T)
    {
        if (T == NULL)
            return 0;
        else
        {
            int i = Depth(T->lchild);
            int j = Depth(T->rchild);
            return i > j ? i + 1 : j + 1;
        }
    }
    
    // 层序遍历（广度优先遍历）  队列实现
    void levelOrderTraversal(TreeNode* root) {
        if (root == nullptr) return;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            std::cout << node->val << " ";
            if (node->left != nullptr) {
                q.push(node->left);
            }
            if (node->right != nullptr) {
                q.push(node->right);
            }
        }
    }
    
    // 前序遍历
    void preorderTraversal(TreeNode* root) {
        if (root == nullptr) return;
        // 访问根节点
        std::cout << root->val << " ";
        // 递归遍历左子树
        preorderTraversal(root->left);
        // 递归遍历右子树
        preorderTraversal(root->right);
    }
    
    // 二叉查找树的查找操作
    bool search(node* root, const int& val) {
    	if (root == nullptr)   return false;
    	if (root->data == val) return true;
    	else if (root->data > val) {
    		return search(root->lchild, val);
    	} else {
    		return search(root->rchild, val);
    	}
    }
    ```

- [二叉树各种类型汇总_二叉树分类-CSDN博客](https://blog.csdn.net/u012060033/article/details/118250049)

  - 二叉树：每个节点至多有两个子树，左右子树有顺序
  - 完全二叉树：除最后一层外，每一层上的结点数均达到最大值；在最后一层上只缺少右边的若干结点
  - 满二叉树：除最后一层无任何子节点外，每一层上的所有结点都有两个子结点的二叉树
  - 二叉搜索树：若它的左子树不空，则左子树上的所有结点的值均小于根节点的值；若它的右子树不空，则右子树上的所有结点的值均大于根节点的 值，左右子树分别为二叉排序树。
  - 平衡二叉树：左右两个子树的`高度差的绝对值不超过1`，并且左右两个子树都是平衡二叉树

- 十进制转化为二进制(整数)   除二取余，逆序排列；小数部分乘二取整，顺序排列

  - ```c++
    std::string decimalToBinary(int n) {
        std::string binary = "";
        while (n > 0) {
            binary = (n % 2 == 0 ? "0" : "1") + binary;
            n /= 2;
        }
        return binary;
    }
    ```
  
- 单调栈寻找下一个更大的元素

  - ```c++
    std::vector<int> nextGreaterElement(const std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> result(n, -1); //初始化为-1，表示没有找到下一个更大元素
        std::stack<int> s; // 单调栈，存储元素的索引
        for (int i = 0; i < n; ++i) {
            while (!s.empty() && nums[i] > nums[s.top()]) {
                result[s.top()] = nums[i];
                s.pop();
            }
            s.push(i);
        }
        return result;
    }
    ```


## 7.25

- 输入输出总结

  - 输入一行空格隔开的数据

    - ```c++
      #include <sstream>
      std::string line;
      // 读取一行数据
      std::getline(std::cin, line);
      // 使用字符串流处理读取的数据
      std::stringstream ss(line);
      std::string token;
      std::vector<std::string> tokens;
      // 将数据分割成多个部分
      while (ss >> token) {
          tokens.push_back(token);
          
      #include <algorithm>
      sort(tokens.begin(),tokens.end());
          
      #include <iostream>
      #include <vector>
      #include <algorithm>
      #include <sstream>
      ```

  - 清除输入缓冲区中的多余字符（cin后其他类型输入，cin本身会处理空字符不需要清理）

    - cin.ignore()     只能清除一个字符

      - ```cpp
        cin.ignore(100, '\n');  // 丢弃最多100个字符，或者直到遇到换行符
        ```

    - getline(cin,string s) 

    - cin.get()    只能清除一个字符

  - 输入一行逗号隔开的字母

    - ```cpp
      std::string line;
      // 读取一行数据
      std::getline(std::cin, line);
      // 使用字符串流处理读取的数据
      std::stringstream ss(line);
      std::string token;
      std::vector<std::string> tokens;
      // 将数据分割成多个部分
      while (std::getline(ss, token, ',')) {
          tokens.push_back(token);
      }
      // 输出分割后的字母 
      for (const auto& t : tokens) {
          std::cout << t << std::endl;
      }
      
      
      std::istream& getline(std::istream& is, std::string& str, char delim);  delim分隔符默认是换行符
      
      ```

- Brian Kernighan算法    也可以使用移位运算符

  - 用于计算一个整数的二进制表示中1的个数的有效方法

    - ```c++
      int countSetBits(int n) {
          int count = 0;
          while (n != 0) {
              n = n & (n - 1);
              count++;
          }
          return count;
      }
      //计算末尾连续的1
      int last_1(int n){
              int count=0;
              while((n & 1)==1){
                  count++;
                  n=n>>1;
              }
              return count;
          }
      ```

- 位运算奇妙结论

  - 判断奇偶：`n & 1` 结果为1表示奇数，为0表示偶数。
  - 判断两个数是否相等：`a ^ b == 0` 表示 `a` 和 `b` 相等
  - n & (n - 1)`：清除`n`的最右边的1。例如，`1010 & 1001 = 1000
  - `(n & (n - 1)) == 0`：如果`n`是2的幂，则`n`的二进制表示中只有一个1
  - `a ^= b; b ^= a; a ^= b;`：使用异或操作交换两个变量的值，**不需要额外空间**。

- __builtin_popcount

  - 用于计算一个整数的二进制表示中1的个数（即汉明重量）

  - ```cpp
    int __builtin_popcount(unsigned int x);
    ```

## 7.26

- istringstream和stringstream

  - 头文件<sstream>

  - `std::istringstream`主要用于读取数据，输入流，不能够写入数据
  
  - `std::stringstream`既可以从字符串中读取数据，也可以将数据写入字符串
  
  - ```c++
    std::string data = "123 456";
    std::istringstream iss(data);
    int a, b;
    iss >> a >> b;
    
    std::stringstream ss;
    // 写入数据
    ss << "123 456";
    // 读取数据
    int a, b;
    ss >> a >> b;
    // 再次写入数据
    ss.clear(); // 清除状态标志  避免因之前的错误状态导致后续操作失败。
    ss.str(""); // 清空字符串   确保每次写入操作都在一个干净的环境中进行，避免数据混乱
    ```
  
- 函数调用运算符  使该类的对象可以像函数一样被调用

  - ```c++
    class MyClass {
    public:
        void operator() (int i) {
            cout << i << endl;
        }
    };
    int main() {
        MyClass obj;
        // 使用重载的 operator()
        obj(10);  // 输出: 10
        return 0;
    }
    ```

- [十进制小数转化为二进制小数 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/decimal-decimals-are-converted-to-binary-fractions.html)

  - 十进制整数转化为二进制：除二取余，逆序排列
  - 十进制小数转化为二进制：乘二取整，顺序排列
  - ![img](https://www.runoob.com/wp-content/uploads/2018/11/210-2.png)
  - ![img](https://www.runoob.com/wp-content/uploads/2018/11/210-3.png)

- 原码，反码，补码**（二进制加减法？**

  - 最高位符号位，0为正数，1为负数  十进制数 +5 的原码表示为`0000 0101`
  - 反码：正数不变，负数除符号位其余所有位取反 十进制数-5的反码表示为`1111 1010`
  - 补码：正数不变，负数反码+1 十进制数 -5 的补码表示为 `1111 1011`

- 0.1+0.2！=0.3

  > 在二进制（计算机使用的系统）中，如果一个分数使用基数（2）的质因数来表示，那么它可以被精确地表示。
  >
  > 2 是 2 的唯一质因数。
  >
  > 因此，1/2、1/4 和 1/8 都可以被精确地表示，因为分母使用了 2 的质因数。
  >
  > 而 1/5 (0.2) 或 1/10 (0.1) 是无限循环的小数，因为分母使用了 5 或 10 的质因数。

- strlen() sizeof()

  - `sizeof()` 是一个运算符，而 `strlen()` 是一个函数。
  - `sizeof()` 计算的是变量或类型所占用的内存字节数，而 `strlen()` 计算的是字符串中字符的个数。   指针表示的字符数组sizeof()会返回指针大小，strlen()仍旧是字符串长度
  - `sizeof()` 可以用于任何类型的数据，而 `strlen()` 只能用于**以空字符 '\0' 结尾的字符串**。
  - sizeof() 计算字符串的长度，包含末尾的 '\0'，strlen() 计算字符串的长度，不包含字符串末尾的 '\0'。

- 输入输出流的控制符[C++输入cout与输出cin（详细用法）_用cin cout输出双精度浮点数-CSDN博客](https://blog.csdn.net/qq_34028920/article/details/77600515)

  - setw(n)
    - **当后面紧跟着的输出字段长度小于 n 的时候，在该字段前面用空格补齐，当输出字段长度大于 n 时，全部整体输出。**
      - cout<<setw(14)<<"hello"<<endl; 
      - cout << "runoob" << setw(4) << "runoob" << endl;

  - hex dec oct
    - cin>>hex>>a;

  - setprecision(n)
    - cout<<setprecision(9)<<a;  输出： 123.456789   cout默认输出六位有效数字

- 字符串转换为字符数组

  - ```c++
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);
    // 使用std::vector<char>存储字符数组   使用迭代器初始化对象
    std::vector<char> charVector(str.begin(), str.end());
    charVector.push_back('\0'); // 添加终止符
    ```

  - [string中c_str()的用法_c++ string str方法-CSDN博客](https://blog.csdn.net/qq_41282102/article/details/82695562)  ？？？？？

    - 为了与C语言兼容，c_str()函数返回一个指向正规C字符串的指针常量

    - > **注意：一定要使用strcpy()函数 等来操作方法c_str()返回的指针。**c_str函数的返回值是**const char*的**，不能直接赋值给**char***，所以就需要我们进行相应的操作转化「通过strcpy函数」。

    - ```C++
      char c[20];//事先声明大小
      string s="1234";
      strcpy(c,s.c_str());  //不能写=，类型错误
      ```


  - const char* 

  - char const*  与前一个等价，指向字符常量的指针，指针可以改变，内容不能改变

  - **char* const** 常量指针，指向不能改变，但内容可以改变

  ```c++
  std::string str;
  std::cout << "Enter a string: ";
  std::getline(std::cin, str);
  // 使用c_str()获取字符数组
  const char* charArray = str.c_str();
  std::cout << "Char Array (using c_str()): " << charArray << std::endl;
  // 使用data()获取字符数组
  const char* charArrayData = str.data();
  std::cout << "Char Array (using data()): " << charArrayData << std::endl;
  ```

## 7.29

- [快速排序算法C++实现（超详细解析！！！！）_c++快速排序-CSDN博客](https://blog.csdn.net/weixin_45031801/article/details/126962679)

  - 注意判断条件！！！

- [归并排序算法C++实现（超详细解析！！！！）_c++归并排序-CSDN博客](https://blog.csdn.net/weixin_45031801/article/details/127034720)

- [1.0 十大经典排序算法 | 菜鸟教程 (runoob.com)](https://www.runoob.com/w3cnote/ten-sorting-algorithm.html)

- [【排序(C++实现)】：基数排序_基数排序c++-CSDN博客](https://blog.csdn.net/bqw18744018044/article/details/81810190)

- [选择排序为什么是不稳定的？_选择排序为什么不稳定-CSDN博客](https://blog.csdn.net/qq_45795744/article/details/121353099)

- [一文看懂哈希表并学会使用C++ STL 中的哈希表_哈希表有哪些函数-CSDN博客](https://blog.csdn.net/Peealy/article/details/116895964)

- substr()方法

  - 当调用`haystack.substr(i, len2)`时，`substr`方法会从位置`i`开始，提取长度为`len2`的子字符串，包含起始位置

  - C++内置查找子字符串：`std::string::find`  pos就是第一个索引

    - ```c++
      #include <iostream>
      #include <string>
      int main() {
          std::string text = "ABABDABACDABABCABAB";
          std::string pattern = "ABABCABAB";
          size_t pos = text.find(pattern);
          if (pos != std::string::npos) {
              std::cout << "Found pattern at index " << pos << std::endl;
          } else {
              std::cout << "Pattern not found" << std::endl;
          }
          return 0;
      }
      ```

  - 通用搜索算法search，包括string，vector   distance可以计算两个迭代器之间的距离

    - ```C++
      #include <iostream>
      #include <string>
      #include <algorithm>
      int main() {
          std::string text = "ABABDABACDABABCABAB";
          std::string pattern = "ABABCABAB";
          auto it = std::search(text.begin(), text.end(), pattern.begin(), pattern.end());
          if (it != text.end()) {
              size_t index = std::distance(text.begin(), it);
              std::cout << "Found pattern at index " << index << std::endl;
          } else {
              std::cout << "Pattern not found" << std::endl;
          }
          return 0;
      }
      ```

## 7.30

- 二分查找    标准模板分为三种情况进行精准匹配   **left<=right**

  - ```c++
    int binarySearch(const std::vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2; // 防止溢出
    
            if (nums[mid] == target) {
                return mid; // 找到目标值，返回其索引
            } else if (nums[mid] < target) {
                left = mid + 1; // 目标值在右半部分
            } else {
                right = mid - 1; // 目标值在左半部分
            }
        }
    
        return -1; // 没有找到目标值
    }
    
    ```

  - 计算一个数的算数平方根

  - 与二分查找略有不同的是，只需要找到最大的最小值即可，不需要精准匹配，分为两种情况

  - ```c++
    class Solution {
    public:
        int mySqrt(int x) {
            if (x == 0) return 0; // 处理特殊情况
            int left = 1, right = 65536; // 右边界应为65536
            int result = 0; // 初始化结果
            while (left <= right) {
                int mid = left + (right - left) / 2; // 防止溢出
                if ((long long)mid * mid <= x) { // 使用long long防止溢出
                    result = mid; // 更新结果
                    left = mid + 1; // 继续向右查找
                } else {
                    right = mid - 1; // 向左查找
                }
            }
            return result;
        }
    };
    ```

- 递归与迭代的转换——二叉树的中序遍历**（通常会借助栈来实现递归向迭代的转换）**

  - ```c++
    // 定义二叉树节点结构
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x) : val(x), left(NULL), right(NULL) {}
    };
    // 中序遍历迭代实现
    void inorderTraversal(TreeNode* root) {
        std::stack<TreeNode*> stack;
        TreeNode* current = root;
        while (current != NULL || !stack.empty()) {
            // 遍历左子树，将所有左子节点压入栈中
            while (current != NULL) {
                stack.push(current);
                current = current->left;
            }
            // 访问节点
            current = stack.top();
            stack.pop();
            std::cout << current->val << " ";
            // 遍历右子树
            current = current->right;
        }
    }
    void preorderTraversal(TreeNode* root) {
        if (!root) return;
    
        std::stack<TreeNode*> stack;
        stack.push(root);
    
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            std::cout << node->val << " ";
    
            if (node->right) stack.push(node->right);
            if (node->left) stack.push(node->left);
        }
    }
    void postorderTraversal(TreeNode* root) {
        if (!root) return;
    
        std::stack<TreeNode*> stack1, stack2;
        stack1.push(root);
    
        while (!stack1.empty()) {
            TreeNode* node = stack1.top();
            stack1.pop();
            stack2.push(node);
    
            if (node->left) stack1.push(node->left);
            if (node->right) stack1.push(node->right);
        }
    
        while (!stack2.empty()) {
            TreeNode* node = stack2.top();
            stack2.pop();
            std::cout << node->val << " ";
        }
    }
    ```
    
    [【数据结构必备基本知识】递归与迭代的联系、区别与优缺点对比详解_递归和迭代的区别及关系-CSDN博客](https://blog.csdn.net/shuiyixin/article/details/83188384#:~:text=递归是不断调用自身，假设递归自己是一个函数的话，那递归的返回值会当作参数再次传入自身。 迭代是将某一个初值设定，不断放入某一个循环体，得到的值成为一个新值再次放入循环体中，通过循环体中的操作，逐步得到我们想要的结果。,总结一下就是： 程序调用自身称为递归，利用变量的原值推出新值称为迭代 。)

- 基本数据类型的大小

  - **`char`**：通常是1个字节（8位）。
  - **`short`**：通常是2个字节（16位）。
  - **`int`**：通常是4个字节（32位）。
  - **`long`**：通常是4个字节（32位）。
  - **`long long`**：通常是8个字节（64位）。
  - **`float`**：通常是4个字节（32位）。
  - **`double`**：通常是8个字节（64位）。
  - **`bool`**：通常是1个字节（8位）。

## 7.31

- 重写和重载

  > - 重写是指在派生类中重新定义（实现）**基类**中的虚函数，使其具有相同的方法签名（包括方法名、参数列表和返回类型），但实现不同。重写的目的是为了实现多态性，使得在运行时可以根据对象的实际类型调用相应的方法。
  >
  > - 重载是指在**同一个类中**定义多个具有相同名称但参数列表不同的方法。重载的目的是为了提供多个同名方法，以便根据不同的参数类型或数量来调用不同的实现。重载不涉及继承和虚函数

## 8.1

- 链表的基本操作实现
- C++ 中的指针传递是**按值传递**的，因此在函数内部修改指针的值不会影响到调用者。为了解决这个问题，你可以使用双指针（指向指针的指针）来传递头指针，这样你就可以在函数内部修改头指针的值。**传递指针的值只能改变指针指向的内容而不能改变指针本身！！！**

## 8.2

- to_string()将数字转换为字符  或者数字+'\0'

- **贪心算法和动态规划的比较：**
  贪心算法是**自顶向下**求解，只能选择眼前对自己最有利的一步，其他的路径看不见。
  动态规划是**自底向上**求解，逐层递推。

- 动态规划一般都脱离了递归，使用迭代完成，**最核心的思想将结果保存下来减少重复计算，状态转移方程**

- 回溯是递归的副产品，只要有递归就会有回溯 但回溯不一定是递归，所谓递归回溯，**本质上是一种枚举法**。

  - ```c++
    void backtracking(参数) {
        if (终止条件) {
            存放结果;
            return;
        }
    
        for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
            处理节点;
            backtracking(路径，选择列表); // 递归
            回溯，撤销处理结果
        }
    }
    ```

  

# 做题总结

**LeetCode 75**

## 7.22

- 双指针
  - 283.0 移动零 
  - 392.判断子序列
  - 11.盛最多水的容器
  - 1679.K和数对的最大数目
- 数组/字符串
  - **1071.字符串的最大公因子**
  - 1431.拥有最多糖果的孩子
  - 345.反转字符串中的元音字母
  
- 链表

  - **206.反转链表**  迭代or递归（基本情况和递归情况）

  - ```c++
    class Solution {
    public:
        ListNode* reverseList(ListNode* head) {
            if (!head || !head->next) {
                return head;
            }
            ListNode* newHead = reverseList(head->next);
            head->next->next = head;
            head->next = nullptr;
            return newHead;
        }
    };
    //newhead是没啥用的，只用来辅助进行递归过程，不参与任何运算
    ```
  
  - **链表万金油技巧**
    - **初始化一个根节点root指向链表头，同时把最后一个结点指向的空指针nullptr也标注出来**

## 7.23

- 递归
  - LCR 123.图书整理I
  - 326.3的幂
- 链表
  - **328.奇偶链表**  分而治之？
- 哈希表
  - 2215.找出两数组的不同
  - 1207.独一无二的出现次数
- 栈
  - **735.小行星碰撞**

## 7.24

- 队列
  - 933.最近的请求次数
- 二叉树
  - 104.二叉树的最大深度
  - 872.叶子相似的树
  - 199.二叉树的右视图
  - 700.二叉搜索树中的搜索
- 二分查找
  - 374.猜数字大小

## 7.25

- 单调栈
  - **901.股票价格跨度**
  - 739.每日温度
- 位运算
  - **338.比特位计数**
  - 136.只出现一次的数字

## 7.26

- 数组/字符串
  - 151.反转字符串中的单词

## 7.29

- 13.罗马数字转整数
- 14.最长公共前缀
- 20.有效的括号
- 21.合并两个有序链表
- 27.移除元素  
- **28.找出字符串中第一个匹配项的下标**   KMP算法

## 7.30

- 35.搜索插入位置  **二分查找循环条件是left<=right**
- 58.最后一个单词的长度
- 69.x的平方根
- 83.删除排序链表中的重复元素
- 94.二叉树的中序遍历
- 100.相同的树
- 101.对称二叉树

## 8.1

- 141.环形链表
- **160.相交链表**
- 206.反转链表
- 203.移除链表元素
- 19.删除链表的倒数第N个结点
- 409.最长回文串
- 455.分发饼干

## 8.2

- 238.除自身以外数组的乘积
- 443.压缩字符串
- 257.二叉树的所有路径
- 746.使用最小花费爬楼梯

# 小型结论

- 简化代码：for_each()   sort()   lambda   find（也适用于找子字符串）   max_element  search   puts("");输出一个空行

  - ```cpp
    // 定义一个简单的函数，用于打印元素
    void printElement(int element) {
        std::cout << element << " ";
    }
    std::vector<int> vec = {1, 2, 3, 4, 5};
    // 使用 std::for_each 对每个元素执行 printElement 函数
    std::for_each(vec.begin(), vec.end(), printElement);
    
    // 使用 Lambda 表达式对每个元素执行操作
        std::for_each(vec.begin(), vec.end(), [](int element) {
            std::cout << element << " ";
        });
    ```

- 在结构体struct中，成员默认是公有的（public）。
  在类class中，成员默认是私有的（private）。
- **辗转相除法**，欧几里得算法
- size_t 无符号类型，不能表示负数size_t size=vec.size()  
- auto it=vec.begin()     auto size=vec.size()
- 使用递归的排序：快速排序，归并排序，堆排序，希尔排序
- 不稳定的排序：快速排序，选择排序，希尔排序，堆排序 **稳定：冒泡，插入，归并**

  - ![img](https://www.runoob.com/wp-content/uploads/2019/03/sort.png)

- 栈上自动分配内存，堆上手动分配
- 三目运算符 condition ? true_expression : false_expression
- ***闭包：一个函数对象，它可以记住并访问其词法作用域中的变量，即使这个函数在其词法作用域之外被调用。***
- C++中函数不能在另一个函数内部声明，但可以使用lambda匿名函数对象

  - 注意捕获列表是否使用引用

- ***栈溢出，内存泄漏***
- vector之间可以直接进行比较==,!=,>,<
- Brian Kernighan算法（计算二进制中1的个数） KMP算法   Floyd判圈算法 牛顿迭代法
- cin>>和getline()混用时一定要注意清除输入缓冲区的内容！！！
- sizeof()  strlen() 区别（一般也只有字符数组用）
- hex dec-Decimal oct bin-Binary
- const char*, char const*, char* const的区别是什么？
- 递归思路清晰，迭代效率更高，可以先用递归想出思路用迭代实现

# 代码

## bubble_insert_select_shellsort

```C++
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

// 冒泡排序函数
void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                // 交换arr[j]和arr[j + 1]
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

void insertsort(vector<int>& v)  //插入排序不是swap！！！
{
    int length=v.size();
    if(length==1) return;
    for(int i=1;i<length;i++)
    {
        int tmp=v[i];
        int j=i-1;
        while(j>=0 && v[j]>tmp)
        {
            v[j+1]=v[j];
            j--;
        }
        v[j+1]=tmp;
    }
}
void selectsort(vector<int>& v)
{
    int length=v.size();
    for(int i=0;i<length-1;i++)
    {
        int j=i+1;
        int min_index=i;
        for(j;j<length;j++)
        {
            if(v[min_index]>v[j]) min_index=j;
        }
        swap(v[i],v[min_index]);
    }
}
void shellsort(vector<int>& v)
{
    int length=v.size();
    for(int gap=length/2;gap>=1;gap/=2)
    {
        for(int i=0;i<gap;i++)
        {
            for(int j=i+gap;j<length;j+=gap)
            {
                int tmp=v[j];
                int k=j-gap;
                while(k>=i && v[k]>tmp)
                {
                    v[k+gap]=v[k];
                    k=k-gap;
                }
                v[k+gap]=tmp;
            }
        }
    }
}
int main() {
    vector<int> v;
    int a;
    string s;
    getline(cin,s);
    std::stringstream ss(s);
    while(ss>>a)
    {
        v.push_back(a);
    }
    insertsort(v);
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<" ";
    }
    system("pause");
    return 0;
}

```

## mergesort

```c++
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

void merge(vector<int>& v, int left, int mid, int right) {
    vector<int> v_tmp;
    int i=left;int j=mid+1;
    while(i<=mid && j<=right)
    {
        if(v[i]<v[j]){
            v_tmp.push_back(v[i++]);
        }
        else{
            v_tmp.push_back(v[j++]);
        }
    }
    while(i<=mid){
        v_tmp.push_back(v[i++]);
    }
    while(j<=right){
        v_tmp.push_back(v[j++]);
    }
    int k=0;
    for(int z=left;z<=right;z++)
    {
        v[z]=v_tmp[k++];
    }
}

void mergesort(vector<int>& v,int left,int right)
{
    if(left<right)
    {
        int mid=(left+right)/2;
        mergesort(v,left,mid);
        mergesort(v,mid+1,right);
        merge(v,left,mid,right);
    }
}

int main() {
    vector<int> v;
    int a;
    int i=0;
    while(cin>>a&& i<3)
    {
        i++;
        v.push_back(a);
        if(i==3)
        {
            break;
        }
    }
    mergesort(v,0,v.size()-1);
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<" ";
    }
    system("pause");
    return 0;
}

```

## quicksort   两个函数都有left<right

```c++
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

int part(vector<int>& v,int left,int right)
{
    int i=left,j=right;
    int pivot=v[left];
    cout<<left<<endl;
    while(i<j)
    {
        while(v[j]>pivot&&i<j)
        {
            j--;
        }
        if(i<j)
        {
            swap(v[i],v[j]);
            i++;
        }
        while(v[i]<=pivot&& i<j)
        {
            i++;
        }
        if(i<j)
        {
            swap(v[i],v[j]);
            j--;
        }
    }
    return i;
}
void quicksort(vector<int>& v,int left,int right)
{
    if(left<right)
    {
        int pivot_index=part(v,left,right);
        quicksort(v,left,pivot_index-1);
        quicksort(v,pivot_index+1,right);
    }
}
int main() {
    vector<int> v;
    int a;
    int i=0;
    while(cin>>a&& i<3)
    {
        i++;
        v.push_back(a);
        if(i==3)
        {
            break;
        }
    }
    
    quicksort(v,0,v.size()-1);
    for(int i=0;i<v.size();i++)
    {
        cout<<v[i]<<" ";
    }
    system("pause");
    return 0;
}

```

## heapsort

```c++
// 调整堆，使其满足堆的性质
void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i; // 初始化最大元素为根节点
    int left = 2 * i + 1; // 左子节点
    int right = 2 * i + 2; // 右子节点
    // 如果左子节点大于根节点
    if (left < n && arr[left] > arr[largest]) {
        largest = left;
    }
    // 如果右子节点大于根节点
    if (right < n && arr[right] > arr[largest]) {
        largest = right;
    }
    // 如果最大元素不是根节点，则交换并继续调整堆
    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}
// 堆排序主函数
void heapSort(std::vector<int>& arr) {
    int n = arr.size();
    // 构建最大堆（从最后一个非叶子节点开始）
    for (int i = n / 2 - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }
    // 一个个从堆顶取出元素
    for (int i = n - 1; i > 0; i--) {
        // 将当前根节点（最大值）与最后一个元素交换
        std::swap(arr[0], arr[i]);
        // 调整堆，使其满足堆的性质（不包括已排序的部分）
        heapify(arr, i, 0);
    }
}
```

## 二叉树深度优先遍历的迭代实现

```c++
#include <iostream>
#include <stack>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

void preorderTraversal(TreeNode* root) {
    if (!root) return;

    std::stack<TreeNode*> stack;
    stack.push(root);

    while (!stack.empty()) {
        TreeNode* node = stack.top();
        stack.pop();
        std::cout << node->val << " ";

        if (node->right) stack.push(node->right); // 右子节点先入栈
        if (node->left) stack.push(node->left);   // 左子节点后入栈
    }
}
void inorderTraversal(TreeNode* root) {
    std::stack<TreeNode*> stack;
    TreeNode* current = root;

    while (current || !stack.empty()) {
        while (current) {
            stack.push(current);
            current = current->left;
        }
        current = stack.top();
        stack.pop();
        std::cout << current->val << " ";
        current = current->right;
    }
}
void postorderTraversal(TreeNode* root) {
    if (!root) return;

    std::stack<TreeNode*> stack1, stack2;
    stack1.push(root);

    while (!stack1.empty()) {
        TreeNode* node = stack1.top();
        stack1.pop();
        stack2.push(node);

        if (node->left) stack1.push(node->left);
        if (node->right) stack1.push(node->right);
    }

    while (!stack2.empty()) {
        TreeNode* node = stack2.top();
        stack2.pop();
        std::cout << node->val << " ";
    }
}

```

## 0-1背包问题

[动态规划之0-1背包问题（思路详解+表格演示过程+最优解打印方法+详细代码）_请利用动态规划求解0-1背包问题-CSDN博客](https://blog.csdn.net/weixin_44952817/article/details/110136435)

```c++
#include <iostream>
#include <vector>

int knapsack(int W, std::vector<int>& weights, std::vector<int>& values, int n) {
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(W + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int w = 1; w <= W; ++w) {
            if (weights[i - 1] <= w) {
                dp[i][w] = std::max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }
    return dp[n][W];
}
int main() {
    std::vector<int> weights = {2, 3, 4, 5};
    std::vector<int> values = {3, 4, 5, 6};
    int W = 5;
    int n = weights.size();
    std::cout << "Maximum value in knapsack is " << knapsack(W, weights, values, n) << std::endl;
    return 0;
}
```

# 华为笔试准备

1. 数组
2. 字符串
3. 排序
4. **贪心**
5. 递归
6. 循环
7. 滑窗
8. 栈
9. 进制转换
10. 位运算
11. 队列
12. 哈希表
13. 链表
14. 线性表
15. 二分查找



1. 图
2. 树
3. DFS搜索
4. BFS搜索
5. **动态规划**
6. 前缀和
7. 排列组合
8. 矩阵
9. 双指针
10. **回溯**   只要有递归就一定有回溯
11. 状态机
12. **并查集**
13. 正则表达式
14. 分治
15. 枚举
16. 统计

- 判断一个字符串能否转换为数字

  - std::stoi,std::stod等函数，通过捕获异常判断是否成功

    - ```c++
      #include <iostream>
      #include <string>
      #include <stdexcept>
      bool isNumber(const std::string& str) {
          try {
              size_t pos;
              double num = std::stod(str, &pos);
              return pos == str.size(); // 确保整个字符串都被转换
          } catch (const std::invalid_argument& e) {
              return false;
          } catch (const std::out_of_range& e) {
              return false;
          }
      }
      //这里pos会指向第一个未被转换的字符的位置，因此要求str以数字开头，也可以不使用pos
      int main() {
          std::string str1 = "123.45";
          std::string str2 = "abc123";
          if (isNumber(str1)) {
              std::cout << str1 << " 可以转换成数字" << std::endl;
          } else {
              std::cout << str1 << " 不能转换成数字" << std::endl;
          }
          if (isNumber(str2)) {
              std::cout << str2 << " 可以转换成数字" << std::endl;
          } else {
              std::cout << str2 << " 不能转换成数字" << std::endl;
          }
          return 0;
      }
      ```

  - stringstream判断

    - ```c++
      #include <iostream>
      #include <sstream>
      #include <string>
      bool isNumber(const std::string& str) {
          std::istringstream iss(str);
          double num;
          iss >> num;
          return iss.eof() && !iss.fail();
      }
      int main() {
          std::string str1 = "123.45";
          std::string str2 = "abc123";
      
          if (isNumber(str1)) {
              std::cout << str1 << " 可以转换成数字" << std::endl;
          } else {
              std::cout << str1 << " 不能转换成数字" << std::endl;
          }
          if (isNumber(str2)) {
              std::cout << str2 << " 可以转换成数字" << std::endl;
          } else {
              std::cout << str2 << " 不能转换成数字" << std::endl;
          }
          return 0;
      }
      ```

  - 正则表达式

    - ```c++
      #include <iostream>
      #include <regex>
      #include <string>
      bool isNumber(const std::string& str) {
          std::regex pattern("^[-+]?[0-9]*\\.?[0-9]+([eE][-+]?[0-9]+)?$");
          return std::regex_match(str, pattern);
      }
      int main() {
          std::string str1 = "123.45";
          std::string str2 = "abc123";
      
          if (isNumber(str1)) {
              std::cout << str1 << " 可以转换成数字" << std::endl;
          } else {
              std::cout << str1 << " 不能转换成数字" << std::endl;
          }
          if (isNumber(str2)) {
              std::cout << str2 << " 可以转换成数字" << std::endl;
          } else {
              std::cout << str2 << " 不能转换成数字" << std::endl;
          }
          return 0;
      }
      
      regex_match(&c, &c + 1, pattern)//匹配单个字符！！！
      ```

- for_each传入多个参数

  - lambda表达式

    - ```c++
      #include <iostream>
      #include <vector>
      #include <algorithm> // std::for_each
      // 定义一个简单的函数，用于打印元素
      void printElement(int element, string &extraParam) {
          std::cout << element << " (" << extraParam << ") ";
      }
      int main() {
          std::vector<int> vec = {1, 2, 3, 4, 5};
          int extraParam = 10;
          // 使用 lambda 表达式捕获 extraParam 并传递给 printElement
          std::for_each(vec.begin(), vec.end(), [&extraParam](int element) {
              printElement(element, extraParam);
          });
          return 0;
      }
      //注意引用的位置
      ```

  - 函数对象

    - ```c++
      #include <iostream>
      #include <vector>
      #include <algorithm> // std::for_each
      // 定义一个函数对象，用于打印元素
      class PrintElement {
      public:
          PrintElement(int extraParam) : extraParam(extraParam) {}
      
          void operator()(int element) const {
              std::cout << element << " (" << extraParam << ") ";
          }
      private:
          int extraParam;
      };
      int main() {
          std::vector<int> vec = {1, 2, 3, 4, 5};
          int extraParam = 10;
          // 使用函数对象传递 extraParam
          std::for_each(vec.begin(), vec.end(), PrintElement(extraParam));
          return 0;
      }
      //PrintElement(extraParam)返回值是实例，是一个函数对象可以被调用，可以在for_each前提前创建
      ```

- 将字符串转换为数字（参考--判断一个字符串能否转换为数字）

  - std::stoi  std::stod  std::stol  std::stof
  - stringstream提取
  - 将数字转换为字符串：stringstream提取，`std::to_string(num)`

- 函数和函数对象的区别

  - 函数对象通过定义一个类，并重载函数调用运算符operator()来实现

  - ```c++
    class PrintElement {
    public:
        void operator()(int element) const {
            std::cout << element << " ";
        }
    };
    
    class Incrementor {
    public:
        Incrementor(int step) : step(step) {}
    
        void operator()(int& value) const {
            value += step;
        }
    private:
        int step;
    };
    ```

  - 函数对象使用时需要先创建一个函数对象，然后通过对象调用operator
  
- 正则表达式

  - 规则

    > 1. **字符匹配**：
    >    - 普通字符（如 `a`、`b`、`1`、`2` 等）直接匹配自身。
    >    - `.` 匹配除换行符外的任何单个字符。
    > 2. **字符类**：
    >    - `[abc]` 匹配方括号内的任意一个字符，即 `a`、`b` 或 `c`。
    >    - `[^abc]` 匹配不在方括号内的任意一个字符，即除 `a`、`b`、`c` 外的任意字符。
    >    - `[a-z]` 匹配从 `a` 到 `z` 的任意一个小写字母。
    >    - `[0-9]` 匹配从 `0` 到 `9` 的任意一个数字。
    > 3. **量词**：
    >    - `*` 匹配前面的元素零次或多次。
    >    - `+` 匹配前面的元素一次或多次。
    >    - `?` 匹配前面的元素零次或一次。
    >    - `{n}` 匹配前面的元素恰好 `n` 次。
    >    - `{n,}` 匹配前面的元素至少 `n` 次。
    >    - `{n,m}` 匹配前面的元素至少 `n` 次，但不超过 `m` 次。
    > 4. **边界匹配**：
    >    - `^` 匹配字符串的开始。
    >    - `$` 匹配字符串的结束。
    >    - `\b` 匹配单词**边界**。
    >    - `\B` 匹配非单词**边界**。
    > 5. **分组和捕获**：
    >    - `(abc)` 捕获组，匹配并记住匹配的字符串。
    >    - `(?:abc)` 非捕获组，匹配但不记住匹配的字符串。
    > 6. **转义字符**：
    >    - `\` 用于转义特殊字符，例如 `\.` 匹配小数点。
    > 7. **预定义字符类**：
    >    - `\d` 匹配任意一个数字，等价于 `[0-9]`。
    >    - `\D` 匹配任意一个非数字字符，等价于 `[^0-9]`。
    >    - `\w` 匹配任意一个字母、数字或下划线，等价于 `[a-zA-Z0-9_]`。
    >    - `\W` 匹配任意一个非字母、数字或下划线的字符，等价于 `[^a-zA-Z0-9_]`。
    >    - `\s` 匹配任意一个空白字符（包括空格、制表符、换行符等）。
    >    - `\S` 匹配任意一个非空白字符。
    > 8. **或操作**：
    >    - `|` 表示或操作，例如 `a|b` 匹配 `a` 或 `b`。

  - 示例

  - ```c++
    #include <iostream>
    #include <regex>
    #include <string>
    int main() {
        std::regex pattern("\\b\\w+\\b"); // 匹配单词
        std::string str = "Hello, world! This is a test.";
        std::smatch matches;
        std::string::const_iterator start = str.begin();
        std::string::const_iterator end = str.end();//这里的类型声明不能写成auto否则会报错！！！！
        while (std::regex_search(start, end, matches, pattern)) {
            std::cout << "匹配到: " << matches.str() << std::endl;
            start = matches[0].second; // 移动到下一个位置
        }
        return 0;
    }
    //regex_search(str, pattern)是否有，不需要找到全部
    
    
    #include <iostream>
    #include <regex>
    #include <string>
    int main() {
        // 定义一个正则表达式模式，匹配所有的数字
        std::regex pattern("\\d+");
        // 要处理的字符串
        std::string str = "Hello, 12345 and 67890!";
        // 使用 regex_replace 进行替换
        std::string result = std::regex_replace(str, pattern, "NUMBER");
        // 输出结果
        std::cout << "替换后的字符串: " << result << std::endl;
        return 0;
    }
    
     regex pattern(".*(...)(.*\\1).*");//\\1引用第一个捕获组的内容
    ```

  - C++中的使用

    > - `std::regex_search`：用于在字符串中搜索与正则表达式匹配的子字符串。
    > - `std::regex_replace`：用于将匹配的子字符串替换为指定的字符串。
    > - **`std::regex_match` 进行匹配**：`std::regex_match` 函数用于检查字符串是否完全匹配正则表达式模式。

- char* array=“hello”指向的内容不能修改，因为一般指向**字符串常量存储在只读内存区域**

  - char array[] = "hello";    **char *array = "hello";**   char *array = new char[6]; int *ptr = &a
  - []在**栈上**分配内存，可以修改字符串内容，动态内存分配new也可以修改
  - 在 C++ 中，当你将一个字符串常量赋值给一个 `char *` 指针时，编译器会自动将字符串常量的起始地址赋值给指针。因此，**不需要显式**地使用取地址操作符 `&`。

- pair  头文件<utility>

  - std::pair<int, double> p1; *// 默认构造*
  -  std::pair<int, double> p2(10, 20.5); *// 直接初始化*
  - int firstValue = p.first;  *// 获取第一个元素* 
  - std::string secondValue = p.second;  *// 获取第二个元素*

- **模板类**

  - **声明模板类**：使用 `template` 关键字，后跟类型参数（通常用 `typename` 或 `class` 表示）。

    ```c++
    template<typename T>
    class MyClass {
        // ...
    };
    ```

  - **实现模板类**：在类声明中提供具体的实现，其中类型参数 `T` 可以像普通类型一样使用。

    ```c++
    template<typename T>
    class MyClass {
    private:
        T value;
    public:
        MyClass(const T& v) : value(v) {}
        T getValue() const { return value; }
        void setValue(const T& v) { value = v; }
    };
    ```

  - **使用模板类**：创建模板类的实例时，可以指定具体的类型，或者让编译器根据上下文推断类型。

    ```c++
    // 显式指定类型
    MyClass<int> intObject(10);
    // 根据上下文推断类型
    MyClass autoStringObject = MyClass<std::string>("Hello");
    ```

- ```c++
  int num = 65;  // ASCII码为65的字符是'A'
  char ch = static_cast<char>(num);  // ch的值为'A'
  
  int num = 123;
  string str = to_string(num);  // str的值为"123"
  ```

- 牛顿迭代法

  - ```c++
    #include <iostream>
    #include <cmath>
    double cubeRoot(double a, double epsilon = 1e-10) {
        double x = a; // 初始猜测值
        while (true) {
            double nextX = (2 * x + a / (x * x)) / 3;
            if (std::abs(nextX - x) < epsilon) {
                return nextX;
            }
            x = nextX;
        }
    }
    int main() {
        double number;
        std::cout << "请输入一个数: ";
        std::cin >> number;
        double cubeRootValue = cubeRoot(number);
        std::cout << "该数的立方根是: " << cubeRootValue << std::endl;
        return 0;
    }
    ```

  - \section{示例}

    假设我们要用牛顿迭代法求解方程 $ x^3 - a = 0 $ 的根，其中 $ a $ 是一个常数。这个方程的根就是 $ a $ 的立方根。

    1. \textbf{函数和导数}：
       - 函数 $ f(x) = x^3 - a $
       - 导数 $ f'(x) = 3x^2 $

    2. \textbf{迭代公式}：
       $ x_{n+1} = x_n - \frac{x_n^3 - a}{3x_n^2} = x_n - \frac{x_n^3 - a}{3x_n^2} = x_n - \frac{x_n}{3} + \frac{a}{3x_n^2} = \frac{2x_n}{3} + \frac{a}{3x_n^2} $

    3. \textbf{初始猜测值}：选择一个初始猜测值 $ x_0 $，例如 $ x_0 = a $。

    4. \textbf{迭代过程}：
       - 计算 $ x_1 = \frac{2x_0}{3} + \frac{a}{3x_0^2} $
       - 计算 $ x_2 = \frac{2x_1}{3} + \frac{a}{3x_1^2} $
       - 继续迭代，直到满足收敛条件。

    \end{document}

  - 设置输出精度：cout<<**fixed**<<setprecison(1)<<number  输出保留一位小数（定点格式）

  - cout<<setprecision(1)<<number  输出保留一位有效数字 **setprecision在<iomanip>**

- DFS与回溯   回溯法一般用于生成**所有可能的解**，动态规划生成**最优解*

  - [C++基础算法之DFS与回溯_c++ dfs-CSDN博客](https://blog.csdn.net/qq_74729280/article/details/138139706?ops_request_misc=%7B%22request%5Fid%22%3A%22172412143216800178589960%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=172412143216800178589960&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2-138139706-null-null.142^v100^pc_search_result_base8&utm_term=C%2B%2B dfs&spm=1018.2226.3001.4187)

  - [迷宫问题_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/cf24906056f4488c9ddb132f317e03bc?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D3%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=&judgeStatus=&tags=5051&title=&gioEnter=menu)

  - [火车进站_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/97ba57c35e9f4749826dc3befaeae109?tpId=37&tqId=21300&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D3%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37%3Ftag%3D1263&difficulty=3&judgeStatus=undefined&tags=&title=)

  - ```c++
    void backtracking(参数) {
        if (终止条件) {
            存放结果;
            return;
        }
        for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
            处理节点;
            backtracking(路径，选择列表); // 递归
            回溯，==撤销==处理结果
        }
    }
    ```

- 二维vector

  - 声明大小：vector<vector<int>> map(row, vector<int>(column));

- 文件布局

  - ```c++
    // MyClass.h
    #ifndef MYCLASS_H
    #define MYCLASS_H
    class MyClass {
    private:
        int privateVar; // 私有成员变量
    public:
        MyClass(); // 构造函数
        ~MyClass(); // 析构函数
        void publicMethod(); // 公共成员函数
        int getPrivateVar(); // 访问私有成员的公共方法
    };
    #endif // MYCLASS_H
    ```

  - ```c++
    // MyClass.cpp
    #include "MyClass.h"
    MyClass::MyClass() {
        // 构造函数实现
    }
    MyClass::~MyClass() {
        // 析构函数实现
    }
    void MyClass::publicMethod() {
        // 成员函数实现
    }
    int MyClass::getPrivateVar() {
        return privateVar;
    }
    ```

  - ```c++
    // main.cpp
    #include "MyClass.h"
    #include <iostream>
    int main() {
        MyClass myObject; // 创建MyClass的实例
        myObject.publicMethod(); // 调用公共成员函数
        int value = myObject.getPrivateVar(); // 访问私有成员变量
        std::cout << "Private variable value: " << value << std::endl;
        return 0;
    }
    ```

- 类

  - 类的数据成员不能在类的声明中初始化！！！

  - 析构函数和构造函数都没有返回值

  - 一个类中只能有一个析构函数

  - 类成员变量默认为private

  - public：对外可见，对内可见  private：对内可见（只能在类体的作用域内访问赋值）  protected：对内可见，对派生类可见

  - 通过类名访问**静态类成员**：MyClass::num;       **静态成员函数**

  - 静态类成员被所有类对象共享，只有一份

  - 对于静态类成员，其类型可以是**当前类的类型**，而非静态类成员则不可以，除非数据成员的类型为当前类的指针或引用类型（关键看需不需要一个实例）

    - ```c++
      class CBook{
      public:
          CBook m_book;		//false
          static CBook m_VCBook;//true
          CBook *m_pBook;		//true
      }
      ```

    - 静态类成员可以作为**成员函数的默认参数**，非静态不可以

  - 类的静态成员函数只能访问类的静态成员变量，不能访问普通的数据成员（因为静态成员函数属于类而不属于任何一个实例，无法得到实例的数据成员，没有this指针）

  - 友元  一般都在public下声明

    - 友元函数  friend int function(int num);  然后在类外实现
    - 友元类   friend class MyClass;  MyClass可以访问该类的私有成员
    - 友元方法   friend void MyClass::OutPut();   MyClass中的OutPut方法可以访问私有成员

- 命名空间

  - ```c++
    namespace MyLibrary {
        void print() {
            std::cout << "Hello from MyLibrary!" << std::endl;
        }
    }
    int main() {
        // 使用命名空间名称作为前缀来调用函数
        MyLibrary::print();
        // 使用using声明来引入特定的名称
        using MyLibrary::print;
        print(); // 直接调用，无需前缀
        // 使用using namespace声明来引入整个命名空间
        using namespace MyLibrary;
        print(); // 直接调用，无需前缀
        return 0;
    }
    ```

- delete和free的区别
  - new做两件事，一是分配内存，二是调用类的构造函数；同样，delete会调用类的析构函数和释放内存。而malloc和free只是分配和释放内存。（对于类或结构体来说）
  - 相比于malloc和free分别调用构造函数和析构函数
  - 会递归调用，可以编译但运行报错
   ```c++
  struct Object{
  	Object(int i):data(i){}
  	~Object(){
      delete this;//等价于this->~Object();free(this);
  	}
  	int data;
  }  

- 动态规划    ==怎么区分动态规划和回溯问题？？？==

  - [ACM 金牌选手教你动态规划的本质。力扣 No.72 编辑距离，真·动画教编程，适合语言初学者或编程新人。_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1FJ4m1M7RJ/?spm_id_from=333.788&vd_source=8b8b2b5a21f99c988184d3ef69173eac)==我的神！！！！！==
  - [C++之动态规划（动态规划入门）_c++动态规划-CSDN博客](https://blog.csdn.net/m0_62755690/article/details/121142019)
  - [【0-1背包问题 】详细解析+图解+详细代码-CSDN博客](https://blog.csdn.net/qq_40802813/article/details/119579370)
  - [C++动态规划详解-CSDN博客](https://blog.csdn.net/weixin_51951103/article/details/120241450)
  - 关键：**状态转移方程** **状态变量**  用空间换时间 ，重叠子问题，无后效性
  - 能用动态规划解决的问题一般也能用递归
  - [走方格的方案数_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/e2a22f0305eb4f2f9846e7d644dba09b?tpId=37&tqId=21314&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D3%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37%3Ftag%3D1263&difficulty=2&judgeStatus=undefined&tags=&title=)
  - [公共子串计算_牛客题霸_牛客网 (nowcoder.com)](https://www.nowcoder.com/practice/98dc82c094e043ccb7e0570e5342dd1b?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D3%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37%3Ftag%3D1263&difficulty=3&judgeStatus=&tags=&title=&gioEnter=menu)
  - 递推和记忆化搜索
    - 递推是一种**自底向上**的方法，从已知的最小问题开始，逐步解决更大的问题，直到解决最终的问题。**（常用）**
    - 记忆化搜索是一种**自顶向下**的方法，通过**递归**解决大问题，并将中间结果存储起来以避免重复计算。
  - **动态规划五步法**
    - **构造问题**
    - **拆解子问题（状态变量）**
    - **求解简单子问题**
    - **通过已知问题来求解（状态转移方程）**
    - **判断复杂度**
  - ==动态规划的状态转移压缩==
  - 动态规划不一定是最优解 [3. 无重复字符的最长子串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-substring-without-repeating-characters/solutions/227999/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/)（滑动窗口）

- C++中全局变量和静态变量会初始化为0，但是局部变量不会，内容随机

- **\#include <bits/stdc++.h>**包含了几乎所有标准库的头文件

- mergesort和quicksort的主函数一定都要加判断**if (left<right)!!!!**

- 最大公因子gcd求法   辗转相除法   最小公倍数可以用**a*b/gcd(a,b)**求解

  - ```c++
    int gcd(int a,int b)
    {
    	if(a<b)
    	{
    		swap(a,b);
    	}
    	if(b==0)
    	{
    		return a;
    	}
    	return gcd(b,a%b); 
    } 
    ```

- ```cpp
  #include <bitset>
  ```

  - `bitset<32> bst(num);` 这行代码创建了一个包含32位的位集合（bitset），并用变量`num`的值来初始化这个位集合。`num`可以是一个整数类型（如`int`、`unsigned int`等），位集合会根据`num`的值来设置相应的位。

    例如，如果`num`的值是5，那么`bitset<32> bst(5);`会创建一个位集合，其中最低的3位是101（二进制表示的5），其余位都是0。

- KMP算法

  - 使用**前缀函数**，判断一个字符串（主串）中是否有模式串的存在
  - 前缀函数：将一个字符串所有不包含自身的前缀与后缀列出，找到相等匹配的前后缀的长度最大值
  - 过程：将模式串与主串用一个‘#’字符链接，计算合并串的前缀函数，如果有个前缀函数等于模式串的长度则找到
  - 代码：

    - ```c++
      vector<int> pi(str.size());
      for(int i=1;i<str.size();i++){
          int len=pi[i-1];
          while(len!=0 && str[i]!=str[len]){
          	len=pi[len-1];
      	}
          if(str[i]==str[len]){
              pi[i]=len+1;
          }
      }
      ```
  - [28. 找出字符串中第一个匹配项的下标 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
