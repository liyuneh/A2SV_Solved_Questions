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
    s = list(word())
    ans = []
    count = 1
    l = 0
    for i in range(1, n):
        if s[i] != s[i-1]:
            ans.append(count)
            count = 1
            l = i
        else:
            count += 1
    if l != i:
        ans.append(count)
    if all(m % 2 == 0 for m in ans):
        print(0)
        return
    cnt = 0
    prev = 0
    # print(ans)
    for i in range(len(ans)):
        if (ans[i] + prev)  % 2 != 0:
            cnt += 1
        prev = (ans[i] + prev) % 2
        
    print(cnt)
    
        
    return


for _ in range(test_cases()):
    solve()