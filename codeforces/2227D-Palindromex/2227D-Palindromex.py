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
    ans = [arr.index(0), 2 * n - 1 - arr[::-1].index(0)]

    def palia(arr, l):
        a = b = l
        count = 0
        while a >= 0 and b < 2 * n and arr[a] == arr[b]:
            count += 1
            a -= 1
            b += 1
        return count - 1
    def palib(arr, l, r):
        count = 0
        while l >= 0 and r < len(arr) and arr[l] == arr[r]:
            l -= 1
            r += 1
            count += 1
        return count - 1
    # print(palia(arr, ans[0]))
    def pali(arr, l , r):
        while l <= r :
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True
    def mex(arr):
        seen = set(arr)
        for i in range(max(arr) + 1):
            if i not in seen:
                return i
        return max(arr) + 1
    mx = 1
    if pali(arr, ans[0], ans[1]):
        mx = max(mx, mex(arr[ans[0]: ans[1] + 1]))
    x = palia(arr, ans[0])
    y = palia(arr, ans[1])
    if x != 0:
        mx = max(mx, mex(arr[ans[0] - x :ans[0] + x + 1]))

    if y != 0 :
        mx = max(mx, mex(arr[ans[1] - y:ans[1] + y +  1]))
    cnt = palib(arr,ans[0], ans[1])
    if pali(arr, ans[0], ans[1]):
        mx = max(mx, mex(arr[ans[0] - cnt:ans[1] + cnt + 1]))
    print(mx )
    # print()
    return


for _ in range(test_cases()):
    solve()