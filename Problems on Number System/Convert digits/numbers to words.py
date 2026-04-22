class Solution:
    def convert_num_into_word(self, s):
        # Words for single digits
        single_digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        # Words for numbers from 10 to 19
        two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

        # Words for multiples of ten from 20 onwards
        tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        # Words for higher powers
        tens_power = ["hundred", "thousand"]

        # Handle empty input
        if len(s) == 0:
            print("")
            return

        # Handle single digit input
        elif len(s) == 1:
            print(single_digit[int(s[0])])
            return

        # Store length of string
        length = len(s)

        # Loop through each digit
        for i in range(len(s)):
            # If more than two digits remain
            if length > 2:
                # Print digit and its place value if digit is not zero
                if int(s[i]) != 0:
                    print(single_digit[int(s[i])], end=" ")
                    print(tens_power[length - 3], end=" ")
                length -= 1
            else:
                # Handle numbers between 10 and 19
                if int(s[i]) == 1:
                    print(two_digits[int(s[i + 1])], end=" ")
                    return
                # Handle multiples of 10 and following digit
                elif int(s[i]) != 0:
                    print(tens_multiple[int(s[i])], end=" ")
                    if int(s[i + 1]) != 0:
                        print(single_digit[int(s[i + 1])], end=" ")
                    return

if __name__ == "__main__":
    # Create solution object
    sol = Solution()

    # Example input
    num = "9090"

    # Call method
    sol.convert_num_into_word(num)

