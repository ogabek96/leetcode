class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for n in nums:
            if n & 1 == 0:
                evens.append(n)
            else:
                odds.append(n)
        res = []
        for i in range(len(nums)):
            if i & 1 == 0:
                res.append(evens[-1])
                evens.pop()
            else:
                res.append(odds[-1])
                odds.pop()
        return res