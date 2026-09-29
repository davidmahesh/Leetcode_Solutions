class Solution:
    def reverseParentheses(self, s):
        stack = [[]]

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                cur = stack.pop()
                cur.reverse()
                stack[-1].extend(cur)
            else:
                stack[-1].append(ch)

        return ''.join(stack[0])
