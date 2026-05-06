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
    graph = [ [] for _ in range(n + 1)]
    for _ in range(m):
        u, v = numbers()
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * ( n + 1)
    total = 0
    def dfs(node):
        stack = [node]
        v, e = [], 0
        while stack:
            cur= stack.pop()
            if visited[cur]:
                continue
            visited[cur] = True
            v.append(cur)
            e += len(graph[cur])
            for ne in graph[cur]:
                if not visited[ne]:
                    stack.append(ne)
        return v, e // 2
    comp = 0
    for i in range(1, n + 1):
        if not visited[i]:
            ok = True
            nodes , edges = dfs(i)
            if len(nodes) == edges:
                for u in nodes:
                    if len(graph[u]) != 2:
                        ok = False
                        break
                if ok:
                    total += 1
    # print(total )


    print(total )

    return


for _ in range(test_cases(1)):
    solve()