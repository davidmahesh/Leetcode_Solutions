class Solution:
    def maxProduct(self, root):
        mod = 10**9 + 7
        subs = []

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subs.append(s)
            return s

        total = dfs(root)
        best = 0
        for s in subs:
            best = max(best, s * (total - s))

        return best % mod
