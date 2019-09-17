class Solution:
    # Instead of a brute-force O(n^2) solution that compares every index with every other, we can increase space to save time
    # Store all previously seen elements in a map, with a key of the number and a value of the index
    # Now, each pass, check if the complement of the current number is in our map (if we have seen it previously)
    # Complexity: Time O(n) Space O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in prev:
                return [prev[comp], i]
            prev[nums[i]] = i