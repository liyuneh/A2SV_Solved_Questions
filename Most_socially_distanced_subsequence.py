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
    arr = numbers()

    ans = []
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            ans.append(-1)
        else:
            ans.append(1)
    if len(set(ans)) == 1:
        print(2)
        print(*[arr[0], arr[-1]])
    else:
        value = [arr[0]]
        past = ans[0]
        ans.append(-ans[-1])
        # print(ans)
        for i in range(len(ans)):
            if ans[i] != past:
                value.append(arr[i])
                past = -past
        
        print(len(value))
        print(*value)


        
    return


for _ in range(test_cases()):
    solve()
