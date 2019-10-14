class Solution:
    # Complexity : O(n^2) time, O(1) additional space (besides output array)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        curr = float('inf')
        for i in range(len(nums) - 2):
            if nums[i] == curr:
                continue
            curr = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + curr == 0:
                    ans.append([nums[left], curr, nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + curr < 0:
                    left += 1
                else:
                    right -= 1
        return ans