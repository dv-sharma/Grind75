class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True
        cleanedstring=""
        cleanedstring=cleanedstring.join(i.lower() for i in s if i.isalnum())

        if cleanedstring== cleanedstring[::-1]:
            return True
        else:
            return False

        #front=0
        #back=len(cleanedstring)-1
        #frontstr=""
        #backstr=""
        #
        #while front<=len(cleanedstring)/2:
        #    frontstr+=frontstr
        #    backstr+=backstr
        #    if frontstr!=backstr:
        #        return False
#
        #    front+=1
        #    back-=1
        #return True
        
