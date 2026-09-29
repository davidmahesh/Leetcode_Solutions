class Solution:
    def sumAndMultiply(self,n):
        d=[c for c in str(n) if c!='0']
        if not d:
            return 0
        x=int(''.join(d))
        return x*sum(int(c) for c in d)