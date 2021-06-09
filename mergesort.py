class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(l, r):
            if l >= r: return 0
            m = (l + r) // 2
            res = mergeSort(l, m) + mergeSort(m + 1, r)
            i = 1
            j = m + 1
            tmp[l:r + 1] = nums[l:r + 1]
            for k in range(1, r + 1):
                if i == m + 1:
                    nums[k] = tmp[j]
                    j += 1
                elif j == r + 1:
                    nums[k] = tmp[i]
                    i += 1
                elif tmp[i] <= tmp[j]:
                    nums[k] = tmp[i]
                    i += 1
                else:
                    nums[k] = tmp[j]
                    j += 1
                    res += m - i + 1
            return res

        tmp = [0] * len(nums)
        return mergeSort(0, len(nums) - 1)
