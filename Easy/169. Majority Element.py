class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        result = None
        for n in nums:
            if cnt == 0:
                result = n
                cnt=1
            elif n == result:
                cnt+=1
            else:
                cnt-=1
        return result