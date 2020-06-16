class Solution:
    # Complexity: O(mn) time [length of coins list and amount], O(n) space [amount]
    # Logic: Break it down into subproblems, as with other dynamic programming type questions
    # If you haven't, take a look at some easy DP problems, and Coin Change 1 and Knapsack.
    # Here, we create our array to store values, then create our base case, which is 1 at index 0
    # (You can make the amount 0 one way, with 0 coins). From here, go through each coin value
    # and use previously cached results to increment our current index.
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [1] + [0 for _ in range(amount)]
        for coin in coins:
            for change in range(coin, amount + 1):
                memo[change] += memo[change - coin]
        return memo[-1]
