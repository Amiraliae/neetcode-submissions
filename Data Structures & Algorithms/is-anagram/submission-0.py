class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        si=sorted(s)
        ti=sorted(t)
        if si==ti: return True
        return False
