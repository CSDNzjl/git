#ifndef OUTPUT_H
#define OUTPUT_H
#include <iostream>
#include <vector>
using namespace std;
class output
{
    public:
    static void print_vector(vector<int>& arr)
    {
        int n = arr.size();
        for(int i=0;i<n;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
        system("pause");
    }
};
class operator_overload
{
    public:
    operator_overload(){};
    operator_overload(vector<int>& arr):arr(arr){};
    operator_overload operator+ (const operator_overload& a)
    {
        vector<int> res;
        int n = a.arr.size();
        for(int i=0;i<n;i++)
        {
            res.push_back((this->arr)[i]+a.arr[i]);
        }
        return res;
    }
    vector<int> arr;
};
#endif

//静态成员，实例成员