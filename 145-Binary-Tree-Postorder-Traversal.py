class Solution(object):
    def postorderTraversal(self, root):
        num=[]
        def f(root):
            if root==None: return num
            f(root.left)
            f(root.right)
            num.append(root.val)
            return num
        return f(root)
        