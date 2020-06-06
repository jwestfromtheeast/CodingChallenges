class Solution:

    # Logic: Initialize our object with each index in the weights list equal to the previous plus the current index from our given list
    # This ensures that there is still an equal distribution our new list, and it is sorted. Now, we can pick a random number in this
    # range (from 1 to the value of the last index of weights), and then use binary search to quickly find where this fits in the list
    def __init__(self, w: List[int]):
        self.weights = [w[0]]
        for i in range(1, len(w)):
            self.weights.append(self.weights[-1] + w[i])

    # Binary search to find proper index faster than n [sqrt(n)]
    def search(self, find):
        l, r = 0, len(self.weights) - 1
        while l < r:
            m = l + (r - l) // 2
            if self.weights[m] < find:
                l = m + 1
            else:
                r = m
        return l

    # pickIndex has a time complexity of O(sqrt(n)), from the binary search above
    def pickIndex(self) -> int:
        find = random.randrange(1, self.weights[-1] + 1)
        return self.search(find)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
