class Solution:
    # If you have not, take a look at Problem 198: House Robber
    # We use that solution with a twist. Since this is circular, the first and last houses
    # are now adjacent. As such, we can break the problem down into two linear paths:
    # houses[start, end - 1] and houses[start + 1, end], to avoid breaking the rules.
    # Uses the House Robber I solution with two calls and takes the max. Note: indexes would be faster than slicing
    # Complexity: O(n) time, O(1) space
    def robLinear(self, nums) -> int:
        prev, curr = 0, nums[0]
        for i in range(1, len(nums)):
            prev, curr = curr, max(prev + nums[i], curr)
        return curr
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.robLinear(nums[:-1]), self.robLinear(nums[1:]))