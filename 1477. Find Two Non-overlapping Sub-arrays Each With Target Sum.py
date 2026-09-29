class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = 10**9
        dp = [INF] * (n + 1)
        ans = INF
        left = 0
        total = 0

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            dp[right + 1] = dp[right]

            if total == target:
                length = right - left + 1
                if dp[left] != INF:
                    ans = min(ans, dp[left] + length)
                dp[right + 1] = min(dp[right + 1], length)

        return -1 if ans == INF else ans
