from collections import defaultdict, deque
from typing import List


class LazyDelta:
    def __init__(self):
        self.delta = 0

    def merge(self, other):
        self.delta += other.delta
        return self

    def active(self):
        return self.delta != 0

    def reset(self):
        self.delta = 0


class TreeNode:
    def __init__(self):
        self.low = 0
        self.high = 0
        self.lazy = LazyDelta()


class RangeTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.nodes = [TreeNode() for _ in range(self.size * 4 + 5)]
        self._construct(arr, 1, self.size, 1)

    def range_add(self, left, right, value):
        tag = LazyDelta()
        tag.delta = value
        self._modify(left, right, tag, 1, self.size, 1)

    def last_position(self, start, target):
        if start > self.size:
            return -1
        return self._search(start, self.size, target, 1, self.size, 1)

    def _apply(self, idx, tag):
        self.nodes[idx].low += tag.delta
        self.nodes[idx].high += tag.delta
        self.nodes[idx].lazy.merge(tag)

    def _push(self, idx):
        if self.nodes[idx].lazy.active():
            tag = LazyDelta()
            tag.delta = self.nodes[idx].lazy.delta
            self._apply(idx << 1, tag)
            self._apply((idx << 1) | 1, tag)
            self.nodes[idx].lazy.reset()

    def _pull(self, idx):
        self.nodes[idx].low = min(
            self.nodes[idx << 1].low, self.nodes[(idx << 1) | 1].low
        )
        self.nodes[idx].high = max(
            self.nodes[idx << 1].high, self.nodes[(idx << 1) | 1].high
        )

    def _construct(self, arr, l, r, idx):
        if l == r:
            self.nodes[idx].low = arr[l - 1]
            self.nodes[idx].high = arr[l - 1]
            return

        mid = (l + r) >> 1
        self._construct(arr, l, mid, idx << 1)
        self._construct(arr, mid + 1, r, (idx << 1) | 1)
        self._pull(idx)

    def _modify(self, ql, qr, tag, l, r, idx):
        if ql <= l and r <= qr:
            self._apply(idx, tag)
            return

        self._push(idx)
        mid = (l + r) >> 1
        if ql <= mid:
            self._modify(ql, qr, tag, l, mid, idx << 1)
        if qr > mid:
            self._modify(ql, qr, tag, mid + 1, r, (idx << 1) | 1)
        self._pull(idx)

    def _search(self, ql, qr, value, l, r, idx):
        if self.nodes[idx].low > value or self.nodes[idx].high < value:
            return -1

        if l == r:
            return l

        self._push(idx)
        mid = (l + r) >> 1

        if qr >= mid + 1:
            res = self._search(ql, qr, value, mid + 1, r, (idx << 1) | 1)
            if res != -1:
                return res

        if ql <= mid:
            return self._search(ql, qr, value, l, mid, idx << 1)

        return -1


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        positions = defaultdict(deque)

        def parity_score(x):
            return 1 if x % 2 == 0 else -1

        best = 0
        prefix = [0] * len(nums)
        prefix[0] = parity_score(nums[0])
        positions[nums[0]].append(1)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1]
            q = positions[nums[i]]
            if not q:
                prefix[i] += parity_score(nums[i])
            q.append(i + 1)

        tree = RangeTree(prefix)

        for i in range(len(nums)):
            best = max(best, tree.last_position(i + best, 0) - i)

            nxt = len(nums) + 1
            positions[nums[i]].popleft()
            if positions[nums[i]]:
                nxt = positions[nums[i]][0]

            tree.range_add(i + 1, nxt - 1, -parity_score(nums[i]))

        return best
