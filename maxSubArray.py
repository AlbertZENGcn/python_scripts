class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lens=len(nums)
        if lens==0: return 0
        dp=[0 for _ in range(lens)]
        dp[0]=nums[0]
        for i in range(1,lens):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
        res=-100000
        for i in range(lens):
            res=max(res,dp[i])
        return res