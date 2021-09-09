class Solution:
    # 只有一个数组的时候
    def nextGreaterElement(self, nums):
        dict, stack = {}, []

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                dict[i] = stack[-1]
            stack.append(nums[i])
        return [dict.get(x, -1) for x in nums]

    # 两个数组的时候，lc496
    def nextGreaterElement(self, nums1, nums2):
        dict, stack = {}, []
        for i in range(len(nums2) - 1, -1, -1):
            while (stack and stack[-1] <= nums2[i]):
                stack.pop()
            if stack:
                dict[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        return [dict.get(x, -1) for x in nums1]

    # 求下标的时候，lc739
    def nextTemperature(self, nums):
        res = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

    #数组变成环形数组，lc503
    def nextGreaterElements_special(self, nums):
        res=[-1 for _ in range(len(nums))]
        stack = []
        n = len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if stack:
                res[i % n] = stack[-1]
            stack.append(nums[i % n])
        return res


s = Solution()
nums = [2, 1, 2, 4, 3]
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
t = [73, 74, 75, 71, 69, 76]
result = s.nextGreaterElements_special(nums)
print(result)
