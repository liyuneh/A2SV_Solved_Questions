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
    visited = [0] * ( n + 1)

    for i in range(1, n + 1):
        if visited[i]:
            continue
        cur = i
        path = []
        while  not visited[cur]:
            visited[cur] = 1
            path.append(cur)
            cur = arr[cur]
        if cur in path:
            start = path.index(cur)
            size = len(path) - start

            for j in range(start, len(path)):
                ans[path[j]] = size
        for node in path:
            if ans[node] == 0 :
                ans[node] = ans[arr[node]]
    print(*ans[1:])  
    return


for _ in range(test_cases()):
    solve()