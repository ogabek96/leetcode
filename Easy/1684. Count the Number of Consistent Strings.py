class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for w in words:
            if self.isCon(allowed, w):
                res+=1
        return res
    def isCon(self, word1, word2):
        word1 = set(word1)
        for ch in word2:
            if ch not in word1:
                return False
        return True