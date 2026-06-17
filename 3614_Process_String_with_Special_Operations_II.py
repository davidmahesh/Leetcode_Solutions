class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        cur = 0
        for c in s:
            if c.islower():
                cur += 1
            elif c == '*':
                cur = max(0, cur-1)
            elif c == '#':
                cur *= 2
            lengths.append(cur)

        if not lengths or k >= lengths[-1]:
            return '.'

        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c.islower():
                if k == lengths[i]-1:
                    return c
            elif c == '#':
                k %= (lengths[i]//2)
            elif c == '%':
                k = lengths[i]-1-k

        return '.'