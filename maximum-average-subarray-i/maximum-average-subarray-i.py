class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        maxav = sums / k
        for i in range(k, len(nums)):
            sums = sums + nums[i] - nums[i - k]
            maxav = max(sums/k, maxav)
        return maxav