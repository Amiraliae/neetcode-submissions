class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        from collections import defaultdict
        counts = defaultdict(int)
        left = right = 0
        d = 0
        ans = 0
        while(right<len(s)):
            counts[s[right]]+=1
            right+=1
            while(right - left - max(counts.values()) > k):
                counts[s[left]]-=1
                left+=1
            ans = max(ans,right-left)
        
        return ans
        

