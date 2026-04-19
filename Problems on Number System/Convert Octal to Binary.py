class Solution:
    # Convert Octal to Decimal
    def octal_to_decimal(self, Octal):
        Decimal = 0
        i = 0
        while Octal != 0:
            rem = Octal % 10
            Decimal += rem * (8 ** i)
            i += 1
            Octal //= 10
        return Decimal

    # Convert Decimal to Binary
    def decimal_to_binary(self, decimal):
        Binary = 0
        i = 0
        while decimal != 0:
            rem = decimal % 2
            Binary += rem * (10 ** i)
            i += 1
            decimal //= 2
        return Binary

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Example input
    Octal = 345
    # Convert octal to decimal
    Decimal = sol.octal_to_decimal(Octal)
    # Print binary conversion
    print(sol.decimal_to_binary(Decimal))
