import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random
# sys.setrecursionlimit(10 ** 7)

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    arr = numbers()
    def merge(l , r):
        if l == r:
            return 0, arr[l], arr[l]
        mid = (l + r)// 2
        left, lmin, lmax = merge(l, mid)
        right, rmin,rmax = merge(mid + 1, r)
        if left == - 1 or right == -1:
            return -1,0,0
        if lmax < rmin:
            return left + right , min(rmin, lmin), max(lmax, rmax)
        elif rmax < lmin:
            return left + right + 1, min(lmin, rmin) , max(rmax, lmax)
        else:
            return -1, 0 ,0
    count, _,_ = merge(0, n - 1)
    print(count) 
    return


for _ in range(test_cases()):
    solve()