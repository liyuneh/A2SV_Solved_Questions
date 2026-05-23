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
    seen = set()
    ans = []
    ans.append(1)
    seen.add(1)
    seen1 = set([1])
    i = 1
    while i < n:
        x = ans[-1]
        for j in range(1,2 * n + 1):
            if j not in seen1 and x + j  not in seen and j not in seen and x + j not in seen:
                ans.append(j)
                seen1.add(j)
                seen.add(x + j)
                break
        i += 1
    print(*ans)

    return


for _ in range(test_cases()):
    solve()