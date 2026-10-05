class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + str(len(word)) + "#" + word

        return encoded
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            num = int(s[i:j])          # Digits before #
            start = j + 1             # First character after #
            words.append(s[start:start + num])
            i = start + num           # Start of the next length

        return words

        
            
