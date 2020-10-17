class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for i in range(len(arr)):
            if freq.get(arr[i]) != None:
                freq[arr[i]]+=1
            else:
                freq[arr[i]] = 1
        maxim = -1
        for n in arr:
            if freq[n] == n:
                if n > maxim:
                    maxim = n
        return maxim