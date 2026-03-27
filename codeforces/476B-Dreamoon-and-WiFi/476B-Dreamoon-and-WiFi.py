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
    s1 = word()
    s2 = word()
    x = 0
    for i in range(len(s1)):
        if s1[i] == "+":
            x += 1
        else:
            x -= 1
    n = len(s1)
    res = 0
    total = 0
    def dfs(i, pos):
        nonlocal total , res
        if i == n:
            total += 1
            if x == pos:
                res += 1
            return 
        if s2[i] == '+':
            dfs(i+1, pos + 1)
        elif s2[i] == "-":
            dfs(i + 1, pos - 1)
        else:
            dfs(i + 1, pos + 1)
            dfs(i + 1, pos - 1)
    dfs(0 ,0)
    print(f"{res / total: .12f}")
            
    
    return

for _ in range(test_cases(1)):
    solve()