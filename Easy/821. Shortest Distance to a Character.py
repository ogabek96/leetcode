class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0] * n
        c_pos = -n
        for i in range(n):
            if s[i] == c:
                c_pos = i
            res[i] = i - c_pos
        for i in reversed(range(n)):
            if s[i] == c:
                c_pos = i
            res[i] = min(res[i], abs(i - c_pos))
        return res