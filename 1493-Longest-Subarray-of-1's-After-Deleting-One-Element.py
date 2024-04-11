class Solution(object):
    def longestSubarray(self, nums):
        prevWindow = 0
        currWindow = 0
        max_length = 0

        for num in nums:
            if num == 0:
                max_length = max(max_length, prevWindow + currWindow)
                prevWindow = currWindow
                currWindow = 0
            else:
                currWindow += 1

        if currWindow == len(nums):
            return currWindow - 1

        max_length = max(max_length, prevWindow + currWindow)
        return max_length
        