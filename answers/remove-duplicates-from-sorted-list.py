def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    seen = set()
    prev = None
    current = head
    while current:
        if current.val in seen:
            prev.next = current.next
        else:
            seen.add(current.val)
            prev = current
        current = current.next
    
    return head