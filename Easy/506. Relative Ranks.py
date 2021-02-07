class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sortednums = sorted(nums, reverse = True)
        ranks = [-1]* (sortednums[0] + 1)
        for i in range(len(sortednums)):
            ranks[sortednums[i]] = i + 1
        res = []
        for n in nums:
            if ranks[n] == 1:
                res.append('Gold Medal')
            elif ranks[n] == 2:
                res.append('Silver Medal')
            elif ranks[n] == 3:
                res.append('Bronze Medal')
            else:
                res.append(str(ranks[n]))
        return res
        
        