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
    s = word()
    arr = [chr(97 + i).upper() for i in range(k)]
    seen = set(s)
    # print(list(seen))
    if sorted(list(seen)) != arr:
        print(0)
        return 
    freq = defaultdict(int)
    for ch in s:
        freq[ch] += 1
    ans = float('inf')
    for key, val in freq.items():
        if key in arr:
            ans = min(ans, val)
    print(ans * k)
    
    return


for _ in range(test_cases(1)):
    solve()