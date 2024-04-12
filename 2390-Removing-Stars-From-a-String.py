class Solution(object):
    def removeStars(self, s):
        stack = []
        for char in s:
            if stack and char == '*':
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)            
        