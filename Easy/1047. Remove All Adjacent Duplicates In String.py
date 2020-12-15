class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if len(stack) == 0:
                stack.append(ch)
            elif stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)