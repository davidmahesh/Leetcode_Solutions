class Solution:
    def twoEditWords(self, queries, dictionary):
        def diff(a, b):
            return sum(x != y for x, y in zip(a, b))
        return [q for q in queries if any(diff(q, d) <= 2 for d in dictionary)]