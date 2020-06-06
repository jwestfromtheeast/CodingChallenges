class Solution:
    # Complexity: Time O(n), Space O(1) [reverse done in-place]
    # Logic: Start with two pointers at the ends of the list, and swap them
    # Increment them towards the center, and continue swapping until they meet
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
