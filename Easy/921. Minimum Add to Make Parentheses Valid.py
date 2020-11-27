class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        cnt = 0
        for ch in S:
            if ch == '(':
                stack.append('(')
            elif len(stack) == 0:
                cnt+=1
            else:
                stack.pop()
        return len(stack) + cnt