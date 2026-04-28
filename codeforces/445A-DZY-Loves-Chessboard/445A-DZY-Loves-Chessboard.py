import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random
sys.setrecursionlimit(10 ** 7)

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    graph = []
    n , m = numbers()
    for _ in range(n):
        graph.append(list(word()))

    dxn = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def dfs(i,j,  color):
        graph[i][j] = color
        next_col = "W" if color == "B" else "B"

        for dx, dy in dxn:
            ni, nj = i + dx, j + dy
            if 0<= ni < n and 0 <= nj < m:
                if graph[ni][nj] == ".":
                    dfs(ni, nj, next_col)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == ".":
                dfs(i, j , "B")

    for i in range(n):
        print("".join(graph[i]))

    

    return


for _ in range(test_cases(1)):
    solve()