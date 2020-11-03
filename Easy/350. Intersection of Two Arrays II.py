class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique = {}
        for n in nums2:
            if n in unique:
                unique[n]+=1
            else:
                unique[n] = 1
        result = []
        for n in nums1:
            if unique.get(n) != None and unique[n] > 0:
                result.append(n)
                unique[n]-=1
        return result