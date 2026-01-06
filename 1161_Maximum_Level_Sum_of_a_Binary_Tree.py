class Solution:
    def maxLevelSum(self, root):
        from collections import deque

        q = deque([root])
        lvl = 1
        ans = 1
        best = root.val

        while q:
            s = 0
            for _ in range(len(q)):
                n = q.popleft()
                s += n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if s > best:
                best = s
                ans = lvl
            lvl += 1

        return ans
