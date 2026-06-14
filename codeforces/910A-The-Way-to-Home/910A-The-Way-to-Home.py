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
    arr = word()
    ans = []
    if arr[0] == '0' or arr[-1] == '0':
        print(-1)
        return 
    for i in range(n):
        if arr[i] == '1':
            ans.append(i + 1)
    i , count = 0, 0
    while i < len(ans) - 1:
        nxt = i

        while nxt + 1 < len(ans) and ans[nxt + 1] - ans[i] <= k:
            nxt += 1
        if nxt == i:
            print(-1)
            return 
        count += 1
        i = nxt
    
    print(count)
       
    return


for _ in range(test_cases(1)):
    solve()