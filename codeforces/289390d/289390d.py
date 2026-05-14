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
    n , m , k= numbers()
    parent = list(range(n))
    size = [1] * (n)

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return parent[x]
    def union(x, y):
        a, b = find(x), find(y)
        if a == b:
            return 
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        return True
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = numbers()
        g[u].append(v)
        g[v].append(u)
    tmp = [words() for _ in range(k)]
    ans = []
    for t, u, v in tmp[::-1]:
        if t == "ask":
            ans.append(find(int(u) - 1) == find(int(v) - 1))
        else:
            union(int(u) - 1, int(v) - 1)
    for cur in ans[::-1]:
        print(yes_no(cur))
    return


for _ in range(test_cases(1)):
    solve()