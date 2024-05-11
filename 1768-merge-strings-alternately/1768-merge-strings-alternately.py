class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        return res.join([x for x in itertools.chain.from_iterable(itertools.zip_longest(list(word1),list(word2))) if x])
            