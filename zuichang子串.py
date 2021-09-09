class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # 滑动窗口问题
        # # 1 定义维护变量
        # res, seen = 0, {}
        # # 2 起始点
        # start = 0
        # n = len(s)
        # for end in range(n):
        #     # 3 进行操作，滑动窗口
        #     # 当前位置的元素个数+1
        #     seen[s[end]] = seen.get(s[end], 0) + 1
        #     # 每个字母都出现一次，不重复，则对结果进行更新
        #     if len(seen) == end - start + 1:
        #         res = max(res, end - start + 1)
        #     # 4 维护窗口，窗口大小可变
        #     while len(seen) < end - start + 1:
        #         seen[s[start]] -= 1
        #         if seen[s[start]] == 0:
        #             del seen[s[start]]
        #         start += 1
        # return seen
        max_res=''
        res=''
        for i in range(1,len(s)):
            res=s[0:i]
            times=len(s)//len(res)
            if len(s)%len(res)!=0:
                continue
            final=''
            for j in range(0,times):
                final+=res
            if final==s:
                max_res=res if len(res)>len(max_res) else max_res
        return max_res



if __name__ == '__main__':
  s=Solution()
  str="abcabcabc"
  result=s.lengthOfLongestSubstring(str)
  print(result)

