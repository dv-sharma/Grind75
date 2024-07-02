class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        cur_sum=0

        for val in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=val
            max_sum=max(max_sum,cur_sum)
        return max_sum

            
            

        
