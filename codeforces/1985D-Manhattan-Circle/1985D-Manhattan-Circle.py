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
    grid = [list(word()) for _ in range(n)]
    s , d = [], []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                s.append(i + j)
                d.append(i - j)
    mn_s, mx_s = min(s), max(s)
    mn_d, mx_d = min(d), max(d)
    sd = (mn_s + mx_s) // 2
    ds = (mn_d + mx_d) // 2
    a = (sd + ds) // 2
    b = a - ds
    print(a + 1, b + 1)

    
    
    return


for _ in range(test_cases()):
    solve()