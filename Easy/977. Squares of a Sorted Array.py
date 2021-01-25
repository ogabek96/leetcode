class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = map(lambda x: x*x, nums)
        return sorted(squares)
        