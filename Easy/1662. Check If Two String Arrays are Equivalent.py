class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        w2 = ""
        for w in word1:
            w1+=w
        for w in word2:
            w2+=w
        if len(w1) != len(w2):
            return False
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return False
        return True