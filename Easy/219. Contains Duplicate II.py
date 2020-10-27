class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if dic.get(nums[i]) != None and i - dic.get(nums[i]) <= k:
                return True
            else:
                dic[nums[i]] = i
        return False