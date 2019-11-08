class Solution:
    # Bottom up dynamic programming solution
    # Cache the max money you can store as you visit each new house. Return the final value
    # Notice for the first solution, we only ever access the previous 2 indexes of the array.
    # So, we can improve space from n to 1 by using a few variables vs an array
    # Complexity: Time O(n) Space O(1)
    def robWorse(self, nums: List[int]) -> int:
        if not nums:
            return 0
        L = len(nums)
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums[0], nums[1])
        money = [0 for i in range(L)]
        money[0] = nums[0]
        for i in range(1, L):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])
        return money[L - 1]
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        prev, curr = 0, nums[0]
        for i in range(1, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)
        return curr