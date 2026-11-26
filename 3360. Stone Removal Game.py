class Solution:
    def canAliceWin(self, n):
        cur = 10
        turn = 0
        while n >= cur:
            n -= cur
            cur -= 1
            turn ^= 1
        return turn == 1
