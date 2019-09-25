class Solution:
    # Dynamic programming bottom-up approach
    # Complexity: Time O(nm), Space O(n) (where n is amount, m is length of coins)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        memo = [0] + [float('inf') for i in range(1, amount + 1)]
        for coin in coins:
            for change in range(coin, amount + 1):
                if coin <= change:
                    memo[change] = min(1 + memo[change - coin], memo[change])
        return memo[amount] if memo[amount] != float('inf') else -1