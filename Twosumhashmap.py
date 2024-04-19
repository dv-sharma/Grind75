class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        valmap={}
        
        for index,val in enumerate(nums):
            difference=target-val
            if difference in valmap:
                return [valmap[difference],index]
            valmap[val]=index
        
