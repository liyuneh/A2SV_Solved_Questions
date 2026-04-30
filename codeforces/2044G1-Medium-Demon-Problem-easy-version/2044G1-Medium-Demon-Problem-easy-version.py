import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    arr = numbers()
    indegree = [0] * (n +1)
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        graph[i + 1].append(arr[i])
        indegree[arr[i]] += 1
    q = deque()
    dist = [0] * (n + 1)

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    ans = 0
    while q:
        node = q.popleft()
        for ne in graph[node]:
            indegree [ne] -= 1
            dist[ne] = max(dist[ne], dist[node] + 1)
            if indegree[ne] == 0:
                q.append(ne)
    print(max(dist) + 2)
    return


for _ in range(test_cases()):
    solve()