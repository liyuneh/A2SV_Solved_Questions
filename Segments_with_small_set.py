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

    count = 0
    freq = defaultdict(int)

    l = 0
    for r in range(n):
        freq[arr[r]] += 1
        while len(freq) > k:
            freq[arr[l]] -= 1
            if not freq[arr[l]]:
                del freq[arr[l]]
            l += 1
        count += ( r- l + 1)

    print(count)
        
    return


for _ in range(test_cases(1)):
    solve()
