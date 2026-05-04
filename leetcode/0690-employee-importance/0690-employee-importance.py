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
        freq = {emp.id: emp for emp in employees}
        def dfs(id):
            emp = freq[id]
            total = emp.importance
            for ne in emp.subordinates:
                total += dfs(ne)
            return total 

        return dfs(id)