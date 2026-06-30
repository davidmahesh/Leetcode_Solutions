class Solution:
    def numberOfSubstrings(self, s):
        freq = {'a':0,'b':0,'c':0}
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                freq[s[l]] -= 1
                l += 1
            res += l
        return res