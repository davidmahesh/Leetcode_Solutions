class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        negatives = 0
        smallest = float('inf')

        for row in matrix:
            for x in row:
                if x < 0:
                    negatives += 1
                v = abs(x)
                total += v
                if v < smallest:
                    smallest = v

        if negatives % 2 == 1:
            total -= 2 * smallest

        return total
