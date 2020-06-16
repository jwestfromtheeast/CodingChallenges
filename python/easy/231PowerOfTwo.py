class Solution:
    # Easy solution: Complexity O(logn) time, no space used
    # Logic: You know any power of 2 is two times itself n times, so repeatedly divide by 2
    # Powers of 2 will converge to 1, and other numbers will terminate earlier and exit the loop while not equal to 1
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return True if n == 1 else False

    # Time complexity O(1), no space used
    # Faster, but less intuitive solution: Think of how binary numbers work. Any power of two will have a single bit equal to 1,
    # while the rest are equal to 0. Think about how to represent this in terms of a logical statement, and check it compared to n.
    # If you "and" n and n - 1, n has only a single bit equal to 1, and n - 1 has all bits but that bit equal to 1. So this logic yields 0.
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & n - 1) == 0
