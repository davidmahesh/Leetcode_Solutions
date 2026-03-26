class Solution:
    def canPartitionGrid(self, grid):
        from collections import defaultdict
        import bisect

        m, n = len(grid), len(grid[0])
        total = sum(grid[i][j] for i in range(m) for j in range(n))

        row_sum = [sum(grid[i]) for i in range(m)]
        col_sum = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        val_rows = defaultdict(list)
        val_cols = defaultdict(list)

        for i in range(m):
            for j in range(n):
                val_rows[grid[i][j]].append(i)
                val_cols[grid[i][j]].append(j)

        for v in val_cols:
            val_cols[v].sort()

        def in_rows(v, r1, r2):
            rows = val_rows.get(v, [])
            idx = bisect.bisect_left(rows, r1)
            return idx < len(rows) and rows[idx] <= r2

        def in_cols(v, c1, c2):
            cols = val_cols.get(v, [])
            idx = bisect.bisect_left(cols, c1)
            return idx < len(cols) and cols[idx] <= c2

        def remove_top(v, r):
            if r + 1 == 1 and n == 1:
                return False
            if r + 1 == 1:
                return grid[0][0] == v or grid[0][n-1] == v
            if n == 1:
                return grid[0][0] == v or grid[r][0] == v
            return in_rows(v, 0, r)

        def remove_bot(v, r):
            rows = m - r - 1
            if rows == 1 and n == 1:
                return False
            if rows == 1:
                return grid[m-1][0] == v or grid[m-1][n-1] == v
            if n == 1:
                return grid[r+1][0] == v or grid[m-1][0] == v
            return in_rows(v, r+1, m-1)

        def remove_left(v, c):
            if m == 1 and c + 1 == 1:
                return False
            if c + 1 == 1:
                return grid[0][0] == v or grid[m-1][0] == v
            if m == 1:
                return grid[0][0] == v or grid[0][c] == v
            return in_cols(v, 0, c)

        def remove_right(v, c):
            cols = n - c - 1
            if m == 1 and cols == 1:
                return False
            if cols == 1:
                return grid[0][n-1] == v or grid[m-1][n-1] == v
            if m == 1:
                return grid[0][c+1] == v or grid[0][n-1] == v
            return in_cols(v, c+1, n-1)

        s_top = 0
        for r in range(m - 1):
            s_top += row_sum[r]
            diff = s_top - (total - s_top)
            if diff == 0:
                return True
            if diff > 0 and remove_top(diff, r):
                return True
            if diff < 0 and remove_bot(-diff, r):
                return True

        s_left = 0
        for c in range(n - 1):
            s_left += col_sum[c]
            diff = s_left - (total - s_left)
            if diff == 0:
                return True
            if diff > 0 and remove_left(diff, c):
                return True
            if diff < 0 and remove_right(-diff, c):
                return True

        return False