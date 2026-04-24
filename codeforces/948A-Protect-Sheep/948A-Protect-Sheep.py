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
    n, m = numbers()
    graph = []
    for i in range(n):
        ans = []
        s = word()
        for j in range(m):
            ans.append(s[j])
        graph.append(ans)
    dxn = [(-1, 0), (0 , 1), (0, -1), (1, 0)]

    def can(i, j):
        count = 0
        for dx, dy in dxn:
            new , new_y= i + dx , j + dy
            if new >= 0 and new < n and new_y >= 0 and  new_y < m:
                if graph[new][new_y] == "W":
                    count += 1

        return count == 0
    # print(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "S":
                if not can(i, j):
                    print("No")
                    return 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == ".":
                graph[i][j] = "D"
    
    print("Yes")
    for i in range(n):
        x = "".join(graph[i])
        print(x)
                


    return


for _ in range(test_cases(1)):
    solve()