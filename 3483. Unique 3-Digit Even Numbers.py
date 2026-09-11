class Solution:
    def totalNumbers(self, digits):
        from itertools import permutations

        return len({
            a * 100 + b * 10 + c
            for a, b, c in permutations(digits, 3)
            if a != 0 and c % 2 == 0
        })
