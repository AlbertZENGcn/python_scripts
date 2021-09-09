class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # odd
            s1 = self.find(s, i, i)
            # even
            s2 = self.find(s, i, i + 1)
            if max(len(s1), len(s2)) > len(res):
                res = s2 if len(s1) < len(s2) else s1
        return res
    # 找回文
    def find(selfs, s, left, right):
        while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


base = Solution()
s = "babad"
res = base.longestPalindrome(s)
print(res)
