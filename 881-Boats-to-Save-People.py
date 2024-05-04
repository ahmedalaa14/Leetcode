class Solution(object):
    def numRescueBoats(self, p, limit):
        p.sort()
        x=0
        l, r=0, len(p)-1
        while l<=r:
            x+=1
            if p[l]+p[r]<=limit:
                l+=1
            r-=1
        return x
        