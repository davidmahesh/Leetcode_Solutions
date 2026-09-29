class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        base = [0] * 26

        for ch in s:
            base[ord(ch) - 97] += 1

        for i in range(n - 1, -1, -1):
            cnt = base[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - 97

                if cnt[x] == 0:
                    possible = False
                    break

                cnt[x] -= 1

            if not possible:
                continue

            t = ord(target[i]) - 97

            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    ans = target[:i] + chr(c + 97)

                    for x in range(26):
                        ans += chr(x + 97) * cnt[x]

                    return ans

        return ""