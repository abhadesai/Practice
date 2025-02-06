class Solution:
    def reverseBits(self, n: int) -> int:

        reversed_num = 0
        for i in range(32):  # Assuming we are working with 32-bit integers
            reversed_num = (reversed_num << 1) | (n & 1)  # Shift left and append the last bit of n
            n >>= 1  # Shift n right to process the next bit
        return reversed_num
 