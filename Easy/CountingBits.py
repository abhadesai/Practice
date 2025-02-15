class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #Initialize array. Zero Indexing so n+1
        output = [0] * (n+1)

        for num in range(1, n+1): # remember - this represents how many times the loop needs to be run

            for i in range(32):
                #check all 32 bits of that number

                if (num & (1 << i)) != 0:
                    output[num] += 1
        return output