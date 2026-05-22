import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify
from random import randint
Random = randint(100, 10**4)
Xor = lambda x:x ^ Random

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    ans = []
    for _ in range(n):
        ans.append(list(numbers()))
    if n == 1:
        print(max(ans[0]))
        return 
    dp = [[0] * 3 for _ in range(n)]
    for i in range(3):
        dp[0][i] = ans[0][i]
    for i in range(n):
        for j in range(3):
            if j == 0:
                dp[i][j] = ans[i][j] + max(dp[i-1][j + 1] , dp[i-1][j + 2])
            elif j == 1:
                dp[i][j] = ans[i][j] + max(dp[i-1][j - 1] , dp[i-1][j + 1])
            else:
                dp[i][j] = ans[i][j] +  max(dp[i-1][j - 1] , dp[i-1][j - 2])
    print(max(dp[n-1]))
    return


for _ in range(test_cases(1)):
    solve()