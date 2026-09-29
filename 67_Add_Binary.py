class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            s = carry
            if i >= 0:
                s += ord(a[i]) - 48
                i -= 1
            if j >= 0:
                s += ord(b[j]) - 48
                j -= 1

            res.append(str(s & 1))
            carry = s >> 1

        return ''.join(reversed(res))
