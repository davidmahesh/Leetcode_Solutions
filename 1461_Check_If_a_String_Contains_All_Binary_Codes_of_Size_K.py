class Solution:
    def hasAllCodes(self, s, k):
        need = 1 << k
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i:i + k])
            if len(seen) == need:
                return True
        return False