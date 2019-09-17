# Leetcode 217
class Solution:
    # Time: O(n) Space O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for num in nums:
            if num in mySet:
                return True
            mySet.add(num)
        return False