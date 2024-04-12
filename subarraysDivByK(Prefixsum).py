class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        lmap = defaultdict(int)
        lmap[0]=1
        count=0
        csum=0

        for i in range(len(nums)):
            csum=(csum+nums[i])%k
            csum=(csum+k)%k

            count+=lmap[csum]
            lmap[csum]+=1
        return count
        
