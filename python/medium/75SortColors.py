class Solution:
    # Complexity: O(n) time, O(1) space [in-place, only numbers needed]
    # Otherwise known as the Dutch National Flag Problem.
    # Logic: A simple solution is to do this in two passes in-place. First, count the frequency
    # of the three colors and store in three variables. Then, go through and reassign them in order to follow this.
    # However, you can look at that code and reduce it down to a single loop. Two variables can keep track of all three colors,
    # by using one to keep track of the rightmost 0, and another to keep track of the leftmost 2, then a third for the current index.
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = i = 0
        right = len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

    # First solution, two loops. Improvements made above
    def sortColorsEasy(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = blue = 0
        for o in nums:
            if o == 0:
                red += 1
            elif o == 1:
                white += 1
            elif o == 2:
                blue += 1
        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < red + white:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums
