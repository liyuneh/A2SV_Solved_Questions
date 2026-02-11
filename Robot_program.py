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
    n , x , k = numbers()
    s = word()
    i = 0
    prev = 0
    while i < len(s):
        if s[i] == "L":
            x -= 1
            if x == 0:
                prev = i
                break
        elif s[i] == "R":
            x += 1
            if x == 0:
                prev = i
                break
        i += 1
    if x != 0:
        print(0)
        return 
    j = 0
    while j  < len(s):
        if s[j] == "L":
            x -= 1
            if x == 0:
                break
        else:
            x += 1
            if x == 0:
                break
        j += 1
    if x != 0:
        print(1)
        return 
    print(1 + (k - prev - 1) // (j + 1))
    
    
    
    return

for _ in range(test_cases()):
    solve()
