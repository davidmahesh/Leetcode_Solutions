from collections import deque
class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = {}

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        full = (1 << k) - 1
        sr, sc = start

        best = {}
        q = deque()

        mask = 0
        if (sr, sc) in litter:
            mask |= 1 << litter[(sr, sc)]

        best[(sr, sc, mask)] = energy
        q.append((sr, sc, energy, mask, 0))

        while q:
            x, y, e, mask, dist = q.popleft()

            if mask == full:
                return dist

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if classroom[nx][ny] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1

                if classroom[nx][ny] == 'R':
                    ne = energy

                nm = mask

                if (nx, ny) in litter:
                    nm |= 1 << litter[(nx, ny)]

                state = (nx, ny, nm)

                if ne > best.get(state, -1):
                    best[state] = ne
                    q.append((nx, ny, ne, nm, dist + 1))

        return -1
