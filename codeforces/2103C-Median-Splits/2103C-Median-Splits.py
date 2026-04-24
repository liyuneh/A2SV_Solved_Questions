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
    arr = numbers()

    for i in range(len(arr)):
        arr[i] = 1 if arr[i] <= k else -1
    def pref_mid (n , arr):
        suff = [0] * (n + 1)
        mn = [0] * (n + 1)
        suff[n] = mn[n] = arr[n-1]
        for i in range(n-2, -1, -1):
            suff[i + 1] = (suff[i + 2] + arr[i])
            mn [i + 1] = min(suff[i + 1], mn[i + 2])
        total = 0 
        for i in range(n - 2):
            total += arr[i]
            if total < 0 :
                continue
            if suff[i + 2] >= mn[i + 3]:
                return True
        return False
    a, b = n + 1, -1
    total = 0
    for i in range(n):
        total += arr[i]
        if total >= 0:
            a = i + 1
            break
    total = 0
    for i in range(n - 1, -1, -1):
        total += arr[i]
        if total >= 0:
            b = i + 1
            break
    if a + 1 < b:
        print("YES")
        return 
    if pref_mid(n, arr):
        print("YES")
        return 
    arr.reverse()
    if pref_mid(n , arr):
        print("YES")
        return 
    print("NO")
    
    
        
    return


for _ in range(test_cases()):
    solve()