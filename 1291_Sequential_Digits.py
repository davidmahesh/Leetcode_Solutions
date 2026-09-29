class Solution:
    def sequentialDigits(self, low, high):
        ans = []
        s = "123456789"

        for l in range(2, 10):
            for i in range(10 - l):
                x = int(s[i:i + l])
                if low <= x <= high:
                    ans.append(x)

        return ans