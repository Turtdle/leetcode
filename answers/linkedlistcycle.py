def hasCycle(head: Optional[ListNode]) -> bool:

    
    """
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.
    """
    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True