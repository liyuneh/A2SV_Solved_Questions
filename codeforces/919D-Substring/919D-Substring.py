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
    n, m = numbers()
    s = " " + word()
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for _ in range(m):
        u, v = numbers()
        graph[u].append(v)
        indegree[v] += 1
    
    q = deque()
    for c in range(1, n + 1):
        if indegree[c] == 0:
            q.append(c)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for ne in graph[node]:
            indegree[ne] -= 1
            if indegree[ne] == 0:
                q.append(ne)
    if len(order) != n:
        print(-1)
        return 
    dp = [[0] * 26 for _ in range(n + 1)]

    for u in order:
        c = ord(s[u ]) - 97
        dp[u][c] += 1

        for v in graph[u]:
            for ch in range(26):
                dp[v][ch] = max(dp[v][ch] , dp[u][ch])
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, max(dp[i]))
    print(ans)
    return


for _ in range(test_cases(1)):
    solve()