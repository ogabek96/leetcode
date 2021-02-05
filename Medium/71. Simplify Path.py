class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        for p in paths:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            elif p != "" and p != '.':
                stack.append(p)
        return "/" + "/".join(stack)