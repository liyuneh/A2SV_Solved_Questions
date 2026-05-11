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
    # deg = [0] * ( n + 1)
    ans = 0
    for _ in range(m):
        u, v = numbers()
        if u == v:
            continue
        ans += 1
        g[u].append(v)
        g[v].append(u)
    vis = [0] * (n + 1)
    for i in range(1,n + 1):
        if vis[i] or not g[i]:
            continue

        q = deque([i])
        vis[i] = 1

        node, edges = 0, 0
        while q:
            u = q.popleft()

            node +=  1
            edges += (len(g[u]))
            for ne in g[u]:
                if not vis[ne]:
                    vis[ne] = 1
                    q.append(ne)
        edges //= 2
        if edges == node:
            ans += 1
    print(ans)

    return


for _ in range(test_cases()):
    solve()