"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        myDict = {}
        for emp in employees:
            myDict[emp.id] = emp
        result = 0
        queue = deque()
        queue+= [id]
        visited = set()
        while len(queue) > 0:
            empId = queue.popleft()
            if empId not in visited:
                result+=myDict[empId].importance
                visited.add(empId)
                queue+=myDict[empId].subordinates
        return result