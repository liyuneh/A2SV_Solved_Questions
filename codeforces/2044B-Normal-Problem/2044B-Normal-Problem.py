n = int(input())
for _ in range(n):
    s = input()
    s = s[::-1]
    k = ""
    for i in range(len(s)):
        if s[i] == 'q':
            k += 'p'
        elif s[i] == 'p':
            k += 'q'
        else:
            k +='w'
            
    print(k)