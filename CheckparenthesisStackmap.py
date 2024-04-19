class Solution:
    def isValid(self, s: str) -> bool:

        charstack=[]
        charmap= {
            ')':    '(',
            ']':    '[',
            '}':    '{'

            }

        for chars in s:
            if chars in charmap:
                if charstack and charstack[-1]==charmap[chars]:
                    charstack.pop()
                else:
                    return False
            else:
                charstack.append(chars)
        if charstack:
            return False
        else:
             return True
