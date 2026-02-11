class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        counter = Counter()
        for i in range(len(responses)):
            num = []
            seen = set()
            for k in range(len(responses[i])):
                if responses[i][k] not in seen:
                    seen.add(responses[i][k])
                    num.append(responses[i][k])
            for j in range(len(num)):
                counter[num[j]] += 1
        nums = sorted(counter.items(), key = lambda x:(-x[1],x[0]))
        return nums[0][0]
