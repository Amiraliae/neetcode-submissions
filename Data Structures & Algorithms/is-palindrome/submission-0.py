class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned  = "".join(char.lower() for char in s if char.isalnum())
        reversedd = "".join(cleaned[i] for i in range(len(cleaned)-1,-1,-1) )
        return True if cleaned==reversedd else False