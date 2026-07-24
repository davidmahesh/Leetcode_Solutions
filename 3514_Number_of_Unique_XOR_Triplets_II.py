from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = 2048
        f = [0] * m
        for x in nums:
            f[x] = 1

        a = f[:]
        h = 1
        while h < m:
            for i in range(0, m, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h <<= 1

        for i in range(m):
            a[i] = a[i] * a[i] * a[i]

        h = 1
        while h < m:
            for i in range(0, m, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = (x + y) // 2
                    a[j + h] = (x - y) // 2
            h <<= 1

        n = len(nums)
        ans = 0
        for x in range(m):
            if f[x]:
                ans += 1
            elif a[x] > 0:
                ans += 1
        return ansfrom typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m = 2048
        f = [0] * m
        for x in nums:
            f[x] = 1

        a = f[:]
        h = 1
        while h < m:
            for i in range(0, m, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = x + y
                    a[j + h] = x - y
            h <<= 1

        for i in range(m):
            a[i] = a[i] * a[i] * a[i]

        h = 1
        while h < m:
            for i in range(0, m, h * 2):
                for j in range(i, i + h):
                    x = a[j]
                    y = a[j + h]
                    a[j] = (x + y) // 2
                    a[j + h] = (x - y) // 2
            h <<= 1

        n = len(nums)
        ans = 0
        for x in range(m):
            if f[x]:
                ans += 1
            elif a[x] > 0:
                ans += 1
        return ans