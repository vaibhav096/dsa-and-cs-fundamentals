class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partitionLinkedList(self, head, x):
        if not head or not head.next:
            return head

        sdummy = ListNode(0)
        ldummy = ListNode(0)
        small = sdummy
        large = ldummy
        temp = head

        while temp:
            if temp.val < x:
                small.next = temp
                small = small.next
            else:
                large.next = temp
                large = large.next
            temp = temp.next  # FIXED: Move to next node!

        small.next = ldummy.next
        large.next = None  # Important: Terminate the list

        return sdummy.next

    def printList(self, head):
        result = []
        while head:
            result.append(str(head.val))
            head = head.next
        print(" -> ".join(result))


def buildLinkedList(values):
    """Build LL from list of values - O(n)"""
    if not values:
        return None
    head = ListNode(values[0])
    temp = head
    for val in values[1:]:
        temp.next = ListNode(val)
        temp = temp.next
    return head


if __name__ == "__main__":
    # Single line input: "1 7 4 6 3 8 9 2"
    values = list(map(int, input("Enter LL values (space-separated): ").split()))
    x = int(input("Enter partition value x: "))

    # Build linked list from input
    head = buildLinkedList(values)

    sol = Solution()

    print("Original: ", end="")
    sol.printList(head)

    newHead = sol.partitionLinkedList(head, x)

    print(f"After partition (x={x}): ", end="")
    sol.printList(newHead)
