class Solution:
    def decodeCiphertext(self, encodedText, rows):
        if rows == 1:
            return encodedText
        cols = len(encodedText) // rows
        matrix = [encodedText[i*cols:(i+1)*cols] for i in range(rows)]
        res = []
        for start in range(cols):
            for r in range(rows):
                c = start + r
                if c < cols:
                    res.append(matrix[r][c])
        return ''.join(res).rstrip()