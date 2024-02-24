class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies) - extraCandies
        return map(lambda x: x>=m, candies)