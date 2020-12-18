class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 1
        right = x
        while left < right:
            mid = right + (left - right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid
        return left - 1