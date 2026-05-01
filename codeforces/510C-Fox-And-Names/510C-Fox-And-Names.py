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
    ans = []
    for _ in range(n):
        s = word()
        ans.append(s)
    graph = defaultdict(list)
    indegree = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for i in range(n -1):
        s1, s2 = ans[i], ans[i + 1]
        if s1.startswith(s2) and len(s1) > len(s2):
            print("Impossible")
            return 

    for i in range(n - 1):
        s1, s2 = ans[i], ans[i + 1]
        for j in range(min(len(s1), len(s2))):
            if s1[j] != s2[j]:
                graph[s1[j]].append(s2[j])
                indegree[s2[j]] += 1
                break
    q = deque()

    for c in indegree:
        if indegree[c] == 0:
            q.append(c)
    res = []
    while q:
        node = q.popleft()
        res.append(node)

        for ne in graph[node]:
            indegree[ne] -= 1
            if indegree[ne] == 0:
                q.append(ne)
    if len(res) == 26:
        print("".join(res))
    else:
        print("Impossible")


    return


for _ in range(test_cases(1)):
    solve()