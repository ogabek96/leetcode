from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        walks = [(1,1), (0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
        queue = deque([(0,0,1)])
        m = len(grid[0]) - 1
        n = len(grid) - 1
        res = []
        while len(queue) > 0:
            x, y, s = queue.popleft()
            if x == m and y == n:
                res.append(s)
            for w in walks:
                x1 = x + w[0]
                y1 = y + w[1]
                if x1 >= 0 and y1 >= 0 and x1 <= m and y1 <= n and grid[x1][y1] != 1:
                    grid[x1][y1] = 1
                    queue.append((x1, y1, s + 1))
                    print(x1, y1)
        if len(res) == 0:
            return -1
        return min(res)