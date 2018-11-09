#include <iostream>
using namespace std;

int sockMerchant(int n, vector<int> ar) {
    vector<int> helper;
    int pairs = 0;
    for(int i = 0; i < n; i++) {
        if(find(helper.begin(), helper.end(), ar[i]) != helper.end()) {
            pairs++;
            helper.erase(remove(helper.begin(), helper.end(), ar[i]), helper.end());
        }
        else {
            helper.push_back(ar[i]);
        }
    }
    return pairs;
}