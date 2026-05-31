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
    arr = sorted(numbers())
    mx = float('inf')
    for i in range(n):
        a, b = 0, 0
        for j in range(i, n):
            if arr[j] > arr[i]:
                a += 1
        for j in range(i, -1, -1):
            if arr[j] < arr[i]:
                b += 1
        mx = min(mx, max(a, b))
    print(mx)
    return


for _ in range(test_cases()):
    solve()