class Solution:
    # Use a two pointer solution. Increment the pointer at the smaller value to keep finding larger answers
    # Complexity: Time O(n), Space O(1)
    def maxArea(self, height: List[int]) -> int:
        left, right, maxi = 0, len(height) - 1, float('-inf')
        while left <= right:
            curr = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            maxi = max(curr, maxi)
        return maxi