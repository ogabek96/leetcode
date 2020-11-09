class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        res = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1:
                if s[i] + s[i + 1] in roman:
                    res+=roman[s[i] + s[i + 1]]
                    i+=1
                else:
                    res+=roman[s[i]]
            else:
                res+=roman[s[i]]
            i+=1
        return res