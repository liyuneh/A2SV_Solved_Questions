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
    graph = [[] for _ in range(n + 1)]
    edges = []
    degree = [0] * (n + 1)
    for _ in range(m):
        t, u , v = numbers()
        if t == 1:
            graph[u].append(v)
            degree[v] += 1
        edges.append((t,u, v))
    def topSort(graph, indegree):
        queue = deque()

        for node in range(1, n + 1):
            if not indegree[node]:
                queue.append(node)
        top_order = []
        while queue:
            cur = queue.popleft()
            top_order.append(cur)

            for neigh in graph[cur]:
                indegree[neigh] -= 1

                if not indegree[neigh]:
                    queue.append(neigh)
    
        return top_order
    nums = topSort(graph, degree)
    if len(nums) != n:
        print("NO")
        return 
    inorder = [0] * (n + 1)
    for i in range(n):
        inorder[nums[i]] = i
    print('YES')
    for t,u , v in edges:
        if t == 0:

            if inorder[u] < inorder[v]:
                print(u, v)
            else:
                print(v, u)
        else:
            print(u, v)
    return


for _ in range(test_cases()):
    solve()