def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

k = int(input().strip())
count = 0
x = 19  
while True:
    if sum_digits(x) == 10:
        count += 1
        if count == k:
            print(x)
            break
    x += 9