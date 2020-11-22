class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cnt = 0
        while len(haystack) >= len(needle):
            if haystack.startswith(needle):
                return cnt
            haystack = haystack[1:]
            cnt+=1
        return -1