t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b > a:
        print(1)
    elif b == a:
        print(2)
    else:
        ans = float('inf')
        for i in range(0 , 30):
            c = b + i
            if c == 1:
                continue
            d = a
            count = 0
            while d > 0:
                d = d // c
                count += 1
            ans = min(ans, count + i)
        print(ans)