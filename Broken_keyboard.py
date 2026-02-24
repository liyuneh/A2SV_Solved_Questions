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
    s = word()
    if len(s) == 1:
        print(s)
        return 
    ans = []
    l , r = 0 , 1
    while r < len(s):
        if s[l] == s[r]:
            l += 2
            r += 2
            
        else:
            if s[l] not in ans:
                ans.append(s[l])
            l += 1
            r += 1
    if l == len(s) - 1:
        if s[l] not in ans:
            ans.append(s[l])
    ans.sort()
    print("".join(ans))
    return


for _ in range(test_cases()):
    solve()
