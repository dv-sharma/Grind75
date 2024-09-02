###################METHOD 1
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:

        stringdict={}

        for words in s:
            print(f'{ord(words)},{words}')
            print(ord('a'))
            if words in stringdict:
                stringdict[words]+=1
            else:
                stringdict[words]=1
        

    
        for val,index in enumerate(s):
            if stringdict[index]==1:
                return val
        return -1

  ##########################################################METHOD 2'
  from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:

        count=[0]*26

        for nums in s:
            count[ord(nums)-ord('a')]+=1
        
        for index,val in enumerate(s):
            if count[ord(val)- ord('a')]==1:
                return index
        
        return -1
        
