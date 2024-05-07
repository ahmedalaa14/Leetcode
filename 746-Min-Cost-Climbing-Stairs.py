class Solution(object):
    def minCostClimbingStairs(self, cost):
        c1, c2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            c1, c2 = c2, min(c1, c2)+cost[i]
        return min(c1, c2)