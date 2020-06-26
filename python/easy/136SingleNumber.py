class Solution:
    # Complexity: O(n) time, O(1) space
    # Logic: Our goal here is to use no additional space (besides a single var to return the solution)
    # Think about the commutative property. Essentially, we can move the order of numbers around, or
    # we can say 1 + 2 + 1 = 1 + 1 + 2, etc. The same applies to some logic, like XOR. Here, 1 ^ 2 ^ 1
    # is a valid input to the problem, which can be rearrange to 1 ^ 1 ^ 2. And any number XOR itself is 0.
    # So this simplifies to 0 ^ 2, or solution of 2. The same applies for longer inputs. The doubles nullify themselves.
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
