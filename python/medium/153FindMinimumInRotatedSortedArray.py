class Solution:
    # binary search
    # essentially, we want to find where the pivot happened, because that gives us our smallest answer (since array originally sorted)
    # if mid is bigger than right, which it wouldnt be in sorted, our pivot is on the right
    # if mid is smaller than right, our pivot must be on the left, or we potentially found our solution (loop will take care of that)
    # Complexity: Time O(logn) Space O(1)
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[left]