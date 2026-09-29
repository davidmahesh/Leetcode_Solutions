class Solution:
    def furthestDistanceFromOrigin(self, moves):
        L = moves.count('L')
        R = moves.count('R')
        blanks = moves.count('_')
        return abs(L - R) + blanks