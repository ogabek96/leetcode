class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxv = max(arr)
        return arr.index(maxv)