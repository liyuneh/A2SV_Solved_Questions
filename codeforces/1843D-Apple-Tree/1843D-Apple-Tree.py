import sys, threading
sys.setrecursionlimit(10 ** 7)
threading.stack_size(1 << 27)
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u , v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    ans = [0] * (n + 1)
    def dfs(node, parent):
        count = 0
        for x in graph[node]:
            if x  == parent:
                continue
            count += 1
            dfs(x, node)
            ans[node] += ans[x]
        if count == 0:
            ans[node] = 1
    dfs(1, 0)
    q = int(input())

    for _ in range(q):
        x, y = map(int, input().split())
        print(ans[x] * ans[y])