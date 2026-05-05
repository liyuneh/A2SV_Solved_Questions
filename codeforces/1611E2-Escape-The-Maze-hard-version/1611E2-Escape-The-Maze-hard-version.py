from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    line = input().strip()
    while line == "":
        line = input().strip()
    n, k = map(int, line.split())
    nums = list(map(int, input().split()))
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    q = deque()

    for f in nums:
        dist[f] = 0
        q.append(f)

    while q:
        node = q.popleft()
        for ne in graph[node]:
            if dist[ne] == -1:
                dist[ne] = dist[node] + 1
                q.append(ne)
    
    distance = [-1] * (n + 1)
    qf = deque([1])
    distance[1] = 0

    while qf:
        node = qf.popleft()
        for ne in graph[node]:
            if distance[ne] == -1:
                distance[ne] = distance[node] + 1
                qf.append(ne)
    ans = 0
    visited = [False] * ( n + 1)
    qb = deque([1])
    visited[1] = True
    while qb:
        node = qb.popleft()
        if dist[node] <= distance[node]:
            ans += 1
            continue
        for ne in graph[node]:
            if not visited[ne]:
                visited[ne] = True
                qb.append(ne)
    
    ok = False
    for i in range(2, n + 1):
        if len(graph[i]) == 1:
            if distance[i] < dist[i]:
                ok = True
                break
    if ok:
        print(-1)
    else:
        print(ans)