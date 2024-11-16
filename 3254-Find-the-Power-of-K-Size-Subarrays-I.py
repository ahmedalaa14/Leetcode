class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * (n - k + 1)  # Initialize answer list with -1
        i, j = 0, 0
        
        while j < n:
            if j > 0 and nums[j] - nums[j - 1] != 1:
                i = j  # Reset 'i' when the difference is not 1
            
            while i < j and j - i + 1 > k:
                i += 1  # Shrink the window if its size is greater than 'k'
            
            if j - i + 1 == k:
                ans[j - k + 1] = nums[j]  # Set the current number when the window size is exactly 'k'
            
            j += 1
        
        return ans