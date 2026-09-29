class Solution:
    def separateSquares(self, squares):
        xs = set()
        for x, y, l in squares:
            xs.add(x)
            xs.add(x + l)
        xs = sorted(xs)
        xi = {v: i for i, v in enumerate(xs)}

        events = []
        for x, y, l in squares:
            events.append((y, 1, xi[x], xi[x + l]))
            events.append((y + l, -1, xi[x], xi[x + l]))
        events.sort()

        seg = [0] * (4 * len(xs))
        cover = [0] * (4 * len(xs))

        def upd(i, l, r, ql, qr, v):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                cover[i] += v
            else:
                m = (l + r) // 2
                upd(i * 2, l, m, ql, qr, v)
                upd(i * 2 + 1, m, r, ql, qr, v)
            if cover[i] > 0:
                seg[i] = xs[r] - xs[l]
            else:
                seg[i] = seg[i * 2] + seg[i * 2 + 1] if r - l > 1 else 0

        slabs = []
        prev_y = events[0][0]
        i = 0
        area = 0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0:
                slabs.append((prev_y, y, seg[1]))
                area += seg[1] * dy
            while i < len(events) and events[i][0] == y:
                _, t, l, r = events[i]
                upd(1, 0, len(xs) - 1, l, r, t)
                i += 1
            prev_y = y

        half = area / 2
        cur = 0

        for y1, y2, w in slabs:
            slab_area = w * (y2 - y1)
            if cur + slab_area >= half:
                return y1 + (half - cur) / w
            cur += slab_area

        return prev_y
