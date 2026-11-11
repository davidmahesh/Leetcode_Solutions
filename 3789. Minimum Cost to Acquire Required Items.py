class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        x = min(need1, need2)
        ans = x * min(costBoth, cost1 + cost2)

        ans += max(0, need1 - x) * min(cost1, costBoth)
        ans += max(0, need2 - x) * min(cost2, costBoth)

        return ans
