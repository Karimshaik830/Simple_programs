class Solution:
    # Function to convert a decimal number to its octal representation
    def decimalToOctal(self, decimal: int) -> str:
        # Handle the edge case where the input is 0
        if decimal == 0:
            return "0"

        octal = ""
        n = decimal

        # Loop until the number becomes 0
        while n > 0:
            # Get the remainder when dividing by 8
            remainder = n % 8
            # Prepend the remainder to the result string
            octal = str(remainder) + octal
            # Update the number using integer division
            n = n // 8

        return octal


# Driver code to test the solution
if __name__ == "__main__":
    sol = Solution()
    decimal_number = 17
    result = sol.decimalToOctal(decimal_number)
    print(f"Decimal: {decimal_number}, Octal: {result}")

    decimal_number = 45
    result = sol.decimalToOctal(decimal_number)
    print(f"Decimal: {decimal_number}, Octal: {result}")