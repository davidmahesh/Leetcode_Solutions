class Solution:
    def rotateTheBox(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        for row in boxGrid:
            empty = n - 1
            for j in range(n-1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j], row[empty] = row[empty], row[j]
                    empty -= 1
        res = []
        for j in range(n):
            res.append([boxGrid[m-1-i][j] for i in range(m)])
        return res