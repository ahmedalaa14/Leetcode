class Solution(object):
    def decodeString(self, s):
        res = []
        for i in s:
            if i != ']':
                res.append(i)
            else:
                substring = ''
                while res[-1] != '[':
                    substring  = res.pop() + substring
                res.pop()
                
                digit = ''
                while res and res[-1].isdigit():
                    digit = res.pop() + digit
                res.append(int(digit) * substring)
        return ''.join(res)