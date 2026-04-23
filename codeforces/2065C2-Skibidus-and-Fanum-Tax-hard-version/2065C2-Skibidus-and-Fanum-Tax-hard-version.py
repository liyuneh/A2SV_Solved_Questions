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
    n , m = numbers()
    a = numbers()
    b = numbers()
    b.sort()
    prev = -float('inf')
    flag = True
    for x in a:
        new = float("inf")
        if x >= prev:
            new = min(new, x)
        num = x + prev
        i = bisect_left(b, num)
        if i < m:
            k = b[i] - x
            if k >= prev:
                new = min(new, k)
        if new == float("inf"):
            flag = False
            break
        prev = new
    if flag:
        print("YES")
    else:
        print("NO")

    
    return


for _ in range(test_cases()):
    solve()