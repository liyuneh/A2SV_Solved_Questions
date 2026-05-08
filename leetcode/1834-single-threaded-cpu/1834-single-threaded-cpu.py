class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        freq = []
        for i, (en, time) in enumerate(tasks):
            freq.append((en, time, i))
        heap = []
        freq.sort()

        ans = []
        time = 0
        i = 0
        n = len(freq)
        i = 0
        while i < n or heap:
            if not heap and time < freq[i][0]:
                time = freq[i][0]
            
            while i < n and freq[i][0] <= time:
                en, pro, idx = freq[i]
                heapq.heappush(heap, (pro, idx))
                i += 1
            pro, idx = heappop(heap)

            time += pro
            ans.append(idx)
        return ans