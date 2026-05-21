import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify

Random = randint(100, 10**4)
Xor = lambda x:x ^ Random

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n, m1, m2 = numbers()

    parent = list(range(n))
    size = [1] * n

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a, b = find(x), find(y)

        if a == b:
            return

        if size[a] < size[b]:
            a, b = b, a

        parent[b] = a
        size[a] += size[b]
    edges = []
    for _ in range(m1):
        u, v = numbers()
        edges.append((u-1, v - 1))

    parent2 = list(range(n))
    size2 = [1] * n

    def find2(x):
        if x != parent2[x]:
            parent2[x] = find2(parent2[x])
        return parent2[x]

    def union2(x, y):
        a, b = find2(x), find2(y)

        if a == b:
            return

        if size2[a] < size2[b]:
            a, b = b, a

        parent2[b] = a
        size2[a] += size2[b]


    for _ in range(m2):
        u, v = numbers()
        union(u- 1, v - 1)

    count = 0

    for u, v in edges:
        if find(u) != find(v):
            count += 1
        else:
            union2(u, v)

    groups = defaultdict(set)

    for i in range(n):
        groups[find(i)].add(find2(i))

    for x in groups.values():
        count += len(x) - 1

    print(count)

for _ in range(test_cases()):
    solve()