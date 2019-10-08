def Solution():
    # Potential changes: make pairs in prev arrays, so can append pair + [nums[idx], nums[after]]
    # Have an if/else in before loop, to create a new dict entry or append to existing, vs fetch, add, replace
    # Complexity: Time O(n^2) average, O(n^3) rare worst (if a lot of pairs in prev with same sum), Space O(n^2)
    def fourNumberSum(self, nums, target):
        ans = []
        prev = {}
        for idx in range(1, len(nums) - 1):
            for after in range(idx + 1, len(nums)):
                comp = target - (nums[idx] + nums[after])
                if comp in prev:
                    for pairs in prev[comp]:
                        ans.append([pairs[0], pairs[1], nums[idx], nums[after]])
            for before in range(0, idx):
                sum = nums[before] + nums[idx]
                sumSet = prev.get(sum, [])
                sumSet.append((nums[before], nums[idx]))
                prev[sum] = sumSet
        return ans