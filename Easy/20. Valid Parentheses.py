class Solution:
    def isValid(self, s: str) -> bool:
        mem = {
            '(': ')',
            '{': '}',
            '[': ']'
        }        
        stack = deque()
        for p in s:
            if p in mem:
                stack.append(p)
            elif len(stack) != 0 and mem.get(stack[-1]) == p:
                    stack.pop()
            else:
                return False
        return len(stack) == 0