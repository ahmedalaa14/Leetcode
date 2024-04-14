class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root :
            return 0 
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right :
                ans += root.left.val
            else :
                ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right) 

        return ans              
        