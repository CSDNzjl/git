#include <iostream>
#include <vector>
#include "output.h"
using namespace std;
int main()
{
    std::vector<int> v1 = {1, 2, 3, 4, 5};
    std::vector<int> v2 = {6, 7, 8, 9, 10};
    operator_overload o1(v1);
    operator_overload o2(v2);
    operator_overload o3 = o1 + o2;
    output::print_vector(o3.arr);
    return 0;
}