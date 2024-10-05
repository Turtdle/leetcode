def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    output = head

    while head != None:
        if head.next != None and head.next.val == val:
            head.next = head.next.next
        else:
            head = head.next

    if output != None and output.val == val:
        return output.next
    return output
    