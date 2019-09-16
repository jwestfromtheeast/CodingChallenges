class Solution:
    # Optimal time: O(n) space: O(1)
    # Simple approach to improve one by one: dp. Notice this problem is just Fibonacci in disguise
    # First, start by identifying the recursive relation and create a simple recursive solution. How can you break down the problem?
    # After writing the recursive solution, improve it with memoization--cache previous results in a hash table or array
    # Then, use your recursive solution to write the solution iteratively (bottom-up). This tends to build up from the start using an array
    # Here, notice we can make another improvement. Since we only ever access the previous 2 elements of an array, can reduce space to O(1)
    # Just hold the previous 2 values and build up from them! We went from O(2^n) time to O(n) time
    def climbStairsR(self, n: int) -> int:
        if n < 1:
            return 0
        memo = {}
        def climbStairsHelper(n, memo):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in memo:
                return memo[n]
            memo[n] = climbStairsHelper(n - 1, memo) + climbStairsHelper(n - 2, memo)
            return memo[n]
        return climbStairsHelper(n, {})
    
    def climbStairsss(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 3:
            return n
        memo = [1, 2]
        for i in range(2, n):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[-1]
    
    def climbStairss(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 3:
            return n
        memo = [0 for i in range(n)]
        memo[0], memo[1] = 1, 2
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[-1]
    
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 3:
            return n
        curr, prev = 2, 1
        for i in range(2, n):
            curr, prev = curr + prev, curr
        return curr