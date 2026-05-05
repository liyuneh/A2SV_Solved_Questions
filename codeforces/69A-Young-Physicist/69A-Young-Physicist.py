n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
sum1, sum2, sum3 = 0, 0, 0
for i in range(n):
    for j in range(3):
        sum1 += matrix[i][0]
        sum2 += matrix [i][1]
        sum3 += matrix [i][2]
if sum1 == 0 and sum2 == 0 and sum3 == 0:
    print("YES")
else:
    print("NO")