from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        x = y = 0
        res = 0
        for c in commands:
            if c == -2:
                d = (d-1) % 4
            elif c == -1:
                d = (d+1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(c):
                    if (x+dx, y+dy) not in obs:
                        x += dx
                        y += dy
                        res = max(res, x*x + y*y)
        return res