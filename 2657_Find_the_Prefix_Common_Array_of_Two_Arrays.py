class Solution:
    def findThePrefixCommonArray(self, A, B):
        seen_a, seen_b = set(), set()
        common = 0
        res = []
        for a, b in zip(A, B):
            seen_a.add(a)
            seen_b.add(b)
            if a in seen_b: common += 1
            if b in seen_a and b != a: common += 1
            res.append(common)
        return res