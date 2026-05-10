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
    n ,m = numbers()
    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        u, v = numbers()
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    q = deque()
    for c in range(1, n + 1):
        if degree[c] == 1:
            q.append(c)
    # print(q)
    ans = 0
    while q :
        ans += 1
        now = list(q)
        q.clear()

        for node in now:
            degree[node] = 0
        for node in now:
            for ne in g[node]:
                if degree[ne] > 0:
                    degree[ne] -= 1
        for i in range(1, n + 1):
            if degree[i] == 1:
                q.append(i)
    print(ans)

    return


for _ in range(test_cases(1)):
    solve()