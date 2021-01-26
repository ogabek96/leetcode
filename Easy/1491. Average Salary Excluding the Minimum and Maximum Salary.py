class Solution:
    def average(self, salary: List[int]) -> float:
        maxSal = max(salary)
        minSal = min(salary)
        return (sum(salary) - maxSal - minSal)/(len(salary) - 2)