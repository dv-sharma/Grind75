class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=1
        right=1
        count=0
        while right<len(nums):
            if nums[right]!=nums[right-1]:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
                
                

        
