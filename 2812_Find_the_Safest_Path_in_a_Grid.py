from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        dist = [[float('inf')]*n for _ in range(n)]
        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r,c))
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c]+1
                    q.append((nr,nc))

        if dist[0][0] == 0 or dist[n-1][n-1] == 0:
            return 0

        heap = [(-dist[0][0], 0, 0)]
        seen = [[False]*n for _ in range(n)]
        while heap:
            neg_safe, r, c = heapq.heappop(heap)
            safe = -neg_safe
            if r == n-1 and c == n-1:
                return safe
            if seen[r][c]:
                continue
            seen[r][c] = True
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0<=nr<n and 0<=nc<n and not seen[nr][nc]:
                    heapq.heappush(heap, (-min(safe, dist[nr][nc]), nr, nc))
        return 0