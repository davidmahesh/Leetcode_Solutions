import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        prev = list(range(-1, n - 1))
        next = list(range(1, n + 1))
        alive = [True] * n

        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        def is_sorted():
            i = 0
            while next[i] < n:
                if nums[i] > nums[next[i]]:
                    return False
                i = next[i]
            return True

        ops = 0

        while not is_sorted():
            s, i = heapq.heappop(heap)

            if not alive[i] or next[i] >= n or not alive[next[i]]:
                continue

            j = next[i]
            nums[i] += nums[j]
            alive[j] = False

            nxt = next[j]
            next[i] = nxt
            if nxt < n:
                prev[nxt] = i

            if prev[i] >= 0:
                heapq.heappush(heap, (nums[prev[i]] + nums[i], prev[i]))
            if nxt < n:
                heapq.heappush(heap, (nums[i] + nums[nxt], i))

            ops += 1

        return ops
