# Function to find non-repeating elements in an array
def findNonRepeatingElement(nums):
    hashMap = {}  # Dictionary to store element counts

    # Count occurrences of each element
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1

    # Print non-repeating elements (count == 1)
    print("Non-repeating numbers are:", end=" ")
    for num, count in hashMap.items():
        if count == 1:
            print(num, end=" ")

# Driver code
nums = [1, 2, -1, 1, 3, 1]  # Example input
findNonRepeatingElement(nums)  # Call function to find non-repeating elements
