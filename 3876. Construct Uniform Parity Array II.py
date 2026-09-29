class Solution:
    def uniformArray(self, nums1):
        nums1.sort()
        possible = {nums1[0] % 2}
        seen = [False, False]
        seen[nums1[0] % 2] = True
        for x in nums1[1:]:
            options = {x % 2}
            for p in range(2):
                if seen[p]:
                    options.add((x - p) % 2)

            possible &= options
            if not possible:
                return False

            seen[x % 2] = True

        return True
