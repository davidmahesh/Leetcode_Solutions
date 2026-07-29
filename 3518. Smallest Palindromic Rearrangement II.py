from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        half = [c // 2 for c in cnt]
        mid = ""
        for i in range(26):
            if cnt[i] % 2:
                mid = chr(i + 97)
                break

        LIMIT = k

        def ways():
            rem = sum(half)
            res = 1
            for x in half:
                if x:
                    res *= comb(rem, x)
                    if res >= LIMIT:
                        return LIMIT
                    rem -= x
            return res

        if ways() < k:
            return ""

        left = []

        while sum(half):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                w = ways()
                if w >= k:
                    left.append(chr(i + 97))
                    break
                k -= w
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]