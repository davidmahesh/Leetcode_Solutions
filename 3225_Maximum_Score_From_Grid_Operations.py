class Solution:
    def maximumScore(self,grid):
        n=len(grid)

        if n==1:
            return 0

        pref=[[0]*(n+1) for _ in range(n)]

        for c in range(n):
            for r in range(n):
                pref[c][r+1]=pref[c][r]+grid[r][c]

        dp=[[[0]*(n+1) for _ in range(n+1)] for _ in range(n)]

        left=[[0]*(n+1) for _ in range(n+1)]
        right=[[0]*(n+1) for _ in range(n+1)]

        for col in range(1,n):

            for cur in range(n+1):
                for prv in range(n+1):

                    if cur<=prv:
                        gain=pref[col][prv]-pref[col][cur]
                        dp[col][cur][prv]=right[prv][0]+gain

                    else:
                        gain=pref[col-1][cur]-pref[col-1][prv]

                        a=right[prv][cur]
                        b=left[prv][cur]+gain

                        if a>b:
                            dp[col][cur][prv]=a
                        else:
                            dp[col][cur][prv]=b

            for cur in range(n+1):

                left[cur][0]=dp[col][cur][0]

                for prv in range(1,n+1):

                    cut=0

                    if prv>cur:
                        cut=pref[col][prv]-pref[col][cur]

                    v=dp[col][cur][prv]-cut

                    if v>left[cur][prv-1]:
                        left[cur][prv]=v
                    else:
                        left[cur][prv]=left[cur][prv-1]

                right[cur][n]=dp[col][cur][n]

                for prv in range(n-1,-1,-1):

                    if dp[col][cur][prv]>right[cur][prv+1]:
                        right[cur][prv]=dp[col][cur][prv]
                    else:
                        right[cur][prv]=right[cur][prv+1]

        ans=0

        for i in range(n+1):

            if dp[n-1][0][i]>ans:
                ans=dp[n-1][0][i]

            if dp[n-1][n][i]>ans:
                ans=dp[n-1][n][i]

        return ans