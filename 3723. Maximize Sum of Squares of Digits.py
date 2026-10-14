class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum < 1 or sum > 9 * num:
            return ""
        ans = []
        for _ in range(num):
            d = min(9, sum)
            ans.append(str(d))
            sum -= d
            
        return ''.join(ans)
