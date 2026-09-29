class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        visited = set()
        stack = [start]
        while stack:
            i = stack.pop()
            if arr[i] == 0:
                return True
            if i in visited:
                continue
            visited.add(i)
            for nxt in (i+arr[i], i-arr[i]):
                if 0 <= nxt < n and nxt not in visited:
                    stack.append(nxt)
        return False