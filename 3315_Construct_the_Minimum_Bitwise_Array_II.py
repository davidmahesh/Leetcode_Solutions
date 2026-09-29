class Solution:
        def minBitwiseArray(self, nums):
            ans = []
            for x in nums:
                if x % 2 == 0:
                    ans.append(-1)                              
                    continue
                b = 0
                while (x >> b) & 1:
                    b += 1
                ans.append(x ^ (1 << (b - 1)))
            return ans
