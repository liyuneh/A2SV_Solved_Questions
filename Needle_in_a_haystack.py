import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
from heapq import heappush, heappop, heapify


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp


def solve():
    s = word()
    t = word()
    counter_s = Counter(s)
    counter_t = Counter(t)
    for c in counter_s:
        if counter_s[c] > counter_t[c]:
            print("Impossible")
            return 
    
    for c in counter_s:
        counter_t[c] -= counter_s[c]
    new_ones = sorted(counter_t.keys())
    # print(new_ones)
    # print(counter_t[new_ones[0]])
    
    ans = []

    l = 0
    for r in range(1, len(s)):
        if ord(s[r]) >= ord(s[l]):
            ans.append(s[l:r])
            l = r
    ans.append(s[l:])
    q = deque(ans)
    new_string = []
    i = 0

    while q and i < len(new_ones):
        if ord(new_ones[i]) >= ord(q[0][0]):
            new_string.append(q.popleft())
        else:
            new_string.append(counter_t[new_ones[i]] * new_ones[i])
            i += 1
    while i < len(new_ones):
        new_string.append(counter_t[new_ones[i]] * new_ones[i])
        i += 1
    while q:
        new_string.append(q.popleft())
    print("".join(new_string))

    
    

    return

for _ in range(test_cases()):
    solve()
