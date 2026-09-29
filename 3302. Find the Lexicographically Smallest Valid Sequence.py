class Solution:
    def validSequence(self, word1: str, word2: str):
        m = len(word2)
        last = [-1] * m

        i = len(word1) - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        changed = False

        for i in range(len(word1)):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and (j == m - 1 or i < last[j + 1]):
                ans.append(i)
                j += 1
                changed = True

        return ans if j == m else []