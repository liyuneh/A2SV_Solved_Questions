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
    g = [[] for _ in range(n + 1)]
    deg = [0] * ( n + 1)

    for i in range(n):
        g[i + 1].append(arr[i])
        deg[arr[i]] += 1
    ans = 0
    q = deque()
    dist = [1 ] * (n + 1)
    for i in range(1, n + 1):
        if deg[i] == 0:
            q.append(i)
    order, seen = [], set()
    while q:
        node = q.popleft()
        order.append(node)
        seen.add(node)
        for ne in g[node]:
            deg [ne] -= 1
            if deg[ne] == 0:
                q.append(ne)
    ans = 0
    for i in range(len(order)):
        node  = order[i]
        for ne in g[node]:
            dist[ne] += dist[node]
            if ne not in seen:
                ans = max(ans, dist[node])
    print(ans + 2)
    
    return


for _ in range(test_cases()):
    solve()