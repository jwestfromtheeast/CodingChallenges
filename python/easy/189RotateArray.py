class Solution:
    # Simpler way: find new index for each element based on len and k
    # Since we don't want to lose data, store values in new auxillary array
    # Then, since we are modifying the input array, copy the values over
    # Complexity: Time O(n) Space O(n)
    def rotatee(self, nums: List[int], k: int) -> None:
        L = len(nums)
        aux = [0 for i in range(L)]
        for i in range(L):
            aux[(i + k) % L] = nums[i]
        for i in range(L):
            nums[i] = aux[i]

    # Math trick: Reverse array, then reverse array from [0, k) and [k, len)
    # Complexity: Time O(n) Space O(1)
    def reverse(self, nums: List[int], i: int, j: int):
        while (i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        L = len(nums)
        if L < 2:
            return
        k %= L
        self.reverse(nums, 0, L - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, L - 1)