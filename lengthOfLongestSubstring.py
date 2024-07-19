class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        right=0
        charset=set()
        length=0
        

        while right<len(s):
            if s[right] not in charset:
                charset.add(s[right])
                right+=1
                length=max(length,right-left)
            else:
                charset.remove(s[left])
                left+=1
        return length



        
