class Solution:
    def numberOfSpecialChars(self, word):
        last_lower = {}
        first_upper = {}
        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                if c.lower() not in first_upper:
                    first_upper[c.lower()] = i
        return sum(c in last_lower and c in first_upper and last_lower[c] < first_upper[c] for c in 'abcdefghijklmnopqrstuvwxyz')