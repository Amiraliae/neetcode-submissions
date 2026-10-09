class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)): return False
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        for c in s1: counts1[c]+=1
        l  = r = 0
        while(r<len(s1)):
            counts2[s2[r]]+=1
            r+=1
        if(counts2 == counts1): return True
        while (r < len(s2)):
            counts2[s2[r]]+=1
            counts2[s2[l]]-=1
            if(counts2[s2[l]]==0): del counts2[s2[l]]
            r+=1
            l+=1
            if(counts2 == counts1): return True
        return False
            
             