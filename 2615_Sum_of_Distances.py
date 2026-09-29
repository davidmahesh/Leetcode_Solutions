from collections import defaultdict

class Solution:
    def distance(self, nums):
        index_map = defaultdict(list)
        for i, v in enumerate(nums):
            index_map[v].append(i)
        
        arr = [0] * len(nums)
        
        for indices in index_map.values():
            n = len(indices)
            prefix = 0
            total = sum(indices)
            
            for k, idx in enumerate(indices):
                total -= idx
                right = total - idx * (n - k - 1)
                left = idx * k - prefix
                arr[idx] = left + right
                prefix += idx
        
        return arr