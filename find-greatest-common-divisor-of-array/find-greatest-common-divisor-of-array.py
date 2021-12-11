class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minv = min(nums)
        maxv = max(nums)
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        return gcd(minv, maxv)