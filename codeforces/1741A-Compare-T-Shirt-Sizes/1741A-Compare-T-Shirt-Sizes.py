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
    a, b = words()
    freq = {"L":2, "S":0, "M":1}
    def sumsS(a):
        count = 0
        for ch in a:
            if ch in freq:
                count += freq[ch]
            else:
                count -= 1
        return count
    def sums(a):
        count = 0
        for ch in a:
            if ch in freq:
                count += freq[ch]
            else:
                count += 1
        return count
    if a == b:
        print("=")
        return 
    l , r = a[-1], b [-1]
    if l == r:
        if l == "S":
            print(">" if sumsS(a) > sumsS(b) else "<")
        elif l == "L":
            print(">" if sums(a) > sums(b) else "<")
        return 
    if l != r:
        if freq[l] > freq[r]:
            print(">")
        else:
            print("<")
        return 
    return


for _ in range(test_cases()):
    solve()