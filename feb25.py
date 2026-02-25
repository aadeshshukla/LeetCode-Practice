# python leetcode 25
# 25. Reverse Nodes in k-Group
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            next_group = tail.next
            # reverse the group
            prev_next = prev.next
            curr = prev_next.next
            for i in range(k - 1):
                temp = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = temp
            prev_next.next = next_group
            prev = prev_next
# Example usage:
# Create a linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k = 2
solution = Solution()
new_head = solution.reverseKGroup(head, k)
# Print the reversed linked list
current = new_head
while current:
    print(current.val, end=' ')
    current = current.next
# Output: 2 1 4 3 5
# lets take linked list and k dynamically
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()
# Example usage:
arr = [1, 2, 3, 4, 5]
k = 3
head = create_linked_list(arr)
solution = Solution()
new_head = solution.reverseKGroup(head, k)
print_linked_list(new_head)
# Output: 3 2 1 4 5
