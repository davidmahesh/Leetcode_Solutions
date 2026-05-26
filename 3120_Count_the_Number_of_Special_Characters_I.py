class Solution:
    def numberOfSpecialChars(self, word):
        s = set(word)
        return sum(c in s and c.upper() in s for c in 'abcdefghijklmnopqrstuvwxyz')
