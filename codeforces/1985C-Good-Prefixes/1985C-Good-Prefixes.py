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
    arr = numbers()
    prefs = arr[0]
    seen = arr[0]
    count = 0 if arr[0] != 0 else 1
    for i in range(1,n ):
        if arr[i] == prefs or prefs + arr[i] - seen == seen:
            count += 1
        prefs += arr[i]
        seen = max(seen, arr[i])
   
    print(count)
    return


for _ in range(test_cases()):
    solve()