class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        freqdict={}
        pair=0

        for durations in time:
            modnum=durations%60

            if modnum==0:
                if 0 in freqdict:
                    pair+=freqdict[0]
            elif 60-modnum in freqdict:
                pair+=freqdict[60-modnum]
            
            if modnum in freqdict:
                freqdict[modnum]+=1
            else:
                freqdict[modnum]=1
        return pair


    
        
