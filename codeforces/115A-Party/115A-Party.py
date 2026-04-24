import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(10 ** 3)


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp


def solve():
    n = number()
    graph = [[] for _ in range(n + 1)]
    roots = []

    for i in range(1, n + 1):
        p = int(input())

        if p == -1:
            roots.append(i)
        else:
            graph[p].append(i)

    q = deque()

    for root in roots:
        q.append((root, 1))

    ans = 0

    while q:
        node, depth = q.popleft()
        ans = max(ans, depth)

        for child in graph[node]:
            q.append((child, depth + 1))
    print(ans)
    return

for _ in range(test_cases(1)):
    solve()