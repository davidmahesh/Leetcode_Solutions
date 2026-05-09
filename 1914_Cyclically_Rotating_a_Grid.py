class Solution:
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        for l in range(min(m, n) // 2):
            elems = []
            for c in range(l, n-l):
                elems.append(grid[l][c])
            for r in range(l+1, m-l):
                elems.append(grid[r][n-1-l])
            for c in range(n-2-l, l-1, -1):
                elems.append(grid[m-1-l][c])
            for r in range(m-2-l, l, -1):
                elems.append(grid[r][l])
            sz = len(elems)
            shift = k % sz
            elems = elems[shift:] + elems[:shift]
            idx = 0
            for c in range(l, n-l):
                grid[l][c] = elems[idx]; idx += 1
            for r in range(l+1, m-l):
                grid[r][n-1-l] = elems[idx]; idx += 1
            for c in range(n-2-l, l-1, -1):
                grid[m-1-l][c] = elems[idx]; idx += 1
            for r in range(m-2-l, l, -1):
                grid[r][l] = elems[idx]; idx += 1
        return grid