if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ans = [[i , j , k] for i in range(x+1) for j in range(y+1) for  k in range(z+1)]
    ans1 = []
    for i in range(len(ans)):
        if sum(ans[i]) != n:
            ans1.append(ans[i])
    print(ans1)
