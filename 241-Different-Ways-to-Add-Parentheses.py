class Solution:
    def __init__(self):
        self.memo = {}
    
    def solveTopDown(self, s):
        if s in self.memo:
            return self.memo[s]
        
        ans = []
        for i in range(len(s)):
            if s[i] in \+-*\:
                left = self.solveTopDown(s[:i])
                right = self.solveTopDown(s[i+1:])
                
                for l in left:
                    for r in right:
                        if s[i] == '+':
                            ans.append(l + r)
                        elif s[i] == '-':
                            ans.append(l - r)
                        else:
                            ans.append(l * r)
        
        if not ans:
            ans.append(int(s))
        
        self.memo[s] = ans
        return ans
    
    def diffWaysToCompute(self, expression: str):
        return self.solveTopDown(expression)