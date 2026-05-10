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
    input()
    n ,k = numbers()
    if n == 1:
        print(1 if k == 0 else 0)
        return 
    g = [[] for _ in range(n + 1)]
    indegree = [0] * (n +1)
    for _ in range(n - 1):
        u, v = numbers()
        g[u].append(v)
        g[v].append(u)
        indegree[u] += 1
        indegree[v] += 1
    q = deque()
    for c in range(1, n + 1):
        if indegree[c] == 1:
            q.append(c)
    ans = n
    while q and  k > 0:
        ans -= len(q)
        for _ in range(len(q)):
            node = q.popleft()
            for ne in g[node]:
                indegree[ne] -= 1
                if indegree[ne] == 1:
                    q.append(ne)
        k -= 1
    print(ans)

    return


for _ in range(test_cases()):
    solve()