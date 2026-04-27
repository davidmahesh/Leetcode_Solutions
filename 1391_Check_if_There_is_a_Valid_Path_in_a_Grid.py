from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        opens = {
            1:{0,1}, 2:{2,3}, 3:{0,3}, 4:{1,3}, 5:{0,2}, 6:{1,2}
        }
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]
        opp = {0:1,1:0,2:3,3:2}
        visited = [[False]*n for _ in range(m)]
        q = deque([(0,0)])
        visited[0][0] = True
        while q:
            r,c = q.popleft()
            if r==m-1 and c==n-1:
                return True
            for d in range(4):
                if d not in opens[grid[r][c]]:
                    continue
                nr,nc = r+dr[d],c+dc[d]
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                    if opp[d] in opens[grid[nr][nc]]:
                        visited[nr][nc] = True
                        q.append((nr,nc))
        return False
