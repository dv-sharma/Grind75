import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countdict=Counter(nums)
        max_heap=[]

        for num,frequency in countdict.items():
            max_heap.append((num,-frequency))
        heapq.heapify(max_heap)

        result=[]
        for _ in range(k):
            num,frequency=heapq.heappop(max_heap)
            result.append(num)
        return result



        
