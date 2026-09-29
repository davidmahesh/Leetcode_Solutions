class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        word = [''] * n
        for i in range(n):
            if word[i]:
                continue
            forced = ''
            for j in range(i):
                if lcp[i][j] > 0:
                    forced = word[j]
                    break
            if forced:
                word[i] = forced
            else:
                used = set(word)
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c not in used:
                        word[i] = c
                        break
                else:
                    return ""
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    if word[j] and word[j] != word[i]:
                        return ""
                    word[j] = word[i]
        actual = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    actual[i][j] = 1 + (actual[i+1][j+1] if i+1 < n and j+1 < n else 0)
                if actual[i][j] != lcp[i][j]:
                    return ""
        return ''.join(word)