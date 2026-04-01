class Solution:
    # Function to reverse a section of the array
    def reverse_section(self, arr, start, end):
        # Swap elements until section is reversed
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Function to left rotate array by d positions
    def left_rotate(self, arr, d):
        n = len(arr)
        # If d is greater than array size, take modulo
        d = d % n
        if d == 0:
            return

        # Reverse first d elements
        self.reverse_section(arr, 0, d - 1)
        # Reverse remaining n-d elements
        self.reverse_section(arr, d, n - 1)
        # Reverse whole array
        self.reverse_section(arr, 0, n - 1)

    # Function to right rotate array by d positions
    def right_rotate(self, arr, d):
        n = len(arr)
        # Right rotation by d is same as left rotation by n-d
        self.left_rotate(arr, n - (d % n))

# Driver code
if __name__ == "__main__":
    # Create object of Solution
    obj = Solution()

    # Example array
    arr = [1, 2, 3, 4, 5]
    k = 2

    # Perform left rotation
    obj.left_rotate(arr, k)
    print("Left Rotation:", arr)

    # Reset array
    arr = [1, 2, 3, 4, 5]

    # Perform right rotation
    obj.right_rotate(arr, k)
    print("Right Rotation:", arr)
