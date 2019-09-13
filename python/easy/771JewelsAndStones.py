# Leetcode 771
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        num = 0
        for j in J:
            jewels[j] = True
        for s in S:
            if s in jewels:
                num += 1
        return num

    # Or use built in set function
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        num = 0
        for s in S:
            if s in jewels:
                num += 1
        return num