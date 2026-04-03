# Function to calculate the median of the array
def getMedian(arr, n):
    arr.sort()  # Sort the array to arrange elements in order

    if n % 2 == 0:
        # If the array size is even, calculate the average of two middle elements
        ind1 = (n // 2) - 1
        ind2 = (n // 2)
        print((arr[ind1] + arr[ind2]) / 2)  # Return the median for even-sized array
    else:
        # If the array size is odd, return the middle element
        print(arr[n // 2])


# Driver code
arr = [4, 7, 1, 2, 5, 6]
n = 6
print("The median of the array is: ", end="")
getMedian(arr, n)  # Function call to calculate and print the median
