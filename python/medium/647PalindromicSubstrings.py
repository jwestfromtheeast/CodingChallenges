# Leetcode 647
class Solution:
    # Uses this helper function
    # For each index of string s, count the palindromes in the string by expanding
    # outward from that one character. Also, expand from that and the adjacent character
    # to account for even length strings
    # Complexity: Time O(n^2) Space O(1)
    def expand(self, s, i, j):
        count = 0
        while (i >= 0 and j < len(s) and s[i] == s[j]):
            count += 1
            i -= 1
            j += 1
        return count

    def countSubstrings(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        count = 0
        for i in range(len(s)):
            count += self.expand(s, i, i) # Check odd length strings
            count += self.expand(s, i, i + 1) # Check even length strings
        return count