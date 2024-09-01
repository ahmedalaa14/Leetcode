class Solution(object):
    def construct2DArray(self, original, m, n):
        if n * m != len(original):
            return []
        
        ans = []
        temp = []
        cnt = 0
        
        for val in original:
            temp.append(val)  
            cnt += 1
            
            if cnt == n:  
                ans.append(temp) 
                temp = []  
                cnt = 0  

        return ans