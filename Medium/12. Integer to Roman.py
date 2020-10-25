class Solution:
    def intToRoman(self, num: int) -> str:
        mem = {
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
            'M': 1000,
        }
        res = ''
        keys = list(reversed(mem.keys()))
        while num > 0:
            for key in keys:
                if num >= mem[key]:
                    num-=mem[key]
                    res+=key
                    break
        return res