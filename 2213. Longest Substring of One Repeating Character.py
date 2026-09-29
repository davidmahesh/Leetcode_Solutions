from typing import List

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)
        prefix_len = [0] * (4 * n)
        suffix_len = [0] * (4 * n)
        max_len = [0] * (4 * n)
        
        def push_up(node: int, l: int, r: int):
            mid = (l + r) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            len_l = mid - l + 1
            len_r = r - mid
            left_char[node] = left_char[left_child]
            right_char[node] = right_char[right_child]
            max_len[node] = max(max_len[left_child], max_len[right_child])
            prefix_len[node] = prefix_len[left_child]
            suffix_len[node] = suffix_len[right_child]

            if right_char[left_child] == left_char[right_child]:
                max_len[node] = max(max_len[node], suffix_len[left_child] + prefix_len[right_child])
                
                if prefix_len[left_child] == len_l:
                    prefix_len[node] = len_l + prefix_len[right_child]
                
                if suffix_len[right_child] == len_r:
                    suffix_len[node] = len_r + suffix_len[left_child]

        def build(node: int, l: int, r: int):
            if l == r:
                left_char[node] = s[l]
                right_char[node] = s[l]
                prefix_len[node] = 1
                suffix_len[node] = 1
                max_len[node] = 1
                return
            
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            push_up(node, l, r)

        def update(node: int, l: int, r: int, idx: int, ch: str):
            if l == r:
                left_char[node] = ch
                right_char[node] = ch
                return
            
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
            push_up(node, l, r)

        build(1, 0, n - 1)
        
        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            res.append(max_len[1])
            
        return res