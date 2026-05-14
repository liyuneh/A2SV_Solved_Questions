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
    parent = [i for i in range(n)]
    val = [0] * (n)
    size = [1] * (n)
    def find( x):
        while x != parent[x]:
            x = parent[x]
        return parent[x]
    
    def union(x, y):
        a , b = find(x), find(y)
        if a != b:
            if size[a] < size[b]:
                a, b = b , a
            elif size[a] == size[b]:
                size[a] += 1
            parent[b] = a

            size[a] += size[b]
            val[b] -= val[a]
        return True
    
    def add( x, value):
        a = find(x)
        val[a] += value

    def get(x):
        ans = val[x]
        if parent[x] == x:
            return ans
        ans += get(parent[x])
        return ans
    
    for _ in range(m):
        parts = words()
        if parts[0] == "add":
            add(int(parts[1]) - 1, int(parts[2]))
        elif parts[0] == "join":
            union(int(parts[1]) - 1, int(parts[2]) - 1 )
        else:
            s = get(int(parts[1]) - 1)
            print(s)
    # print()
    # print(rank)
    # print(dsu.parent, dsu.rank)
    return


for _ in range(test_cases(1)):
    solve()