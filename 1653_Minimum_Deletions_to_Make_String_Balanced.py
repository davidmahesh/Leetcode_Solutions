class Solution:
    def minimumDeletions(self, s):
        b = 0
        ans = 0

        for ch in s:
            if ch == 'b':
                b += 1
            else:
                if b > 0:
                    ans += 1
                    b -= 1

        return ans
