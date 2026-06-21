class Solution:
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for c in costs:
            count[c] += 1

        bought = 0
        for price in range(1, max_cost + 1):
            if count[price] == 0:
                continue
            qty = min(count[price], coins // price)
            bought += qty
            coins -= qty * price
            if coins == 0:
                break
        return bought