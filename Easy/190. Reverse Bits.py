class Solution:
    def reverseBits(self, n: int) -> int:
        nums = []
        while n >= 1:
            nums.append(n % 2)
            n= int(n / 2)
        nums = nums + [0 for i in range(32 - len(nums))]
        cnt = len(list(nums)) - 1
        res = 0
        for n in nums:
            res+= int(n) * 2**cnt
            cnt-=1
        return res