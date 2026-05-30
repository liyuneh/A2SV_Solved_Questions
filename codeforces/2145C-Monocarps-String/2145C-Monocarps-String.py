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
    s = word()
    count = Counter(s)
    if count['a'] == count['b']:
        print(0)
        return 

    pref = [0 ] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + (1 if s[i] == 'a' else -1)
    total = pref[n]

    ans = float('inf')
    freq = {0:0}
    for r in range(1, n + 1):
        l = pref[r] - total
        if l in freq:
            ans = min(ans, r - freq[l])
        freq[pref[r]] = r
    if ans >= n:
        print(-1)
    else:
        print(ans)
    return


for _ in range(test_cases()):
    solve()