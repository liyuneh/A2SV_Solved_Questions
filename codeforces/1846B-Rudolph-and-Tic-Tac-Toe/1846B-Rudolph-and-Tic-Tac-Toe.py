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
    grid = [list(word()) for _ in range(3)]
    ans = [list(new) for new in zip(*grid)]
    # for i in range(3):
    #     print(*ans[i])
    # print()

    for i in range(3):
        if len(set(grid[i])) == 1 and grid[i][0] != ".":
            print(grid[i][0])
            return 
    diagonal = []
    diagonal1 = []
    for i in range(3):
        diagonal.append(grid[i][i])
    if len(set(diagonal)) == 1 and diagonal[0] != ".":
        print(diagonal[0])
        return 
    
    diagonal1.append(grid[0][2]), diagonal1.append(grid[1][1]), diagonal1.append(grid[2][0])
    if len(set(diagonal1)) == 1 and diagonal1[0] != ".":
        print(diagonal1[0])
        return 
    for i in range(3):
        if len(set(ans[i])) == 1 and ans[i][0] != ".":
            print(ans[i][0])
            return
    print("DRAW")

    return


for _ in range(test_cases()):
    solve()