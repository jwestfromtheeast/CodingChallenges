class Solution:
    # Dynamic programming bottom-up approach
    # Complexity: Time O(nm), Space O(n) (where n is amount, m is length of coins)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        memo = [0] + [float('inf') for _ in range(amount)]
        for coin in coins:
            for change in range(coin, amount + 1):
                memo[change] = min(memo[change], 1 + memo[change - coin])
        return memo[-1] if memo[-1] != float('inf') else -1
