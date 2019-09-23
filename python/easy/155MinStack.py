class MinStack:
    # Make min stack in python (access to min element at any time)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        self.s.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        if not self.s:
            return None
        return self.s.pop()

    def top(self) -> int:
        if not self.s:
            return None
        return self.s[-1][0]

    def getMin(self) -> int:
        if not self.s:
            return float('inf')
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()