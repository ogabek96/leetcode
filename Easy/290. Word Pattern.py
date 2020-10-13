class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        leng = len(pattern)
        words = s.split()
        if leng != len(words):
            return False
        inc = []
        for i in range(leng):
            if pattern[i] not in m and words[i] not in inc:
                m[pattern[i]] = words[i]
                inc.append(words[i])
            elif m.get(pattern[i]) != words[i]:
                return False
        return True