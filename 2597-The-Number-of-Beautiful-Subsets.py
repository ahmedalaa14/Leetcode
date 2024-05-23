class Solution(object):
    def beautifulSubsets(self, nums, k):
        def is_beautiful(subset):
            num_set = set(subset)
            for num in num_set:
                if (num + k) in num_set or (num - k) in num_set:
                    return False
            return True
        def backtrack(start, curr):
            if is_beautiful(curr):
                self.count += 1
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        self.count = 0
        backtrack(0, [])
        return self.count - 1                       