class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace(".", " ")
        hmap = defaultdict(int)
        for word in paragraph.split(" "):
            word = word.lower()
            word = word.strip()
            if word not in banned and word != "":
                hmap[word]+=1
        result = ""
        maxocc = 0
        for word, occ in hmap.items():
            if maxocc < occ:
                result = word
                maxocc = occ
        print(hmap)
        return result