class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        results = [0] * len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while len(stack) > 0 and T[i] >= stack[-1][1]:
                stack.pop()
            if len(stack) > 0 and T[i] < stack[-1][1]:
                results[i] = stack[-1][0] - i
            stack.append((i, T[i]))
        return results