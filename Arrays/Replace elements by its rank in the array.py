class Solution:
    # Function to replace elements by their rank in the array
    def replaceWithRank(self, arr):
        # Make a sorted copy of the array
        sorted_arr = sorted(arr)

        # Create a dictionary to hold ranks
        rank_map = {}

        # Initialize rank counter
        rank = 1

        # Assign ranks to unique elements
        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1

        # Build the result using rank map
        result = [rank_map[num] for num in arr]
        return result

# Driver code
obj = Solution()
arr = [1, 5, 8, 15, 8, 25, 9]
res = obj.replaceWithRank(arr)
print(*res)
