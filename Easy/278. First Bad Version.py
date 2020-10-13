# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        return self.findBad(1, n)
    
    def findBad(self, start, end):
        if start == end:
            return start
        mid = int((start + end) / 2)
        if isBadVersion(mid):
            return self.findBad(start, mid)
        else:
            return self.findBad(mid + 1, end)