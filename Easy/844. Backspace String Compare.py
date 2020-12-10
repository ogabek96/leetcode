class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackone = deque()
        stacktwo = deque()
        for ch in S:
            if len(stackone) > 0 and ch == '#':
                stackone.pop()
            elif ch != '#':
                stackone.append(ch)
        for ch in T:
            if len(stacktwo) > 0 and ch == '#':
                stacktwo.pop()
            elif ch != '#':
                stacktwo.append(ch)
        return "".join(stackone) == "".join(stacktwo)