t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    found = False
    for i in range(n):
        if arr[arr[i] - 1] == i + 1:
            found = True
            break
    if found:
        print(2)
    else:
        print(3)