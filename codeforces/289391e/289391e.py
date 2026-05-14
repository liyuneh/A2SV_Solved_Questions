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
    parent = list(range(n))
    size = [1] * n
    def find(x):
        while x != parent[x]:
            x = parent[x]
        return parent[x]
    def union(x, y):
        a, b = find(x), find(y)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
        return True
    ans = [numbers() for _ in range(m)]
    ans.sort(key = lambda x:x[2])
    count = 0
    for u, v, w in ans:
        a , b = find(u - 1), find(v - 1)
        if a == b:
            continue
        else:
            union(u - 1, v - 1)
            count += w
    print(count)


    return


for _ in range(test_cases(1)):
    solve()