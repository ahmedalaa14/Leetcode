class Solution:
    def getMaximumXor(self, nums, maximumBit):
        answer = [0] * len(nums)
        totalXor = 0
        maxNum = (1 << maximumBit) - 1  # maxNum with all bits set up to maximumBit
        
        for i in range(len(nums)):
            totalXor ^= nums[i]  # Update cumulative XOR
            answer[len(nums) - i - 1] = totalXor ^ maxNum  # Calculate k and store in reverse order
            
        return answer