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
    n , m = numbers()
    nums = numbers()
    l , r , Sum = 0 ,0 ,0 
    count = 0
    for r in range(n):
        Sum += nums[r]
        while Sum > m :
            Sum -= nums[l]
            l += 1
        count += (r - l + 1)
    print(count)
    return

for _ in range(test_cases(1)):
    solve()
