class Solution:
    def averageOfSubtree(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0, 0

            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)

            total = ls + rs + node.val
            count = lc + rc + 1

            if node.val == total // count:
                self.ans += 1

            return total, count

        dfs(root)
        return self.ans
