class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        vals = sorted(set(nums))
        size = len(vals)

        count = [0] * (size + 1)
        total = [0] * (size + 1)

        def update(i, c, v):
            while i <= size:
                count[i] += c
                total[i] += v
                i += i & -i

        def query(bit, i):
            res = 0
            while i:
                res += bit[i]
                i -= i & -i
            return res

        def kth(rank):
            idx = 0
            step = 1 << (size.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= size and count[nxt] < rank:
                    idx = nxt
                    rank -= count[nxt]
                step >>= 1

            return idx + 1

        def window_cost():
            mid = kth((x + 1) // 2)
            value = vals[mid - 1]

            left_count = query(count, mid)
            left_sum = query(total, mid)

            right_count = x - left_count
            right_sum = query(total, size) - left_sum

            return value * left_count - left_sum + right_sum - value * right_count

        for i in range(x):
            idx = __import__('bisect').bisect_left(vals, nums[i]) + 1
            update(idx, 1, nums[i])

        costs = [window_cost()]

        for i in range(x, n):
            old = __import__('bisect').bisect_left(vals, nums[i - x]) + 1
            new = __import__('bisect').bisect_left(vals, nums[i]) + 1

            update(old, -1, -nums[i - x])
            update(new, 1, nums[i])

            costs.append(window_cost())

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [float('inf')] * (n + 1)

            for i in range(x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]
