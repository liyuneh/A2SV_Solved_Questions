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
    n = number()
    s = word()
    if "aa" in s:
        print(2)
        return 
    if "aba" in s or "aca" in s:
        print(3)
        return 
    if "abca" in s or "acba" in s:
        print(4)
        return 
    if "abbacca" in s or "accabba" in s:
        print(7)
        return 
    print(-1)
    
    return

for _ in range(test_cases()):
    solve()
