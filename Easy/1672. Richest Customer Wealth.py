class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxs = []
        for alist in accounts:
            temp = 0
            for n in alist:
                temp+=n
            maxs.append(temp)
        return max(maxs)