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
    h , w = numbers()
    ans = []
    hor = [[0]  *(w + 1) for _ in range(h+1)]
    ver = [[0] * (w + 1) for _ in range(h + 1)]

    for _ in range(h):
        ans.append(word())
    for i in range(h):
        for j in range(w-1):
            if ans[i][j] == "." and ans[i][j+1] == ".":
                hor[i+1][j+1] = 1
    for i in range(h-1):
        for j in range(w):
            if ans[i][j] == "." and ans[i+1][j] == ".":
                ver[i+1][j+1] = 1
    
    for i in range(1, h + 1):
        for j in range(1, w+ 1):
            hor[i][j] += hor[i-1][j] + hor[i][j-1] - hor[i-1][j-1]
            ver[i][j] += ver[i-1][j] + ver[i][j-1] - ver[i-1][j-1]
    def get (ps, r1,c1,r2,c2):
        if r1 > r2 or c1 > c2:
            return 0
        return ps[r2][c2] - ps[r1-1][c2] - ps[r2][c1-1] + ps[r1-1][c1-1]

    q = number()
    for _ in range(q):
        r1,c1,r2,c2 = numbers()
        hori = get(hor,r1,c1,r2,c2 - 1)
        veri = get(ver,r1,c1,r2 - 1,c2)
        print(hori + veri)
    



    return


for _ in range(test_cases(1)):
    solve()
