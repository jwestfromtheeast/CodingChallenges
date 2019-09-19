# Leetcode 238
class Solution:
    # Use a pointer and move through the array. Start from the left and move right, multiplying each index of the
    # solution by the product of the previous index. Then, do the same from right to left
    # Complexity: Time O(n) Space O(n) [to store our answer, technically no additional space besides our answer]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)
        sums = [1 for i in range(L)]
        temp = 1
        for i in range(L):
            sums[i], temp = temp, temp * nums[i]
        temp = 1
        for i in range(L - 1, -1, -1):
            sums[i], temp = sums[i] * temp, temp * nums[i]
        return sums