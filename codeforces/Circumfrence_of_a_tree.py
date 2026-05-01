import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Ran

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    if n <= 1:
        print(0)
        return 
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = numbers()
        tree[u].append(v)
        tree[v].append(u)
    def bfs(start):
        dist = [-1] * (n +1)
        q = deque([start])
        dist[start] = 0
        far = start
        while q:
            node = q.popleft()
            for ne in tree[node]:
                if dist[ne] == -1:
                    dist[ne] = max(dist[ne], dist[node] + 1)
                    q.append(ne)
                    if dist[ne] > dist[far]:
                        far = ne
        return far, dist
    c, _ = bfs(1)

    _, nums1 = bfs(c)
    print(max(nums1) * 3)

    

    
    
    return


for _ in range(test_cases(1)):
    solve()
