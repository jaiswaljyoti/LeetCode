class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_num = max(nums)
        weights = [0]*(max_num+1)
        for num in nums:
            weights[num] += num

        dp = [0]*(max_num+1)
        for i in range(1, max_num+1):
            if i == 1:
                dp[i] = weights[i]
            else:
                dp[i] = max(dp[i-1], dp[i-2]+weights[i])

        return dp[-1]