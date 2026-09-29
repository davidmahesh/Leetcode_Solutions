class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        tree = [([0] * k, 1 % k) for _ in range(2 * size)]

        def merge(a, b):
            ca, pa = a
            cb, pb = b
            c = ca[:]

            for r in range(k):
                if cb[r]:
                    c[(pa * r) % k] += cb[r]

            return c, (pa * pb) % k

        for i in range(n):
            x = nums[i] % k
            c = [0] * k
            c[x] = 1
            tree[size + i] = (c, x)

        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(idx, val):
            p = size + idx
            x = val % k
            c = [0] * k
            c[x] = 1
            tree[p] = (c, x)

            p //= 2
            while p:
                tree[p] = merge(tree[2 * p], tree[2 * p + 1])
                p //= 2

        def query(l, r):
            left = None
            right = None
            l += size
            r += size + 1

            while l < r:
                if l & 1:
                    left = tree[l] if left is None else merge(left, tree[l])
                    l += 1

                if r & 1:
                    r -= 1
                    right = tree[r] if right is None else merge(tree[r], right)

                l //= 2
                r //= 2

            if left is None:
                return right
            if right is None:
                return left

            return merge(left, right)

        ans = []

        for idx, value, start, x in queries:
            update(idx, value)
            counts, _ = query(start, n - 1)
            ans.append(counts[x])

        return ans
