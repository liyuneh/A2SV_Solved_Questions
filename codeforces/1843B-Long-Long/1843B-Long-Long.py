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
    arr = numbers()
    if n == 1:
        if arr[0] < 0:
            print(abs(arr[0]), 1)
        else:
            print(arr[0], 0)
        return 
    total = sum(i if i > 0 else -i for i in arr)
    ans = []
    for i in range(n):
        if arr[i] < 0:
            ans.append(-1)
        elif arr[i] > 0:
            ans.append(1)
    if not ans:
        print(arr[0], 0)
        return 
    count = 0
    l = 0
    for i in range(len(ans) - 1):
        if ans[i] < 0 and ans[i + 1] > 0:
            count += 1
            l = i + 1
    if   ans[-1] < 0 :
        count += 1
    
    print(total , count)
    return


for _ in range(test_cases()):
    solve()