class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    def mergeSort(self, arr):
        mid = len(arr) // 2
        if len(arr) == 1:
            return arr
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left, right)
    def merge(self, arr1, arr2):
        a = 0
        b = 0
        res = []
        while a < len(arr1) and b < len(arr2):
            if arr1[a] <= arr2[b]:
                res.append(arr1[a])
                a+=1
            else:
                res.append(arr2[b])
                b+=1
        while a < len(arr1):
            res.append(arr1[a])
            a+=1
        while b < len(arr2):
            res.append(arr2[b])
            b+=1
        return res