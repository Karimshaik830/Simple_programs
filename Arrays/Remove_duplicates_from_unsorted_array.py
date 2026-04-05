# Solution class containing optimized method
class Solution:
    # Method to remove duplicates from array
    def remove_duplicates(self, arr):
        seen = {}
        result = []

        # Traverse each element
        for val in arr:
            # If not already seen, add to result
            if val not in seen:
                result.append(val)
                seen[val] = True

        return result

# Driver code
if __name__ == "__main__":
    arr = [4, 5, 4, 2, 2, 3, 1]
    sol = Solution()
    result = sol.remove_duplicates(arr)
    print("Array after removing duplicates:", result)
