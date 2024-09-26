def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #start two vars, if var1 is less than var2, then append var1 to the new list and move var1 to the next node
    var1 = list1
    var2 = list2
    output = ListNode()
    current = output
    while var1 and var2:
        if var1.val < var2.val:
            current.next = var1
            var1 = var1.next
        else:
            current.next = var2
            var2 = var2.next
        current = current.next
    if var1:
        current.next = var1
    if var2:
        current.next = var2
    return output.next