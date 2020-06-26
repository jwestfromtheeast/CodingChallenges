class Solution:
    # Complexity: O(n) time, O(1) space
    # Logic: The first time a number appears, store it in single. The second time a number appears, it will then clear
    # the single, and store it in double (for 2 appearances). The third time, it will check for single, but since it "ands"
    # with the inverse of double, it will stay cleared, and double will also clear (reverting back to nothing). By the end,
    # we can return the only number remaining in single (which has then appeared one time)
    def singleNumber(self, nums: List[int]) -> int:
        single = double = 0
        for num in nums:
            single = (single ^ num) & ~double
            double = (double ^ num) & ~single
        return single
