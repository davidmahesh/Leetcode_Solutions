class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1

        odd = -1
        for i in range(26):
            if cnt[i] % 2:
                if odd != -1:
                    return ""
                odd = i

        halfCnt = [x // 2 for x in cnt]
        m = n // 2

        def makePal(left):
            x = ''.join(left)
            if n % 2:
                return x + chr(odd + 97) + x[::-1]
            return x + x[::-1]

        def smallestGreater(pos, left, counts):
            if pos == m:
                res = makePal(left)
                if res > target:
                    return res
                return ""

            t = ord(target[pos]) - 97

            for c in range(t, 26):
                if counts[c] == 0:
                    continue

                counts[c] -= 1
                left.append(chr(c + 97))

                if c > t:
                    rest = []
                    for j in range(26):
                        if counts[j]:
                            rest.extend([chr(j + 97)] * counts[j])

                    candidate = makePal(left + rest)

                    if candidate > target:
                        return candidate

                else:
                    candidate = smallestGreater(pos + 1, left, counts)
                    if candidate:
                        return candidate

                left.pop()
                counts[c] += 1

            return ""

        return smallestGreater(0, [], halfCnt)