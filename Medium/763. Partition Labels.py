class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if S == None or len(S) == 0:
            return None
        last_indexes = {}
        result = []
        for i in range(len(S)):
            last_indexes[S[i]] = i
        start = 0
        end = 0
        for i in range(len(S)):
            end = max(end, last_indexes[S[i]])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result