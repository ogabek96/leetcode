class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mem = [0]*1001
        for tr in trips:
            for i in range(tr[1], tr[2]):
                mem[i]+=tr[0]
        return max(mem) <= capacity