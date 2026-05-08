class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = Counter(words)
        heap = []

        for word, cnt in freq.items():
            heapq.heappush(heap, (-cnt, word))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans