def Mx(arr):
        seen = set(arr)
        for i in range(len(arr) + 1):
            if i not in seen:
                return i

    ans = []
    another = [i for i in range(n)]

    if arr == another:
        print(0)
        print()
        continue

    while arr != another:
        x = Mx(arr)
        if x < n:
            arr[x] = x
            ans.append(x + 1)
        else:
            for i in range(n):
                if arr[i] != i:
                    arr[i] = x
                    ans.append(i + 1)
                    break

    print(len(ans))
    print(*ans)