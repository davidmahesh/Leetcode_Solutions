class Solution:
    def createBinaryTree(self, descriptions):
        from collections import defaultdict
        nodes = {}
        children = set()
        def get(v):
            if v not in nodes:
                nodes[v] = TreeNode(v)
            return nodes[v]
        for p, c, left in descriptions:
            pn, cn = get(p), get(c)
            if left:
                pn.left = cn
            else:
                pn.right = cn
            children.add(c)
        for v in nodes:
            if v not in children:
                return nodes[v]