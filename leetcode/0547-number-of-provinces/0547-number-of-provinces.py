class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        arr = UnionFind(n)
        nums = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] and arr.find(i) != arr.find(j):
                    nums -= 1
                    arr.union(i, j)
        return nums
