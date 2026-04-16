def print_binary(n):
    flag = False  # To skip leading zeroes

    # Loop from 32 down to 0
    for i in range(32, -1, -1):
        # Shift n right by i bits and check the LSB
        if (n >> i) & 1:
            flag = True  # First '1' encountered
            print(1, end='')
        else:
            if flag:
                print(0, end='')

# Call the function
print_binary(28)
