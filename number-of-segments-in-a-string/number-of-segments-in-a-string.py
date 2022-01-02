class Solution:
    def countSegments(self, s: str) -> int:
        segments = s.split(" ")
        cnt = 0
        for seg in segments:
            if seg.strip() != "":
                cnt+=1
        return cnt