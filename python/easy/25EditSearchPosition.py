class Solution:
    # Complexity: O(logn) time [binary search], O(1) space [two variables]
    # Logic: From the problem alone, this is just binary search with a very slight modification.
    # Normally, we would return -1 outside of the loop to indicate "not found", but here we return
    # l instead, which will point to the index that target would be inserted at to keep the sort
    # Also, we set mid = l + (r - l) // 2 instead of mid = (l + r) // 2 to avoid overflow. Always do this.
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l
