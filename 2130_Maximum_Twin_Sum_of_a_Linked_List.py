class Solution:
    def pairSum(self, head):
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        n = len(vals)
        return max(vals[i] + vals[n-1-i] for i in range(n//2))