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
    n , l , r = numbers()
    arr = numbers()
    left, right = [], []
    cnt1, cnt2 = Counter(arr[:l]), Counter(arr[l:])
    for k, v in cnt1.items():
        if v > cnt2[k]:
            left.append(v - cnt2[k])
    for k, v in cnt2.items():
        if v > cnt1[k]:
            right.append(v - cnt1[k])
    # print(left, right)
    a, b = sum(left), sum(right)
    ans = 0
    if a < b:
        left, right = right, left
        a, b = b, a
    ans += b
    want = (a - b) // 2
    left.sort(reverse=True)
    right.sort(reverse=True)
    for cur in left:
        can = cur // 2
        ans += min(can, want)
        want -= min(can, want)
    if want:
        ans += (want * 2)
    print(ans)
    return


for _ in range(test_cases()):
    solve()
