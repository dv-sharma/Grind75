class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        map={}
        
        for numbers in nums:
                
            if numbers in map:
                return True
            else:
                map[numbers]=1
        return False

       


        
        
