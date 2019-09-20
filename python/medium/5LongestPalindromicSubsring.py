class Solution:
    # Idea: Similar to palindromic substrings (647)
    # Here, we consider all palindromic substrings, and find the longest one
    # Expand off of each character in the string to find the longest palindrome available
    # Run it from i to i AND i to i + 1 to account for odd and even length strings
    # Complexity: O(n^2) time, O(1) space
    def getLongest2(self, s: str, i: int, j: int):
        res = ''
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res = s[i:j + 1]
            i -= 1
            j += 1
        return res
        
    def longestPalindrome2(self, s: str) -> str:
        if len(s) < 2:
            return s
        res = ''
        for i in range(len(s)):
            odd = self.getLongest(s, i, i)
            if len(odd) > len(res):
                res = odd
            even = self.getLongest(s, i, i + 1)
            if len(even) > len(res):
                res = even
        return res

    # Speed consideration: all of these string operations are slow. Use tuples instead
    # Doesn't improve Big-O, but runs faster
    def getLongest(self, s: str, i: int, j: int):
        res = (0, 0)
        while i >= 0 and j < len(s) and s[i] == s[j]:
            res = (i, j)
            i -= 1
            j += 1
        return res
        
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        res = (0, 0)
        for i in range(len(s)):
            odd = self.getLongest(s, i, i)
            if odd[1] - odd[0] > res[1] - res[0]:
                res = odd
            even = self.getLongest(s, i, i + 1)
            if even[1] - even[0] > res[1] - res[0]:
                res = even
        return s[res[0]:res[1] + 1]