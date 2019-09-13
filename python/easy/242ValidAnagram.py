# Leetcode 242
class Solution:
    # Three different ways to solve with similar approach
    def isAnagrammm(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst = [0] * 26
        # Char approach using numeric char values
        for i in range(len(s)):
            lst[ord(s[i]) - ord('a')] += 1
            lst[ord(t[i]) - ord('a')] -= 1
        for a in lst:
            if a != 0:
                return False
        return True
    
    def isAnagramm(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for a in s:
            curr = freq.get(a, 0)
            freq[a] = curr + 1
        for a in t:
            curr = freq.get(a, 0)
            freq[a] = curr - 1
        for key in freq:
            if freq[key] != 0:
                return False
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        for a in s:
            if a in freq:
                freq[a] += 1
            else:
                freq[a] = 1
        for a in t:
            if a in freq:
                freq[a] -= 1
            else:
                return False
        for val in freq.values():
            if val != 0:
                return False
        return True