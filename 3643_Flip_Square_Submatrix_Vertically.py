class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        rows = [grid[x + i][y:y + k] for i in range(k)]
        rows.reverse()
        for i in range(k):
            grid[x + i][y:y + k] = rows[i]
        return grid