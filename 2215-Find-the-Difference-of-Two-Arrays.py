class Solution(object):
    def findDifference(self, num1, num2):
        first = list(set(num1)-set(num2))
        second = list(set(num2)-set(num1))
        return [first , second]
        