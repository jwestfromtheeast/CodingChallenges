class Solution:
    # Another two pointer solution. See 11 Container with Most Water first, if you have not
    # This time, we have a more complex grid, so keep track of the current max height on both sides
    # This will affect how much water you can collect at each spot
    # Complexity Time O(n) Space O(1)
    def trap(self, height: List[int]) -> int:
        max_left, max_right = float('-inf'), float('-inf')
        left, right, trapped = 0, len(height) - 1, 0
        while left <= right:
            max_left, max_right = max(max_left, height[left]), max(max_right, height[right])
            if height[left] < height[right]:
                trapped += max_left - height[left]
                left += 1
            else:
                trapped += max_right - height[right]
                right -= 1
        return trapped