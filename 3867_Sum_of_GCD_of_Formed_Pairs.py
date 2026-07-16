from math import gcd

class Solution:
    def gcdSum(self, nums):
        arr = []
        mx = 0

        for x in nums:
            if x > mx:
                mx = x
            arr.append(gcd(x, mx))

        arr.sort()

        i = 0
        j = len(arr) - 1
        ans = 0

        while i < j:
            ans += gcd(arr[i], arr[j])
            i += 1
            j -= 1

        return ans