class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if (j + 1 - i) & 1 == 1:
                    sums += sum(arr[i:j+1])
        return sums