class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        curr = 0
        for n in gain:
            curr+=n
            maxAlt = max(curr, maxAlt)
        return maxAlt