import math
t = int(input())
for _ in range(t):
    n,m, k = map(int, input().split())
    b = math.ceil(n / m)
    c = n - b
    if k >= c:
        print("NO")
    else:
        print("YES")