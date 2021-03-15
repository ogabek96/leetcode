class Solution:
    def reorderSpaces(self, text: str) -> str:
        spCnt=0
        words = []
        for ch in text:
            if ch == " ":
                spCnt+=1
        for w in text.split(" "):
            if w != "":
                words.append(w)
        if len(words) == 1:
            return words[0] + " " * spCnt
        eqSp = spCnt // (len(words) - 1)
        remSp = spCnt - eqSp * (len(words) - 1)
        return (" " * eqSp).join(words) + " " * remSp