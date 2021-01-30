class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        res = []
        for i in range(len(words) - 1):
            if words[i] == first and words[i + 1] == second and i + 2 <= len(words) - 1:
                res.append(words[i + 2])
        return res