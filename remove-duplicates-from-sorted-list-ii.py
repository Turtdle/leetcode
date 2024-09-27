def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev = dummy
    current = head
    while current:
        if current.next and current.val == current.next.val:
            while current.next and current.val == current.next.val:
                current = current.next
            prev.next = current.next
        else:
            prev = current
        current = current.next
    
    return dummy.next