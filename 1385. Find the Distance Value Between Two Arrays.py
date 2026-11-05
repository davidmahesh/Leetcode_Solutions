class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        return sum(
            all(abs(x - y) > d for y in arr2)
            for x in arr1
        )
