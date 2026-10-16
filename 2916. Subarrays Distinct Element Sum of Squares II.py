class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7
        
        bit1 = [0] * (n + 2)
        bit2 = [0] * (n + 2)
        
        def add(bit, i, val):
            while i <= n + 1:
                bit[i] += val
                i += i & -i
                
        def query(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
            
        def range_add(l, r, val):
            add(bit1, l, val)
            add(bit1, r + 1, -val)
            add(bit2, l, val * (l - 1))
            add(bit2, r + 1, -val * r)
            
        def prefix_sum(i):
            return query(bit1, i) * i - query(bit2, i)
            
        def range_sum(l, r):
            return prefix_sum(r) - prefix_sum(l - 1)
            
        last = {}
        ans = 0
        cur_sq = 0
        
        for r, x in enumerate(nums, 1):
            l = last.get(x, 0) + 1
            s = range_sum(l, r)
            cur_sq = (cur_sq + 2 * s + (r - l + 1)) % mod
            ans = (ans + cur_sq) % mod
            range_add(l, r, 1)
            last[x] = r
            
        return ans
