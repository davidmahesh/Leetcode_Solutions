class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            freq = [0] * 26
            distinct = 0
            maxf = 0

            for j in range(i, n):
                idx = ord(s[j]) - 97
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                if freq[idx] > maxf:
                    maxf = freq[idx]

                length = j - i + 1
                if maxf * distinct == length:
                    if length > ans:
                        ans = length

        return ans
