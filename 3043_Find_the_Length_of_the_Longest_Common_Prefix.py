class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        seen = set()
        for x in arr1:
            s = str(x)
            for i in range(1, len(s)+1):
                seen.add(s[:i])
        res = 0
        for y in arr2:
            s = str(y)
            
            for i in range(1, len(s)+1):
                if s[:i] in seen:
                    res = max(res, i)
        return res
