class Solution:
    def digitSum(self, s, k):
        while len(s) > k:
            res = ""

            for i in range(0, len(s), k):
                total = sum(int(ch) for ch in s[i:i + k])
                res += str(total)

            s = res

        return s
