using namespace std;
#include <iostream>

    long findReverse(long num)
    {
        long rev_num = 0; 
        while (num > 0) 
        { 
             rev_num = rev_num * 10 + num % 10; 
             num = num / 10; 
        }
        return rev_num; 
    } 

int main() {
    long num = 123;
    cout << findReverse(num) << endl;
}