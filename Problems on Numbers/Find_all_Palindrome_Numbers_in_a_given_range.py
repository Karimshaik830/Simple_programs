def isPalindrome(n):
    reverse = 0
    temp = n
    # Reverse the number by extracting its digits
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
        # If n and reverse are the same, then n is a palindrome
    return n == reverse
#Driver code
min_val = 100
max_val = 150  # Loop through all numbers in the given range
for i in range(min_val, max_val + 1):
    if  isPalindrome(i):
        print(i, end=" ")