class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        minHeap = []
        
        for stick in sticks:
            heappush(minHeap, stick)
        
        cost = currCost = 0
        while len(minHeap) > 1:
            one = heappop(minHeap)
            two = heappop(minHeap)
            currCost = one + two
            cost += currCost
            heappush(minHeap, currCost)
            
        return cost
