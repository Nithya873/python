class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # Handle negative numbers using 2's complement
        if num < 0:
            num += 2 ** 32

        hex_chars = "0123456789abcdef"
        result = []

        while num > 0:
            digit = num % 16
            result.append(hex_chars[digit])
            num //= 16

        # Reverse because we collected from least significant digit
        return "".join(reversed(result))
