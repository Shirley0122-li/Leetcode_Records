class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        res = num1
        num2_bits = bin(num2).count("1")
        res_bits = bin(num1).count("1")

        # Add '1' to result if res_bits < num2_bits
        if res_bits < num2_bits:
            for i in range(32):  # Iterate through all 32 bits
                if (res & (1 << i)) == 0:  # If the bit is not set
                    res |= (1 << i)  # Set the bit
                    res_bits += 1
                if res_bits == num2_bits:
                    break

        # Remove '1' from result if res_bits > num2_bits
        elif res_bits > num2_bits:
            for i in range(32):  # Iterate through all 32 bits
                if (res & (1 << i)) != 0:  # If the bit is set
                    res &= ~(1 << i)  # Clear the bit
                    res_bits -= 1
                if res_bits == num2_bits:
                    break
        
        return res