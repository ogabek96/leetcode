class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = nums[0]
        for n in nums:
            max1 = max(max1, n)
        max2 = -sys.maxsize - 1
        f2 = False
        for n in nums:
            if n < max1:
                f2 = True
                max2 = max(max2, n)
        max3 = -sys.maxsize - 1
        f3 = False
        for n in nums:
            if n < max2:
                f3 = True
                max3 = max(max3, n)
        print(max1, max2, max3)
        if not f3:
            return max1
        if not f2:
            return max1
        return min(max1, max2, max3)