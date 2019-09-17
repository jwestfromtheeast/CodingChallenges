class Solution:
    # Complexity: Time O(n) Space O(1)
    def firstUniqChar(self, s: str) -> int:
        freq = [0 for i in range(26)]
        for c in s:
            freq[ord(c) - 97] += 1
        for i in range(len(s)):
            if freq[ord(s[i]) - 97] == 1:
                return i
        return -1