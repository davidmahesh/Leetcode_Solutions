class Solution:
    def removeInvalidParentheses(self, s):
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def dfs(i, balance, lrem, rrem, cur):
            if i == len(s):
                if balance == 0 and lrem == 0 and rrem == 0:
                    ans.add(''.join(cur))
                return

            ch = s[i]

            if ch == '(':
                if lrem:
                    dfs(i + 1, balance, lrem - 1, rrem, cur)

                cur.append(ch)
                dfs(i + 1, balance + 1, lrem, rrem, cur)
                cur.pop()

            elif ch == ')':
                if rrem:
                    dfs(i + 1, balance, lrem, rrem - 1, cur)

                if balance:
                    cur.append(ch)
                    dfs(i + 1, balance - 1, lrem, rrem, cur)
                    cur.pop()

            else:
                cur.append(ch)
                dfs(i + 1, balance, lrem, rrem, cur)
                cur.pop()

        dfs(0, 0, left, right, [])
        return list(ans)
