class Solution:
    def braceExpansionII(self, expression):
        n = len(expression)

        def parse(i):
            parts = []
            cur = {""}

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    parts.append(cur)
                    cur = {""}
                    i += 1
                elif expression[i] == '{':
                    part, i = parse(i + 1)
                    cur = {a + b for a in cur for b in part}
                else:
                    ch = expression[i]
                    cur = {a + ch for a in cur}
                    i += 1

            parts.append(cur)

            res = set()
            for part in parts:
                res |= part

            if i < n and expression[i] == '}':
                i += 1

            return res, i

        return sorted(parse(0)[0])
