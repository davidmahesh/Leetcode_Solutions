class Solution:
    def areSimilar(self, mat, k):
        n = len(mat[0])
        shift = k % n
        if shift == 0:
            return True
        for i, row in enumerate(mat):
            if i % 2 == 0:
                rotated = row[shift:] + row[:shift]
            else:
                rotated = row[n-shift:] + row[:n-shift]
            if rotated != row:
                return False
        return True