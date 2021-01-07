class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = set(arr)
        cnt = 0
        for i in range(1, 10000):
            if i not in nums:
                cnt+=1
            if k == cnt:
                return i
