class Solution:
    # Complexity: O(nlogn) Time [this is due to the sort on differences], O(n) space
    # Logic: Greedy approach. At first, send everyone to City A, then decide afterwards who to actually send to City B
    # (Since we must send half to each). To determine who to send to City B, sort the differences between the cost
    # for each person. Send the first half of this sorted list to City B instead of A. To do this simply,
    # just add the first half of the differences list to the total.
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = sum([cost[0] for cost in costs])
        diff = [cost[1] - cost[0] for cost in costs]
        diff.sort()
        return total + sum(diff[:len(costs)//2])
