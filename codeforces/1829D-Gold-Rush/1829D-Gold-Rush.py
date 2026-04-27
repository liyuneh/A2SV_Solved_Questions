import sys
sys.setrecursionlimit(10 ** 7)
t = int(input())
def check(n, m, dp):
    if n == m :
        return True
    if n <= 1 or n % 3 != 0:
        return False
    if n in dp:
        return dp[n]
    dp[n] = check(2 * (n // 3), m, dp) or check( n // 3, m, dp)
    return dp[n]

for _ in range(t):
    n ,m = map(int, input().split())
    dp = {}
    if check(n, m , dp):
        print("YES")
    else:
        print("NO")