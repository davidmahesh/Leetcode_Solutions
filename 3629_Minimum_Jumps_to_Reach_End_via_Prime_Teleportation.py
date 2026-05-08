from collections import deque, defaultdict

class Solution:
    def minJumps(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        def isPrime(x):
            if x < 2:
                return False
            if x < 4:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i*i <= x:
                if x % i == 0 or x % (i+2) == 0:
                    return False
                i += 6
            return True
        def primeFactors(x):
            factors = set()
            d = 2
            while d*d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors
        primeToIndices = defaultdict(list)
        for i, v in enumerate(nums):
            for p in primeFactors(v):
                primeToIndices[p].append(i)
        usedPrime = set()
        visited = [False]*n
        visited[0] = True
        queue = deque([0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == n-1:
                    return steps
                for nb in [i-1, i+1]:
                    if 0 <= nb < n and not visited[nb]:
                        visited[nb] = True
                        queue.append(nb)
                if isPrime(nums[i]):
                    p = nums[i]
                    if p not in usedPrime:
                        usedPrime.add(p)
                        for j in primeToIndices[p]:
                            if not visited[j]:
                                visited[j] = True
                                queue.append(j)
            steps += 1
        return steps