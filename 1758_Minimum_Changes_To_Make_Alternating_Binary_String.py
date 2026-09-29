class Solution:
    def minOperations(self, s: str) -> int:
        a = b = 0
        
        for i, c in enumerate(s):
            if c != ('0' if i % 2 == 0 else '1'):
                a += 1
            if c != ('1' if i % 2 == 0 else '0'):
                b += 1
        
        return min(a, b)