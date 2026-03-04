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
    n , k , q = numbers()
    freq = {}
    mx = 200003
    arr = [0] * mx
    for _ in range(n):
        a, b = numbers()
        arr[a] += 1
        arr[b + 1] -= 1
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    pre = 0
    for i in range(len(arr)):
        if arr[i] >= k:
            pre += 1
        arr[i] = pre
    for _ in range(q):
        l, r = numbers()
        print(arr[r] - arr[l - 1])
    return


for _ in range(test_cases(1)):
    solve()
