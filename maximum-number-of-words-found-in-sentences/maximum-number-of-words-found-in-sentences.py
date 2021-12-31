class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxw = 0
        for sent in sentences:
            maxw = max(maxw, len(sent.split(" ")))
        return maxw