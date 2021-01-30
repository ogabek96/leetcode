class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        minD = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            minD = min(arr[i + 1] - arr[i], minD)
        res = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minD:
                res.append([arr[i], arr[i + 1]])
        return res