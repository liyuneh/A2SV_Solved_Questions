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
    s = word()
    p = word()

    pref1, pref2 = [], []
    countone, countzero = 0 , 0 
    for i in range(len(s)):
        if s[i] == "1":
            countone += 1
        else:
            countzero += 1
        pref1.append(countone)
        pref2.append(countzero)
    flipped = 0
    possible = True
    for i in range(len(s) - 1, - 1, -1):
        if flipped ^ int(s[i]) != int(p[i]):
            if pref1[i] == pref2[i]:
                flipped ^= 1
            else:
                print("NO")
                possible = False
                return 
    print("YES" if possible else "NO")
        
    return


for _ in range(test_cases()):
    solve()
