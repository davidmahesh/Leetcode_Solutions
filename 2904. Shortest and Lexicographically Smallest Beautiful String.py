class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        ones = 0
        min_len = n + 1
        ans = ""

        for right in range(n):
            if s[right] == '1':
                ones += 1

            while ones == k:
                length = right - left + 1
                cur = s[left:right + 1]

                if length < min_len or (length == min_len and cur < ans):
                    min_len = length
                    ans = cur

                if s[left] == '1':
                    ones -= 1
                left += 1

        return ans