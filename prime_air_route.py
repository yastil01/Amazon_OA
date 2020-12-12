from collections import defaultdict
class Solution(object):
    def optimalFlightPath(self, maxTravelDist, forwardRouteList, returnRouteList):
        
        diffDist = defaultdict(list)
        
        fList = sorted(forwardRouteList, key=lambda x:x[1])
        rList = sorted(returnRouteList, key=lambda x:x[1])
        fl, rr = 0, len(rList) - 1
        
        while fl < len(fList) and rr >= 0:
            diff = maxTravelDist - (fList[fl][1] + rList[rr][1])
            if  diff >= 0 :
                diffDist[diff].append([fList[fl][0],rList[rr][0]])
                fl += 1
            else:
                rr -= 1
        
        if not diffDist:
            return -1
        
        minDiff = float('inf')
        for k in diffDist:
            minDiff = min(minDiff, k)
        
        return diffDist[minDiff]
    
obj = Solution()
maxTravelDist=7000
forwardRouteList=[[1,2000],[2,4000],[3,6000]]
returnRouteList=[[1,2000]]
ans = obj.optimalFlightPath(maxTravelDist, forwardRouteList, returnRouteList)
print(ans)       
