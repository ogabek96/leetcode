class Solution:
    def maxPower(self, s: str) -> int:
        cnt = 1
        let = s[0]
        maxcnt = 1
        for ch in s[1:]:
            if ch == let:
                cnt+=1
            else:
                let = ch
                cnt = 1
            maxcnt = max(cnt, maxcnt)
        return maxcnt