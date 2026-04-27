n = int(input())

for _ in range(n):
    s = int(input())
    ans = list(map(int, input().split()))

    count = 0
    max_count = 0
    for i in range(s):
        if ans[i] == 0:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)