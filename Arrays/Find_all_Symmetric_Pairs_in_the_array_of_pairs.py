# Function to find symmetric pairs in an array
def findSymmetricPairs(arr):
    mp = {}  # Dictionary to store first element and its pair
    print("The Symmetric Pairs are:")

    # Loop through the array to find symmetric pairs
    for i in range(len(arr)):
        first, second = arr[i]

        # Check if {second, first} existed previously
        if second in mp and mp[second] == first:
            print(f"({first} {second})", end=" ")
        else:
            # Store {first, second} pair in the map
            mp[first] = second

# Driver code
arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]  # Example input
findSymmetricPairs(arr)  # Call function to find symmetric pairs
