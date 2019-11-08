class Solution:
    # Store all previous numbers, so if we see a previous, have hit a loop
    # Complexity: Time O(n^2) Space O(n)
    def isHappy(self, n: int) -> bool:
        prev = set()
        while n != 1:
            next_n = 0
            while n > 0:
                next_digit = n % 10
                next_n += (next_digit * next_digit)
                n //= 10
            if next_n in prev:
                return False
            prev.add(next_n)
            n = next_n
        return True
    
    def isHappyPythonic(self, n: int) -> bool:
        prev = set()
        while n != 1:
            if n in prev:
                return False
            prev.add(n)
            n = sum([int(c) ** 2 for c in str(n)])
        return True