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
    arr1 = numbers()
    arr2 = numbers()
    count = 0
    a = Counter(arr1)
    b = Counter(arr2)
    seen = list(set(arr1))
    for i in range(len(seen)):
        if seen[i] in b:
            count += (a[seen[i]] * b[seen[i]])
    # l , r = 0 , 0 
    # while l < n and r < m:
    #     if arr1[l] == arr2[r]:
    #         val = arr1[l]
    #         count1 = 0
    #         while l < n and arr1[l] == val:
    #             count1 += 1
    #             l += 1
    #         count2 = 0
    #         while  r < m and arr2[r] == val:
    #             count2 += 1
    #             r += 1
    #         count += count1 * count2
    #     elif arr1[l]  <  arr2[r]:
    #         l += 1
    #     else:
    #         r += 1
    print(count)
    return

for _ in range(test_cases(1)):
    solve()
