class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        units = 0
        for b in boxTypes:
            if b[0] <= truckSize:
                units+= b[0] * b[1]
                truckSize-=b[0]
            else:
                units+= truckSize * b[1]
                return units
        return units