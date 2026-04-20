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
    if len(set(arr)) == 1:
        print(1)
        return 
    if len(arr) == 2:
        print(2)
        return 
    res = [arr[0]]
    for ch in arr[1:]:
        if ch != res[-1]:
            res.append(ch)
    count = len(res)
    for i in range(len(res) - 2):
        count -= (res[i] < res[i + 1] and res[i + 1] < res[i+ 2])
        count -= (res[i] > res[i + 1] and res[i + 1] > res[i + 2])
    print(count)

    return


for _ in range(test_cases()):
    solve()