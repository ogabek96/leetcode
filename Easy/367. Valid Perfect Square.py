class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 2
        right = num / 2 + 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if mid ** 2 == num:
                return True
            if mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False