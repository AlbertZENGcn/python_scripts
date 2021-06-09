class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lens=len(nums)
        res=list()
        nums.sort()

        for first in range(lens):
            if(first>0and nums[first]==nums[first-1]):continue
            third=lens-1
            target=-nums[first]
            for second in range(first+1,lens):
                if(second>first+1 and nums[second]==nums[second-1]): continue
                while(second<third and nums[second]+nums[third]>target):
                    third-=1
                if(third==second): break
                if(nums[second]+nums[third]==target):
                    res.append([nums[first],nums[second],nums[third]])
        return res

