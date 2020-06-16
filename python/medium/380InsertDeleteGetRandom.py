class RandomizedSet:

    # Logic: To support constant-time random access, we must use a list, to get a random index and access the number there.
    # This creates another problem of constant-time inserts and removes, which we can fix by using a map, mapping number->array index
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    # If the value is already in the set, return False. Else, append it to our list and add it to the index map
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True

    # The most tricky function. Here, we want to essentially swap the last element with the element we are removing, in order to remove it in constant time.
    # So, we swap all references to them, then remove the element from both of our structures.
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            # First, get the position of the element we want to remove, and the value of the last item
            p = self.pos[val]
            last = self.nums[-1]
            # Place the last item into the position of the item you are removing
            self.nums[p] = last
            # Update the index of the last item to match the above assignment
            self.pos[last] = p
            # Delete our elements
            self.nums.pop()
            self.pos.pop(val)
            return True
        return False

    # Easy, use the most stable random function to return a random element from an iterable (our nums list, here)
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
