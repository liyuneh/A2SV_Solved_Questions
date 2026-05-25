import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp


def solve():
    n = number()
    prev = sum([i + 1 if i % 2 == 1 else 0 for i in range(1,n )])
    res = 2
    for i in range(2, n + 1):
        num = i
        j = 1
        s = 0
        while j * num <= n:
            s += (j * num)
            j += 1
        if s >= prev:
            prev = s
            res = num
    print(res)


    return

for _ in range(test_cases()):
    solve()