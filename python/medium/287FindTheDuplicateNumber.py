class Solution:
    # Complexity: O(n) time [while loop], O(1) space
    # Logic: We must not exceed O(1) space for this problem, so no hash table or set allowed.
    # This problem is just a Linked List in disguise (Linked List II on LC if you've done it)
    # By the pigeonhole principle, we have n + 1 spots and each integer is between 1 and n, so there
    # must be a duplicate. Since the numbers and spots in the array are bounded, this can be a linked list in disguise,
    # where you get the value at the index of your current value, and repeat. Do this and check for a cycle.
    # This problem can also be solved with binary search in O(nlogn) time, so this solution remains the fastest.
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        # You find a loop when this loop completes, but it is not guaranteed to be the duplicate value
        while not slow == fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Reset fast back to zero, and the pointers will intersect at the start of the loop, our duplicate
        fast = 0
        while not slow == fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
