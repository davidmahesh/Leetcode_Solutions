import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        is_sorted = all(nums[i] >= nums[i-1] for i in range(1, n))
        if is_sorted:
            return 0
        
        next_idx = {i: i+1 for i in range(n-1)}
        next_idx[n-1] = None
        prev_idx = {i: i-1 for i in range(1, n)}
        prev_idx[0] = None
        
        values = {i: nums[i] for i in range(n)}
        
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i+1], i, nums[i], nums[i+1]))
        
        operations = 0
        
        violations = set()
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                violations.add(i)
        
        while violations:
            while heap:
                total, left, left_val, right_val = heapq.heappop(heap)
                right = next_idx.get(left)
                
                if right is not None and left in values and right in values:
                    if values[left] == left_val and values[right] == right_val:
                        break
            else:
                break
            
            operations += 1
            merged_value = values[left] + values[right]
            
            prev = prev_idx.get(left)
            next_next = next_idx.get(right)
            
            if left in violations:
                violations.discard(left)
            if prev is not None and prev in violations:
                violations.discard(prev)
            if right in violations:
                violations.discard(right)
            
            del values[right]
            values[left] = merged_value
            
            next_idx[left] = next_next
            if next_next is not None:
                prev_idx[next_next] = left
            
            if prev is not None and values[prev] > merged_value:
                violations.add(prev)
            if next_next is not None and merged_value > values[next_next]:
                violations.add(left)
            
            if prev is not None:
                heapq.heappush(heap, (
                    values[prev] + merged_value,
                    prev,
                    values[prev],
                    merged_value
                ))
            
            if next_next is not None:
                heapq.heappush(heap, (
                    merged_value + values[next_next],
                    left,
                    merged_value,
                    values[next_next]
                ))
        
        return operations
