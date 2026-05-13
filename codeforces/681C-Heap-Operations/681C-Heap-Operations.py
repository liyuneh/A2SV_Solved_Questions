import sys, math, heapq as heapq, itertools
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
    def getMin(heap, x):
        count = 0
        should = 0
        while  heap and heap[0] < x:
            heapq.heappop(heap)
            count += 1

        if not heap or heap[0] != x:
            should += 1
        
        return count, should

    def remove(heap):
        cnt = 0
        if not heap:
            heapq.heappush(heap, 0)
            cnt += 1

        heapq.heappop(heap)
        return True, cnt
    def insert(heap, val):
        heapq.heappush(heap, val)
        return True
    n = number()
    ans = []
    heap = []
    for _ in range(n):
        parts = words()
        if parts[0] == "insert":
            insert(heap, int(parts[1]))
            ans.append(f"{parts[0]} {parts[1]}")
        elif parts[0] == "removeMin":
            a, b = remove(heap)
            if b == 1:
                ans.append("insert 0")
            ans.append(parts[0])
        else:
            cnt, should = getMin(heap, int(parts[1]))
            # print(cnt, should)
            for _ in range(cnt):
                ans.append("removeMin")
            if should:
                insert(heap, int(parts[1]))
                ans.append(f"insert {parts[1]}")
            ans.append(f"getMin {parts[1]}")
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])
    return


for _ in range(test_cases(1)):
    solve()