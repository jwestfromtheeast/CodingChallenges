using namespace std;
#include <iostream>
#include <vector>

int hourglassSum(vector<vector<int>> arr) {
    int largest = -60;
    for(int i = 1; i < 5; i++)
        {
            for(int j = 1; j < 5; j++)
                {
                    int sum = arr[i-1][j-1];
                    sum += arr[i-1][j];
                    sum += arr[i-1][j+1];
                    sum += arr[i][j];
                    sum += arr[i+1][j-1];
                    sum += arr[i+1][j];
                    sum += arr[i+1][j+1];
                    if(sum > largest)
                    {
                        largest = sum;
                    }
                }
        }
    return largest;
}

int main() {
    vector<vector<int>> case3;
    case3[0] = {-1, -1, 0, -9, -2, -2};
    case3[1] = {-2, -1, -6, -8, -2, -5};
    case3[2] = {-1, -1, -1, -2, -3, -4};
    case3[3] = {-1, -9, -2, -4, -4, -5};
    case3[4] = {-7, -3, -3, -2, -9, -9};
    case3[5] = {-1, -3, -1, -2, -4, -5};
    cout << hourglassSum(case3) << endl;
    int bigBoy = hourglassSum(case3);
    cout << bigBoy << endl;
    return 0;
}