import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random
# sys.setrecursionlimit(10 ** 8)

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n , m = numbers()
    parent = list(range(n + 2))
    size = [1] * (n + 2)
    left = list(range(n + 2))
    lateralSize = [1] * (n + 2)
    def findLeft(x):
        while x != left[x]:
            left[x] = left[left[x]]
            x = left[left[x]]
        return x
    def unionh(x, y):
        x, y = findLeft(x), findLeft(y)
        union(x, y)
        x, y = min(x, y), max(x, y)
        left[y] = x
        lateralSize[x] += lateralSize[y]
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        a, b = find(x), find(y)
        if a == b:
            return 
        if size[a] < size[b]:
            a, b = b , a
        parent[b] = a
        size[a] += size[b]
        return True
    def merg(x, y):
        x, y = min(x, y), max(x, y)
        x = findLeft(x)
        while x + lateralSize[x] <= y:
            unionh(x, x + lateralSize[x])
            
    for _ in range(m):
        nums = numbers()
        if nums[0] == 1:
            union(nums[1], nums[2] )
        elif nums[0] == 2:
            merg(nums[1] , nums[2] )
        else:
            print(yes_no(find(nums[1] ) == find(nums[2])))
    return


for _ in range(test_cases(1)):
    solve()