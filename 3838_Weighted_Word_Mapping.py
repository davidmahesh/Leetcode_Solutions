class Solution:
    def mapWordWeights(self, words, weights):
        res = []
        for word in words:
            w = sum(weights[ord(c)-ord('a')] for c in word) % 26
            res.append(chr(ord('z') - w))
        return ''.join(res)