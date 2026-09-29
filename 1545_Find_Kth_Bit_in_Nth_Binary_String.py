class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1
        mid = length // 2 + 1
        
        if k == mid:
            return "1"
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        mirrored = mid - (k - mid)
        bit = self.findKthBit(n - 1, mirrored)
        return "0" if bit == "1" else "1"