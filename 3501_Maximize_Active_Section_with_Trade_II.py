from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        cnt1 = s.count('1')
        blk_l, blk_r, blk_len = [], [], []
        i = 0
        while i < n:
            st = i
            while i < n and s[i] == s[st]:
                i += 1
            if s[st] == '0':
                blk_l.append(st)
                blk_r.append(i-1)
                blk_len.append(i-st)
        m = len(blk_len)
        if m < 2:
            return [cnt1]*len(queries)
        pairs = [blk_len[k]+blk_len[k+1] for k in range(m-1)]
        size = 1
        while size < len(pairs):
            size <<= 1
        tree = [0]*(2*size)
        for k in range(len(pairs)):
            tree[size+k] = pairs[k]
        for k in range(size-1, 0, -1):
            tree[k] = max(tree[2*k], tree[2*k+1])
        def rmq(ql, qr):
            if ql > qr:
                return 0
            res = 0
            ql += size; qr += size+1
            while ql < qr:
                if ql&1: res = max(res, tree[ql]); ql += 1
                if qr&1: qr -= 1; res = max(res, tree[qr])
                ql >>= 1; qr >>= 1
            return res
        ans = []
        for l, r in queries:
            i = bisect_left(blk_r, l)
            j = bisect_right(blk_l, r)-1
            if i > m-1 or j < 0 or i >= j:
                ans.append(cnt1)
                continue
            fl = blk_r[i]-max(blk_l[i], l)+1
            ll = min(blk_r[j], r)-blk_l[j]+1
            if i+1 == j:
                ans.append(cnt1+fl+ll)
                continue
            best = max(fl+blk_len[i+1], blk_len[j-1]+ll, rmq(i+1, j-2))
            ans.append(cnt1+best)
        return ans