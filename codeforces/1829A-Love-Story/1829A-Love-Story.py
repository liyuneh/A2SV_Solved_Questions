n = int(input())
k = "codeforces"
for _ in range(n):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] != k[i]:
            count += 1
    print(count)