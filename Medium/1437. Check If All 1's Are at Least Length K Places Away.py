class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastInd = - k - 1
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - lastInd - 1 >= k:
                    lastInd = i
                else:
                    print(i, lastInd)
                    return False
        return True