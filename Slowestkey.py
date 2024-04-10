class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key=keysPressed[0]
        time=releaseTimes[0]

        for i in range(1,len(releaseTimes)):
            curr_time=releaseTimes[i]-releaseTimes[i-1]
            if curr_time>time:
                time=curr_time
                key=keysPressed[i]
            elif curr_time==time:
                if keysPressed[i]>key:
                    key=keysPressed[i]
                
        return key
     

      

            
          


        
