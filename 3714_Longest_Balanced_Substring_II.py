class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0

        # Case 1: single character substrings
        curr = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                ans = max(ans, curr)
                curr = 1
        ans = max(ans, curr)

        # Case 2: exactly two characters
        def two_char(c1, c2):
            nonlocal ans
            diff = 0
            first = {0: -1}
            for i, ch in enumerate(s):
                if ch != c1 and ch != c2:
                    diff = 0
                    first.clear()
                    first[0] = i
                    continue
                diff += 1 if ch == c1 else -1
                if diff in first:
                    ans = max(ans, i - first[diff])
                else:
                    first[diff] = i

        two_char('a', 'b')
        two_char('a', 'c')
        two_char('b', 'c')

        # Case 3: all three characters
        ca = cb = cc = 0
        first = {(0, 0): -1}

        for i, ch in enumerate(s):
            if ch == 'a':
                ca += 1
            elif ch == 'b':
                cb += 1
            else:
                cc += 1

            key = (ca - cb, ca - cc)
            if key in first:
                ans = max(ans, i - first[key])
            else:
                first[key] = i

        return ans
