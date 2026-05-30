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
    s = list(word())
    s = [int(x) for x in s]
    a,b, c = s.count(0) if 0 in s else 0 ,s.count(1) if 1 in s else 0, s.count(2) if 2 in s else 0


    arr = ['+'] * ( n )
    for i in range(n):
        if (i < a + c or i >= n - b -c) : arr[i] = "?"
        if (i < a or i >= n - b or k == n) : arr[i] = '-'
    print("".join(arr))
    


    return


for _ in range(test_cases()):
    solve()