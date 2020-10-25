class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            left = 0
            right = len(row) - 1
            ans = -1
            while left <= right:
                mid = int(left + (right - left)/2)
                if row[mid] < 0:
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            if ans != -1:
                res+= len(row) - ans
        return res