from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj_listt = [[] for _ in range(n)]
        for uu, vv in edges:
            adj_listt[uu].append(vv)
            adj_listt[vv].append(uu)
            
        tin_arr = [0] * n
        tout_arr = [0] * n
        dep_arr = [0] * n
        up_mat = [[0] * 17 for _ in range(n)]
        
        stkk = [(0, 0, 0)]
        timm = 0
        
        while stkk:
            uu, pp, statee = stkk.pop()
            if statee == 0:
                timm += 1
                tin_arr[uu] = timm
                up_mat[uu][0] = pp
                for jj in range(1, 17):
                    up_mat[uu][jj] = up_mat[up_mat[uu][jj-1]][jj-1]
                stkk.append((uu, pp, 1))
                for vv in adj_listt[uu]:
                    if vv != pp:
                        dep_arr[vv] = dep_arr[uu] + 1
                        stkk.append((vv, uu, 0))
            else:
                tout_arr[uu] = timm
                
        fenn = [0] * (n + 2)
        
        def upd_fenn(idxx, vall):
            while idxx <= n:
                fenn[idxx] ^= vall
                idxx += idxx & (-idxx)
                
        def qry_fenn(idxx):
            ress = 0
            while idxx > 0:
                ress ^= fenn[idxx]
                idxx -= idxx & (-idxx)
            return ress
            
        curr_vals = [0] * n
        for ii in range(n):
             mskk = 1 << (ord(s[ii]) - ord('a'))
             curr_vals[ii] = mskk
             upd_fenn(tin_arr[ii], mskk)
             upd_fenn(tout_arr[ii] + 1, mskk)
             
        def get_lcaa(uu, vv):
            if dep_arr[uu] < dep_arr[vv]:
                uu, vv = vv, uu
            difff = dep_arr[uu] - dep_arr[vv]
            for jj in range(17):
                if (difff >> jj) & 1:
                    uu = up_mat[uu][jj]
            if uu == vv:
                return uu
            for jj in range(16, -1, -1):
                if up_mat[uu][jj] != up_mat[vv][jj]:
                    uu = up_mat[uu][jj]
                    vv = up_mat[vv][jj]
            return up_mat[uu][0]
            
        ans_listt = []
        for qq in queries:
            partss = qq.split()
            if partss[0] == "update":
                u_node = int(partss[1])
                chh = partss[2]
                new_mskk = 1 << (ord(chh) - ord('a'))
                diff_mskk = curr_vals[u_node] ^ new_mskk
                curr_vals[u_node] = new_mskk
                upd_fenn(tin_arr[u_node], diff_mskk)
                upd_fenn(tout_arr[u_node] + 1, diff_mskk)
            else:
                u_node = int(partss[1])
                v_node = int(partss[2])
                lca_node = get_lcaa(u_node, v_node)
                tot_mskk = qry_fenn(tin_arr[u_node]) ^ qry_fenn(tin_arr[v_node]) ^ curr_vals[lca_node]
                if (tot_mskk & (tot_mskk - 1)) == 0:
                    ans_listt.append(True)
                else:
                    ans_listt.append(False)
                    
        return ans_listt
