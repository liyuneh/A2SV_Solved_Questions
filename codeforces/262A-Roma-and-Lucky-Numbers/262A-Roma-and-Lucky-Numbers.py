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
    n , k = numbers()
    arr = numbers()
    ans = 0
    for i in range(n):
        x = str(arr[i])
        count = 0
        for j in range(len(x)):
            if x[j] in ['4', '7']:
                count += 1
        if count > k:
            ans += 1
    print( n - ans)

    return


for _ in range(test_cases(1)):
    solve()