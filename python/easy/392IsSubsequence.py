class Solution:
    # Complexity: O(n) time [where n is the length of t], O(1) space [two variables]
    # Logic: Two pointer approach, pointer i for string s and pointer j for string t
    # Always increment pointer j, and compare the char at pointers i and j in the strings
    # If they match, increment i as well. If s is a subsequence, you will have iterated through
    # all of s at some point, and can return True. Else, return False.
    # Edge case: s is an empty string, which you can return true, since empty string is a subsequence of any string
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = j = 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
            j += 1
        return False
