class Solution:
    def smallestSubsequence(self, s):
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        st = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue
            while st and st[-1] > c and last[st[-1]] > i:
                seen.remove(st.pop())
            st.append(c)
            seen.add(c)

        return "".join(st)