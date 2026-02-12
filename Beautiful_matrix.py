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
    previ,prevj =  float('inf'), float('inf')
    for i in range(5):
        arr = numbers()
        if 1 in arr:
            x = arr.index(1)
            prevj = x
            previ = i
    print(abs(3 - prevj-1) + abs(3 - previ -1))
            

    return

for _ in range(test_cases(1)):
    solve()
