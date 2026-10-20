class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        
        pref = [0] * n
        drop_idx = [0] * n
        for i in range(n - 1):
            pref[i + 1] = pref[i]
            drop_idx[i + 1] = drop_idx[i]
            if nums[i] > nums[i + 1]:
                pref[i + 1] += 1
                drop_idx[i + 1] = i
        divs = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                divs.append(i)
                if i * i != n:
                    divs.append(n // i)
            i += 1
            
        ans = 0
        for k in divs:
            ok = True
            prev_max = -1
            for start in range(0, n, k):
                end = start + k - 1
                drops = pref[end] - pref[start]
                if drops > 1:
                    ok = False
                    break
                if drops == 0:
                    cur_min = nums[start]
                    cur_max = nums[end]
                else:
                    if nums[end] > nums[start]:
                        ok = False
                        break
                    p = drop_idx[end]
                    cur_min = nums[p + 1]
                    cur_max = nums[p]
                if cur_min < prev_max:
                    ok = False
                    break
                prev_max = cur_max
            if ok:
                ans += k
                
        return ans
