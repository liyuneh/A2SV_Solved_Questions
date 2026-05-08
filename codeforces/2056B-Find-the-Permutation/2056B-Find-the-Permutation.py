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
    g = [word() for _ in range(n)]
    p = list(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            bad = False
            x, y = p[i], p[j]
            if g[x][y] == "1":
                if x > y:
                    bad = True
            else:
                if x < y :
                    bad = True
            if bad:
                p[i], p[j] = p[j], p[i]
    print(*[x + 1 for x in p])


    return


for _ in range(test_cases()):
    solve()