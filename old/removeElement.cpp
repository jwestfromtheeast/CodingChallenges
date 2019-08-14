//Leetcode: 27. Remove Element
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0; //slow
        for(int i = 0; i < nums.size(); i++) { //fast
            if(nums[i] != val) { //if this loop is not triggered, it adjusts all future elements back by how many times triggered.
                nums[count] = nums[i];
                count++;
            }
        }
        return count;
    }
};
