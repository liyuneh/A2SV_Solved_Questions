class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def memo(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in  dp:
                dp[i] = max(memo(i - 1), memo(i - 2) + nums[i])
            return dp[i]
        return memo(n - 1)