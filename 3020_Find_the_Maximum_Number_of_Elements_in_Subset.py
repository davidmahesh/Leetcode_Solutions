from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)
        res = 1
        if cnt[1] >= 2:
            res = cnt[1] if cnt[1] % 2 == 1 else cnt[1] - 1

        for x in cnt:
            if x == 1:
                continue
            length = 0
            cur = x
            while cnt[cur] >= 2:
                length += 2
                cur = cur * cur
            if cnt[cur] >= 1:
                length += 1
            elif length > 0:
                length -= 1
            res = max(res, length)
        return res