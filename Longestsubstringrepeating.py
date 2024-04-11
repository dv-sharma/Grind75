class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wordset=set()
        left=0
        result=0
        for right in range(len(s)):
            while s[right] in wordset:
                wordset.remove(s[left])
                left+=1
            wordset.add(s[right])
            result=max(result,right-left+1)
        return result
