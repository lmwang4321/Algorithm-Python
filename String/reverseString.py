class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right-1)
        helper(0, len(s)-1)

    def reverseOf(self, st):
        if st == '':
            return ''
        return self.reverseOf(st[1:])+st[0]

s = Solution()
st = 'TOP'
res = s.reverseOf(st)
print(res)