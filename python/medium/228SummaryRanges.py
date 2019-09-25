class Solution:
    # Complexity: Time O(n) Space O(n) (to store ans)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                ans.append(self.convert(nums[start], nums[i - 1]))
                start = i
        ans.append(self.convert(nums[start], nums[-1]))
        return ans
    
    def convert(self, i, j):
        if i == j:
            return str(i)
        else:
            return str(i) + '->' + str(j)