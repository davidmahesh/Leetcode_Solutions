from typing import List

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        best_key = '__best__'

        def insert(word, idx):
            node = trie
            length = len(wordsContainer[idx])
            cur_best = node.get(best_key, (-1, float('inf'), float('inf')))
            if (length, idx) < (cur_best[1], cur_best[2]):
                node[best_key] = (idx, length, idx)
            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
                cur_best = node.get(best_key, (-1, float('inf'), float('inf')))
                if (length, idx) < (cur_best[1], cur_best[2]):
                    node[best_key] = (idx, length, idx)

        def query(word):
            node = trie
            best = node[best_key][0]
            for ch in reversed(word):
                if ch not in node:
                    break
                node = node[ch]
                best = node[best_key][0]
            return best

        for i, w in enumerate(wordsContainer):
            insert(w, i)

        return [query(q) for q in wordsQuery]