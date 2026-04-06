# Function to insert at beginning of array
def insertAtBeginning(arr, x):
    arr.insert(0, x)
    return arr

# Driver code
arr = [2, 3, 4, 5]
x = 1
arr = insertAtBeginning(arr, x)
print(arr)


class Solution:
    # Function to insert at end of array
    def insertAtEnd(self, arr, x):
        arr.append(x)
        return arr

# Driver code
arr = [1, 2, 3, 4]
x = 5

obj = Solution()
arr = obj.insertAtEnd(arr, x)
print(arr)


class Solution:
    # Function to insert at a given position (0-based index)
    def insertAtPosition(self, arr, pos, x):
        arr.insert(pos, x)
        return arr

# Driver code
arr = [1, 2, 4, 5]
pos, x = 2, 3

obj = Solution()
arr = obj.insertAtPosition(arr, pos, x)
print(arr)
