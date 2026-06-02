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

    if all(num < 0 for num in arr):
        print(0)
        print()
        return 
    
    if all(num > 0 for num in arr):
        print(1)
        print(n)
        return 
    ans = []
    prev = 1
    for i in range(n - 1, -1, -1):
        if arr[i] * prev > 0:
            ans.append(i + 1)
            prev = - prev
    print(len(ans))
    print(*ans)
        
    return


for _ in range(test_cases()):
    solve()