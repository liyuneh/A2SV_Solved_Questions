import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random
from itertools import accumulate

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    a = numbers()
    m = number()
    b = numbers()

    red  = list(accumulate(a))
    blue = list(accumulate(b))

    r_mx = max(0 , max(red))
    b_mx = max(0 , max(blue))

    print(r_mx + b_mx)
    return


for _ in range(test_cases()):
    solve()
