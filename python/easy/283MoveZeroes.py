# Leetcode 283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                nums[i - zeroes] = nums[i]
        for i in range(len(nums) - zeroes, len(nums)):
            nums[i] = 0