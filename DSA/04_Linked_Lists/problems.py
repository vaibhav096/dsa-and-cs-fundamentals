# ============================================================================
#                  LINKED LIST PROBLEMS - CODE SOLUTIONS
# ============================================================================

# Node Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper function to create linked list from array
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to array
def to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ============================================================================
# PROBLEM 1: REVERSE LINKED LIST
# Time: O(n), Space: O(1)
# ============================================================================

def reverse_list(head):
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1
    """
    prev = None
    current = head

    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward

    return prev


# Recursive version
def reverse_list_recursive(head):
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


print("Reverse List:", to_array(reverse_list(create_list([1, 2, 3, 4, 5]))))


# ============================================================================
# PROBLEM 2: DETECT CYCLE
# Time: O(n), Space: O(1)
# ============================================================================

def has_cycle(head):
    """
    Floyd's Cycle Detection (Tortoise and Hare)
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


# ============================================================================
# PROBLEM 3: FIND CYCLE START
# Time: O(n), Space: O(1)
# ============================================================================

def detect_cycle(head):
    """
    Returns node where cycle begins, or None
    """
    slow = fast = head

    # Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


# ============================================================================
# PROBLEM 4: FIND MIDDLE OF LIST
# Time: O(n), Space: O(1)
# ============================================================================

def find_middle(head):
    """
    For even length, returns second middle node
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


print("Middle of List:", find_middle(create_list([1, 2, 3, 4, 5])).val)


# ============================================================================
# PROBLEM 5: REMOVE NTH NODE FROM END
# Time: O(n), Space: O(1)
# ============================================================================

def remove_nth_from_end(head, n):
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5
    """
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove nth node
    slow.next = slow.next.next

    return dummy.next


print("Remove 2nd from end:", to_array(remove_nth_from_end(create_list([1, 2, 3, 4, 5]), 2)))


# ============================================================================
# PROBLEM 6: MERGE TWO SORTED LISTS
# Time: O(n+m), Space: O(1)
# ============================================================================

def merge_two_lists(l1, l2):
    """
    Input: 1 -> 2 -> 4 and 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2

    return dummy.next


l1 = create_list([1, 2, 4])
l2 = create_list([1, 3, 4])
print("Merge Lists:", to_array(merge_two_lists(l1, l2)))


# ============================================================================
# PROBLEM 7: CHECK PALINDROME
# Time: O(n), Space: O(1)
# ============================================================================

def is_palindrome(head):
    """
    Input: 1 -> 2 -> 2 -> 1
    Output: True
    """
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


print("Is Palindrome [1,2,2,1]:", is_palindrome(create_list([1, 2, 2, 1])))
print("Is Palindrome [1,2,3]:", is_palindrome(create_list([1, 2, 3])))


# ============================================================================
# PROBLEM 8: INTERSECTION OF TWO LISTS
# Time: O(n+m), Space: O(1)
# ============================================================================

def get_intersection(headA, headB):
    """
    Find node where two lists intersect
    """
    if not headA or not headB:
        return None

    a, b = headA, headB

    # When one reaches end, redirect to other list's head
    # They will meet at intersection or both become None
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a


# ============================================================================
# PROBLEM 9: ADD TWO NUMBERS
# Numbers stored in reverse order
# Time: O(max(n,m)), Space: O(max(n,m))
# ============================================================================

def add_two_numbers(l1, l2):
    """
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8 (342 + 465 = 807)
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])
print("Add Two Numbers:", to_array(add_two_numbers(l1, l2)))


# ============================================================================
# PROBLEM 10: REMOVE DUPLICATES FROM SORTED LIST
# Time: O(n), Space: O(1)
# ============================================================================

def delete_duplicates(head):
    """
    Input: 1 -> 1 -> 2 -> 3 -> 3
    Output: 1 -> 2 -> 3
    """
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


print("Remove Duplicates:", to_array(delete_duplicates(create_list([1, 1, 2, 3, 3]))))


# ============================================================================
# PROBLEM 11: REVERSE NODES IN K-GROUP
# Time: O(n), Space: O(1)
# ============================================================================

def reverse_k_group(head, k):
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 2 -> 1 -> 4 -> 3 -> 5
    """
    # Count nodes
    count = 0
    node = head
    while node:
        count += 1
        node = node.next

    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy

    while count >= k:
        # Reverse k nodes
        prev = None
        current = prev_group.next

        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Connect groups
        tail = prev_group.next
        tail.next = current
        prev_group.next = prev
        prev_group = tail

        count -= k

    return dummy.next


print("Reverse K-Group:", to_array(reverse_k_group(create_list([1, 2, 3, 4, 5]), 2)))


# ============================================================================
# PROBLEM 12: SORT LIST (Merge Sort)
# Time: O(n log n), Space: O(log n)
# ============================================================================

def sort_list(head):
    """
    Input: 4 -> 2 -> 1 -> 3
    Output: 1 -> 2 -> 3 -> 4
    """
    if not head or not head.next:
        return head

    # Find middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    # Sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Merge sorted halves
    return merge_two_lists(left, right)


print("Sort List:", to_array(sort_list(create_list([4, 2, 1, 3]))))


# ============================================================================
# PROBLEM 13: ROTATE LIST
# Time: O(n), Space: O(1)
# ============================================================================

def rotate_right(head, k):
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 4 -> 5 -> 1 -> 2 -> 3
    """
    if not head or not head.next or k == 0:
        return head

    # Find length and tail
    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next

    # Normalize k
    k = k % length
    if k == 0:
        return head

    # Find new tail (length - k - 1 from head)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Rotate
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head


print("Rotate List:", to_array(rotate_right(create_list([1, 2, 3, 4, 5]), 2)))


# ============================================================================
# PROBLEM 14: ODD EVEN LINKED LIST
# Group odd indices first, then even indices
# Time: O(n), Space: O(1)
# ============================================================================

def odd_even_list(head):
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 3 -> 5 -> 2 -> 4
    """
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


print("Odd Even List:", to_array(odd_even_list(create_list([1, 2, 3, 4, 5]))))


# ============================================================================
# PROBLEM 15: SWAP NODES IN PAIRS
# Time: O(n), Space: O(1)
# ============================================================================

def swap_pairs(head):
    """
    Input: 1 -> 2 -> 3 -> 4
    Output: 2 -> 1 -> 4 -> 3
    """
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # Swap
        first.next = second.next
        second.next = first
        prev.next = second

        prev = first

    return dummy.next


print("Swap Pairs:", to_array(swap_pairs(create_list([1, 2, 3, 4]))))


# ============================================================================
# PROBLEM 16: REORDER LIST
# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
# Time: O(n), Space: O(1)
# ============================================================================

def reorder_list(head):
    """
    Input: 1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 5 -> 2 -> 4 -> 3
    """
    if not head or not head.next:
        return head

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    current = slow.next
    slow.next = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Merge two halves
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

    return head


result = create_list([1, 2, 3, 4, 5])
reorder_list(result)
print("Reorder List:", to_array(result))


print("\n=== All Linked List Problems Complete ===")
