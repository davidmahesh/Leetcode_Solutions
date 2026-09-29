class Solution:
    def zigZagArrays(self,n,l,r):
        MOD=10**9+7
        m=r-l+1
        if n==1:
            return m%MOD
        size=2*m
        def mat_mul(A,B):
            sz=len(A)
            C=[[0]*sz for _ in range(sz)]
            for i in range(sz):
                for k in range(sz):
                    if A[i][k]==0:
                        continue
                    for j in range(sz):
                        C[i][j]=(C[i][j]+A[i][k]*B[k][j])%MOD
            return C
        def mat_pow(M,p):
            sz=len(M)
            R=[[1 if i==j else 0 for j in range(sz)] for i in range(sz)]
            while p:
                if p&1:
                    R=mat_mul(R,M)
                M=mat_mul(M,M)
                p>>=1
            return R
        T=[[0]*size for _ in range(size)]
        for x in range(m):
            for y in range(m):
                if y<x:
                    T[m+y][x]=(T[m+y][x]+1)%MOD
                if y>x:
                    T[y][m+x]=(T[y][m+x]+1)%MOD
        Tn=mat_pow(T,n-1)
        ans=0
        for x in range(m):
            for s in range(size):
                ans=(ans+Tn[s][x]+Tn[s][m+x])%MOD
        return ans%MOD