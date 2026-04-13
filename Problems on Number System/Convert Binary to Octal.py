def binary_to_octal(s):
    n = len(s)

    # Pad leading zeros to make length a multiple of 3
    if n % 3 == 1:
        s = "00" + s
    elif n % 3 == 2:
        s = "0" + s

    n = len(s)
    ans = ""

    # Process every group of 3 bits
    for i in range(0, n, 3):
        temp = int(s[i]) * 4 + int(s[i + 1]) * 2 + int(s[i + 2]) * 1
        ans += str(temp)

    return ans

# Driver code
s = "1100110"
print(binary_to_octal(s))
