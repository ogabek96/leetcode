class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ran = [False] * 51
        for start, end in ranges:
            for i in range(start, end + 1):
                ran[i] = True
        for i in range(left, right + 1):
            if ran[i] == False:
                return False
        return True