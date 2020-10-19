class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        leng = len(arr)
        cnt = 0
        newArr = []
        while(cnt < leng):
            if arr[cnt] == 0:
                newArr.append(0)
                newArr.append(0)
            else:
                newArr.append(arr[cnt])
            cnt+=1
        for i in range(leng):
            arr[i] = newArr[i]