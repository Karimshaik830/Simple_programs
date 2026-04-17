import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Merges k sorted linked lists into one sorted linked list.
        Time Complexity: O(N log k) where N is the total number of nodes.
        Space Complexity: O(k) for the priority queue.
        """
        # A min-priority queue to keep track of the smallest node across all lists
        min_heap = []

        # 1. Push the head of each non-empty list into the heap
        # We store (node.val, index, node) to ensure uniqueness in comparisons
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))

        # 2. Use a dummy node to simplify building the new list
        dummy = ListNode(0)
        current = dummy

        # 3. Process the heap until empty
        while min_heap:
            # Get the node with the smallest value
            val, i, node = heapq.heappop(min_heap)

            # Append it to our result list
            current.next = node
            current = current.next

            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next


# --- Example Usage ---
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


# Input: [[1,4,5],[1,3,4],[2,6]]
l1 = create_linked_list([1, 4, 5])
l2 = create_linked_list([1, 3, 4])
l3 = create_linked_list([2, 6])

sol = Solution()
merged = sol.mergeKLists([l1, l2, l3])
print_linked_list(merged)  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6