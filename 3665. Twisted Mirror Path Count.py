from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        modd = 1000000007
        r_lenn = len(grid)
        c_lenn = len(grid[0])
        
        dp_mat = [[[0, 0] for _ in range(c_lenn)] for _ in range(r_lenn)]
        dp_mat[0][0][0] = 1
        
        for ii in range(r_lenn):
            for jj in range(c_lenn):
                if grid[ii][jj] == 0:
                    tot_ways = (dp_mat[ii][jj][0] + dp_mat[ii][jj][1]) % modd
                    if jj + 1 < c_lenn:
                        dp_mat[ii][jj + 1][0] = (dp_mat[ii][jj + 1][0] + tot_ways) % modd
                    if ii + 1 < r_lenn:
                        dp_mat[ii + 1][jj][1] = (dp_mat[ii + 1][jj][1] + tot_ways) % modd
                else:
                    if dp_mat[ii][jj][0] > 0 and ii + 1 < r_lenn:
                        dp_mat[ii + 1][jj][1] = (dp_mat[ii + 1][jj][1] + dp_mat[ii][jj][0]) % modd
                    if dp_mat[ii][jj][1] > 0 and jj + 1 < c_lenn:
                        dp_mat[ii][jj + 1][0] = (dp_mat[ii][jj + 1][0] + dp_mat[ii][jj][1]) % modd
                        
        return (dp_mat[r_lenn - 1][c_lenn - 1][0] + dp_mat[r_lenn - 1][c_lenn - 1][1]) % modd
