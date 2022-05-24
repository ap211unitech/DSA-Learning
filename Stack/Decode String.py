

class Solution:
    def decodeString(self, s):

        num = []
        let = []
        res = ""
        i = 0

        while(i < len(s)):
            if s[i].isdigit():
                number = ''
                while(i < len(s) and s[i].isdigit()):
                    number += s[i]
                    i += 1
                num.append(int(number))
            elif s[i] == "[":
                let.append(res)
                res = ""
                i += 1
            elif s[i] == "]":
                u = let[-1]+res*num[-1]
                let.pop()
                num.pop()
                res = u
                i += 1
            else:
                res += s[i]
                i += 1
            # print(num,let,res)
        return res


ob = Solution()
print(ob.decodeString(input()))
