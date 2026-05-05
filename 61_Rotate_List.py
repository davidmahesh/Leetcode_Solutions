class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        tail.next = head
        steps = n - k
        cur = head
        for _ in range(steps - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head