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

    if n == k :
        print(0)
        return 
    if k == 1:
        print(arr[-1] - arr[0])
        return 
    ans = []
    for i in range(1, len(arr)):
        ans.append(arr[i] - arr[i-1])
    ans.sort()
    print(sum(ans[:(n -k)]))
    
            
        


    return


for _ in range(test_cases(1)):
    solve()
