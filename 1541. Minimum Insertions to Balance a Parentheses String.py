class Solution:
    def minInsertions(self, s):
        ans = 0
        balance = 0

        for ch in s:
            if ch == '(':
                if balance % 2:
                    ans += 1
                    balance -= 1
                balance += 2
            else:
                balance -= 1
                if balance < 0:
                    ans += 1
                    balance = 1

        return ans + balance
