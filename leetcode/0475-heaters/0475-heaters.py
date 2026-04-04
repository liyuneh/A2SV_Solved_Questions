class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        r = 0
        for num in houses:
            i = bisect_left(heaters, num)

            left = float("inf") if i == 0 else num - heaters[i-1]
            right = float("inf") if i == len(heaters) else heaters[i] - num
            min_dis = min(left, right)
            r = max(r, min_dis)


        return r