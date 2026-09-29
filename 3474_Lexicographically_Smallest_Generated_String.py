class Solution:
    def generateString(self, str1, str2):
        n, m = len(str1), len(str2)
        L = n + m - 1
        word = [''] * L
        fixed = [False] * L
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if word[i+j] == '':
                        word[i+j] = str2[j]
                        fixed[i+j] = True
                    elif word[i+j] != str2[j]:
                        return ""
                    else:
                        fixed[i+j] = True
        for i in range(L):
            if word[i] == '':
                word[i] = 'a'
        for i in range(n):
            if str1[i] == 'F':
                if word[i:i+m] == list(str2):
                    changed = False
                    for j in range(m-1, -1, -1):
                        if not fixed[i+j]:
                            word[i+j] = 'a' if str2[j] != 'a' else 'b'
                            changed = True
                            break
                    if not changed:
                        return ""
        return ''.join(word)