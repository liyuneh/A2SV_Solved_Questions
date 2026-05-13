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
    ans  = []
    seen = set()
    cur = 1
    for x in arr:
        if x not in seen:
            ans.append(x)
            seen.add(x)
        else:
            while cur in seen:
                cur += 1
            ans.append(cur)
            seen.add(cur)
    print(*ans)

    return


for _ in range(test_cases()):
    solve()