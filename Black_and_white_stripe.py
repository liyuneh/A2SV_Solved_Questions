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
    n , k = numbers()
    s = word()
    l= 0 
    count = 0
    res = float('inf')
    for r in range(len(s)):
        count += 1 if s[r] == 'W' else 0
        if r - l + 1 == k:
            res = min(res, count)
            count -= 1 if s[l] == 'W' else 0
            l += 1
    print(res )
    return

for _ in range(test_cases()):
    solve()
