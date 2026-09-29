class Solution:
    def maxNumberOfBalloons(self,text):
        from collections import Counter
        c=Counter(text)
        return min(c['b'],c['a'],c['l']//2,c['o']//2,c['n'])