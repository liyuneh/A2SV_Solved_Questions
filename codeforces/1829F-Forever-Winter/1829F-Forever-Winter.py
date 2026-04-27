from collections import defaultdict
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    ans = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        ans[u] += 1
        ans[v] += 1
    freq = defaultdict(int)
    for i in range(1, n + 1):
        freq[ans[i]] += 1
    # print(ans)
    val = sorted(freq.values())
    # print(val)
    if len(val) == 3:
        x = val[1]
        y = val[2] // val[1]
        print(x, y)
    else:
        x = val[0] - 1
        y = val[1] // (val[0] - 1)
        print(x, y)