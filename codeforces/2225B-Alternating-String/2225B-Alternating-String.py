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
    s = word()
    if len(s) <= 2:
        print("YES")
        return 
    ans = []
    def check(arr):
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
        return True

    for i in range(len(s)):
        ans.append(1 if s[i] == "a" else -1)
    if check(ans):
        print("YES")
        return 
    prev = -1
    last = len(s)
    for i in range(1,len(ans)):
        if ans[i] == ans[i-1]:
            if prev == -1 :
                prev = i
            else:
                last = i
                break
    # print(ans)
    for i in range(prev, last):
        if ans[i] == 1:
            ans[i] = -1
        else:
            ans[i] = 1
    # print(ans)
    # print(prev, last)
    # print()
    if check(ans):
        print("YES")
        return 
    print("NO")
    return


for _ in range(test_cases()):
    solve()