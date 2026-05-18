from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        groups = defaultdict(list)
        for i, v in enumerate(arr):
            groups[v].append(i)
        visited = [False]*n
        visited[0] = True
        q = deque([(0, 0)])
        while q:
            i, steps = q.popleft()
            for nxt in [i-1, i+1] + groups[arr[i]]:
                if nxt == n-1:
                    return steps+1
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps+1))
            groups[arr[i]].clear()
        return -1