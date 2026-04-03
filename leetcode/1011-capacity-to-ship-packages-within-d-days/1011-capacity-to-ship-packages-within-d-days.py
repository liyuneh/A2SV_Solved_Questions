class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(num):
            count = 1
            dmr = 0
            for i in range(len(weights)):
                if dmr + weights[i] <= num:
                    dmr += weights[i]
                else:
                    dmr = weights[i]
                    count += 1
            return count <= days
        total = sum(weights)
        mm = max(weights)
        
        while mm < total :
            mid = (total + mm) // 2
            if checker(mid):
                total = mid
            else:
                mm = mid + 1
        return mm