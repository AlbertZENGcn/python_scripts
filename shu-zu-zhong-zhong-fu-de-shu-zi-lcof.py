class Solution:
    def findRepeatNumber(self, nums):
        for i in range(0, len(nums) - 1):
            for j in range(i+1,len(nums) - 1):
                if nums[i] == nums[j]:
                    print(nums[i])
                    return nums[j]
s=Solution()
s.findRepeatNumber([3, 1, 2, 3])
