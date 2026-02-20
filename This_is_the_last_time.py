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
    ans = []
    for _ in range(n):
        l , r, re = numbers()
        ans.append([l,r,re])
    ans.sort(key = lambda x:(x[0], x[1],x[2]))
    # print(ans)
    mx = 0
    for l , r, re in ans:
        if l <= k :
            k = max(k , re)
        mx = max(mx, k)
    print(mx)
    

        
    # print(mx)
    return


for _ in range(test_cases()):
    solve()
