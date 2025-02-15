class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s        # adding length of word and # before each word. this will help when converting back to original string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])        #extract length
            i = j + 1                   # prep i to extract word
            j = i + length              # prep j for next word
            res.append(s[i:j])          # extract word
            i = j               #prep for next word 
            
        return res