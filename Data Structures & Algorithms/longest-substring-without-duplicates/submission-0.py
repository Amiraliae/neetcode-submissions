class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = left =0
        seen = set()
        ans = 0
        while  right < len(s):
            
            while s[right] in seen:
                seen.remove(s[left])
                left+=1   
            seen.add(s[right])
            ans = max(ans,right-left+1)
            right+=1
        return ans

            
