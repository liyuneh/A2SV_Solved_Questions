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
    a = numbers()
    b = numbers()
    ans = []
    for i in range(n):
        if a[i] > b[i]:
            ans.append([3,i+1])
            a[i], b[i] = b[i],a[i]
    for i in range(len(a)):
        for j in range(0,len(a) -i- 1):
            if a[j] > a[j+1]:
                ans.append([1,j+1])
                a[j],a[j+1] = a[j+1],a[j]
    for i in range(len(b)):
        for j in range(0, len(b)- i - 1):
            if b[j] > b[j+1]:
                ans.append([2,j+1])
                b[j],b[j+1] = b[j+1],b[j]
    print(len(ans))
    for an in ans:
        print(*an)
  
    
    return


for _ in range(test_cases()):
    solve()
