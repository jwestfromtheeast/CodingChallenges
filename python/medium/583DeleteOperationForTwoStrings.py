# Leetcode 583
class Solution:
    def lcs(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return 0
        len1, len2 = len(word1), len(word2)
        memo = [[0 for i in range(len2 + 1)] for i in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
        return memo[len1][len2]
    
    def minDistance(self, word1: str, word2: str) -> int:
        longest = self.lcs(word1, word2)
        return (len(word1) - longest) + (len(word2) - longest)