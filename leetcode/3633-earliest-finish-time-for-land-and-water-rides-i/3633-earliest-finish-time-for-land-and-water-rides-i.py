class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        for i in range(len(landStartTime)):
            x = landStartTime[i] + landDuration[i]
            for j in range(len(waterStartTime)):
                finish = max(x, waterStartTime[j] ) +  waterDuration[j]
                ans = min(ans, finish)
        for i in range(len(waterStartTime)):
            x = waterStartTime[i] + waterDuration[i]
            for j in range(len(landStartTime)):
                finish = max(x,landStartTime[j]) + landDuration[j]
                ans = min(ans, finish)
        return ans 
                