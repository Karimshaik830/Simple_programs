class Solution:
    # Function to convert octal to decimal
    def octal_to_decimal(self, Octal):
        # Initialize decimal result
        Decimal = 0
        # Position counter (power of 8)
        i = 0
        # Loop until all octal digits are processed
        while Octal != 0:
            # Get the last digit of octal number
            rem = Octal % 10
            # Add to decimal result after multiplying by 8^i
            Decimal += rem * (8 ** i)
            # Increment position
            i += 1
            # Remove the last digit from octal
            Octal //= 10
        # Return final decimal value
        return Decimal

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Example octal number
    Octal = 345
    # Call method to convert and print
    print("The decimal equivalent of the given octal number is",
          sol.octal_to_decimal(Octal))
