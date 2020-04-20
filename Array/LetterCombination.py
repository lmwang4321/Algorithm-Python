class Solution:
    def letterCombinations(self, digits):
        lookup = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not digits:
            return []
        n = len(digits)
        res = []
        def helper(i,tmp):
            if i == n:
                res.append(tmp)
                return 
            for alp in lookup[digits[i]]:
                helper(i+1,tmp+alp)
        helper(0,"")
        return res

    def letterCombinations2(self, digits):
        phone = {'2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z']}
        
        if not digits:return []
        
        res = ['']
        tem = []
        for i in digits:
            #res = [x+y for x in res for y in phone[i]]
            for x in res:
                for y in phone[i]:
                    tem.append(x+y)
                    print("tem: ", tem)
            print("res: ", res)
            res = tem
            tem=[]
                
        return res

s = Solution()
lsl = s.letterCombinations2("256")
print(lsl)