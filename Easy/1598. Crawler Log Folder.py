class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = deque()
        for l in logs:
            if l == '../':
                if len(stack) > 0:
                    stack.pop()
            elif l != './':
                stack.append(l)
        return len(stack)