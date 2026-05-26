n = int(input())
for i in range(0 , n):
    a,b = map(str, input().split())
    a_first = a[0]
    b_first = b[0]
    a = b_first + a[1:]
    b = a_first + b[1:]
    print(a + " " + b)