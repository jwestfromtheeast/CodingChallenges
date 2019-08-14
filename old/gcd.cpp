//find the gcd of n numbers
using namespace std;

class Solution {
public:
  int gcd(int a, int b) {
    while(b > 0) {
      temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }
  
  int findGCD(int* arr, int len) {
    int result = gcd(arr[0], arr[1]);
    for(int i = 1; i < len - 2; i++) {
      result = gcd(result, arr[i]);
    }
    return result;
  }
};
