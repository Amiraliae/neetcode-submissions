class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start  = 0
        size = 1e7
        l = r = 0
        tcount = defaultdict(int)
        scount = defaultdict(int)
        for c in t: tcount[c]+=1
        have, need = 0, len(tcount)
        while r<len(s) :
            c = s[r]
            scount[c]+=1
            if c in tcount and scount[c] == tcount[c]:
                have += 1
            r+=1
            while have == need:
                if(r-l<size): 
                    start= l 
                    size = r-l
                if s[l] in tcount and scount[s[l]] == tcount[s[l]]:
                    have -= 1
                scount[s[l]]-=1
                l+=1
            
        if size == 1e7:
            return ""
        return s[start:start+size]