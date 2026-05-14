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
    n , m = numbers()
    a = numbers()
    b = numbers()
    ans = []
    for i , ch in enumerate(a):
        ans.append([ch, i])
    ans.sort()
    b.sort()
    for i in range(len(ans)):
        ans[i].append(b[i])
    
    ans.sort(key = lambda x:x[1])
    new = []
    for a, b, c in ans:
        new.append(c)
    print(*new)
    return


for _ in range(test_cases()):
    solve()