# Function to find repeating elements in the array
def findRepeatingElements(arr):
    arr.sort()  # Sort the array to easily find duplicates

    print("The repeating elements are:", end=" ")
    for i in range(len(arr) - 1):
        # If current element is equal to next element, it's a repeating element
        if arr[i] == arr[i + 1]:
            print(arr[i], end=" ")


# Driver code
arr = [1, 1, 2, 3, 4, 4, 5, 2]  # Example input
findRepeatingElements(arr)  # Call the function to find repeating elements
print(" ")
#######

from collections import Counter


# Function to find repeating elements in an array
def findRepeatingElements(arr):
    elementCount = Counter(arr)  # Count occurrences of each element

    print("The repeating elements are:", end=" ")
    # Print the elements that appear more than once
    for element, count in elementCount.items():
        if count > 1:
            print(element, end=" ")


# Driver code
arr = [1, 1, 2, 3, 4, 4, 5, 2]  # Example input
findRepeatingElements(arr)  # Call function to find repeating elements
