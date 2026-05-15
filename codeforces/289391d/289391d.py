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
    n ,m = numbers()
    parent = list(range(n))
    rank = [0] * (n)
    def find(x):
        arr = []
        while rank[x] !=  0:
            arr.append(x)  
            x = parent[x]
        run = 0
        for i in range(len(arr) - 1, -1, -1):
            run += rank[arr[i]]
            rank[arr[i]] = run
            parent[arr[i]] = x

        return 0 if not arr else rank[arr[0]]

    def union(x, y):
        parent[x] = y
        rank[x] += 1
        return True
    for _ in range(m):
        nums = numbers()
        if nums[0] == 1:
            union(nums[1] - 1, nums[2] - 1)
        else:
            print(find(nums[1] - 1))

    
    return


for _ in range(test_cases(1)):
    solve()