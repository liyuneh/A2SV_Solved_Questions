for _ in range(int(input())):
    n = int(input())
    a = list(input().strip())
    b = input()
    ans = 0
    for i in range(n):
        if b [i] == "1":
            if i > 0 and a[i-1] == "1":
                ans += 1
                a[i-1] = "0"
            elif a[i] == "0":
                ans += 1
            elif i < n - 1 and a[i + 1] == "1":
                ans += 1
                a[i + 1] ="0"
    print(ans)