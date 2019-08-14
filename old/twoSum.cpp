//Leetcode 1. Two Sum
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> go;
        for(int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if(go.count(complement)) {
                return {go[complement], i};
            }
            go[nums[i]] = i;
        }
    }
};
