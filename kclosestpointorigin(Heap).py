class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        distanceheap=[]
        finallist=[]

        for x,y in points:
            priority= x**2+y**2
            heapq.heappush(distanceheap,(priority,x,y))

        for _ in range(k):
            _,x,y=heapq.heappop(distanceheap)
            finallist.append([x,y])
        return finallist
        
