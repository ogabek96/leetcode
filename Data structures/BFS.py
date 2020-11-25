from collections import deque
def bfs(graph, startvalue, searchvalue):
  queue = deque()
  visited = set([startvalue])
  queue += graph[startvalue]
  while len(queue) > 0:
    value = queue.popleft()
    if value not in visited:
      if value == searchvalue:
        return True
      else:
        queue += graph[value]
        visited.add(value)
  return False

# Test
graph = {
  'a': ['b', 'c'],
  'c': ['d'],
  'b': [],
  'd': []
}
print(bfs(graph, 'a', 'd')) # Should return True
print(bfs(graph, 'a', 'e')) # Should return False