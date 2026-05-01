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
    arr = [0] + numbers()
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        cur = i
        visited = set()

        while cur not in visited:
            visited.add(cur)
            cur = arr[cur]
        ans[i] = len(visited)
    print(*ans[1:])
        

    return


for _ in range(test_cases()):
    solve()