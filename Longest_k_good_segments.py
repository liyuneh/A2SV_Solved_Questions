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
    n , k = numbers()
    arr = numbers()

    seen = set()
    l = 0
    ans = []
    freq = defaultdict(int)
    for r in range(len(arr)):
        freq[arr[r]] += 1
        if len(freq) == k:
            ans.append((r - l , l + 1, r + 1))
        while len(freq) > k:
            freq[arr[l]] -= 1
            if not freq[arr[l]]:
                del freq[arr[l]]
            l += 1
    ans.sort(key = lambda x:-x[0])
    # print(ans)
    if ans:
        print(ans[0][1], ans[0][2])
    else:
        print(1,len(arr))
    return


for _ in range(test_cases(1)):
    solve()
