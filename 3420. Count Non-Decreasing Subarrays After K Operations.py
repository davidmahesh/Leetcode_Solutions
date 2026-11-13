class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        LOG = n.bit_length()

        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                nxt[i] = stack[-1]
            stack.append(i)

        up = [nxt]
        sm = [[nums[i] * (nxt[i] - i) for i in range(n)]]

        for p in range(1, LOG):
            prev = up[p - 1]
            curr = [-1] * n
            sums = [0] * n

            for i in range(n):
                j = prev[i]
                if j < n and prev[j] != -1:
                    curr[i] = prev[j]
                    sums[i] = sm[p - 1][i] + sm[p - 1][j]

            up.append(curr)
            sm.append(sums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = 0

        for l in range(n):
            pos = l
            used = 0

            for p in range(LOG - 1, -1, -1):
                j = up[p][pos]

                if j != -1:
                    cost = sm[p][pos] - (pref[j] - pref[pos])

                    if used + cost <= k:
                        used += cost
                        pos = j

                        if pos == n:
                            break

            if pos == n:
                ans += n - l
                continue

            end = nxt[pos] - 1
            remaining = k - used

            low, high = pos, end
            best = pos - 1

            while low <= high:
                mid = (low + high) // 2
                cost = nums[pos] * (mid - pos + 1) - (pref[mid + 1] - pref[pos])

                if cost <= remaining:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1

            ans += best - l + 1

        return ans
