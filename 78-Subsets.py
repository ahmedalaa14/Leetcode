class Solution(object):
    def subsets(self, nums):
        Ans = []
        n = len(nums)

        def Helper(op, start_index):
            if start_index == n:
                Ans.append(list(op))
                return
            
            op.append(nums[start_index])
            Helper(op, start_index + 1)
            
            op.pop()
            
            Helper(op, start_index + 1)
        
        Helper([], 0)
        return Ans