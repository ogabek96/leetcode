class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = ''
        for ch in S:
            if ch != '-':
                s+=ch.upper()
        split = int(len(s) / K)
        carry = len(s) % K
        result = ''
        if carry != 0:
            result+=s[:carry]
            if carry < len(s):
                result+='-'
            
        for i in range(carry, len(s), K):
            result+=s[i: i+K]
            if i != len(s) - K:
                result+='-'
        return result