class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        date = date.split('-')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        if year % 4 == 0 and year % 100 != 0:
            days[2]+=1
        res = 0
        for i in range(1, month):
            res+= days[i]
        res+=day
        return res
        