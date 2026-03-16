class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        sums = set()
        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c])
                for size in range(1, min(m, n)):
                    if r - size < 0 or r + size >= m:
                        break
                    if c - size < 0 or c + size >= n:
                        break
                    total = 0
                    for d in range(size):
                        total += grid[r - size + d][c + d]
                        total += grid[r + d][c + size - d]
                        total += grid[r + size - d][c - d]
                        total += grid[r - d][c - size + d]
                    sums.add(total)
        top = sorted(sums, reverse=True)[:3]
        return top
