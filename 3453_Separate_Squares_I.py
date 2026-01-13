class Solution:
    def separateSquares(self, squares):
        def area_below(y):
            s = 0
            for _, yi, l in squares:
                if y <= yi:
                    continue
                h = min(l, y - yi)
                s += h * l
            return s

        total = sum(l * l for _, _, l in squares)
        lo = min(yi for _, yi, _ in squares)
        hi = max(yi + l for _, yi, l in squares)

        for _ in range(60):
            mid = (lo + hi) / 2
            if area_below(mid) * 2 < total:
                lo = mid
            else:
                hi = mid

        return lo
