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
    n ,k = numbers()
    arr = numbers()
    arr.sort()
    # print(arr)
    ans = 0
    total = sum(arr)
    for i in range(n):
        total -= arr[i]
        if i + 1 == (k * 2):
            break
    l = i
    ans = total
    for i in range(n - 1, max(0, n - k) - 1, -1):
        total += arr[l]
        total += arr[l - 1]
        l -= 2
        total -= arr[i]
        ans = max(ans, total)
    print(ans)
    return

for _ in range(test_cases()):
    solve()

    # 10 11 12 13 15 22