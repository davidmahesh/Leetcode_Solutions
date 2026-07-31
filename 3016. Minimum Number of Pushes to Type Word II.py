from typing import List
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = [0] * 26
        for c in word:
            cnt[ord(c) - 97] += 1
        cnt.sort(reverse=True)
        ans = 0
        for i in range(26):
            if cnt[i] == 0:
                break
            ans += cnt[i] * (i // 8 + 1)
        return ans