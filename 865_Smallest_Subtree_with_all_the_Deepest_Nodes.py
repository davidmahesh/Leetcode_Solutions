class Solution:
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return 0, None
            dl, nl = dfs(node.left)
            dr, nr = dfs(node.right)
            if dl > dr:
                return dl + 1, nl
            if dr > dl:
                return dr + 1, nr
            return dl + 1, node

        return dfs(root)[1]
