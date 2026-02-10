class Solution:
    def isHappy(self, n: int) -> bool:
        was = set()
        while n != 1 and n not in was:
            was.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1

