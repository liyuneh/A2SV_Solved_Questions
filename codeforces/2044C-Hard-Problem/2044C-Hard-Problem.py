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
    m,a,b,c = numbers()
    keri1 = 0 if a > m else m - a
    keri2 = 0 if b > m else m - b
    first = a if a < m else m
    second = b if b < m else m
    count = first + second
    # print(count)
    if keri1 > 0 and c >= keri1:
        count += keri1
        c -= keri1
    elif keri1 > 0 and c < keri1:
        count += c
        c = 0
    if keri2 > 0 and c >= keri2 :
        count += keri2
        c -= keri2
    elif keri2 > 0 and c < keri2:
        count += c
        c = 0
    

    print(count)
    return

for _ in range(test_cases()):
    solve()