class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start, end):
        # Edge case for empty or single node list
        if not self.head or self.length == 1 or end >= self.length or start < 0:
            return None
        # Let's identify some key points in the linked list
        temp = self.head
        # variable to store the node before the start index to be able to
        # reference it back when the partition has been reversed, and
        # we need to join it back to the main list
        actual_before = temp

        # Lets identify the starting node for the reverse
        for _ in range(start):
            actual_before = temp  # update the node before reference
            temp = temp.next  # move to the next node
        # we have found the temp_head for the partition to reverse
        temp_head = temp
        # Let's find the tail of the partition to reverse
        for _ in range(start, end):
            temp = temp.next
        # we found the tail of the partition
        temp_tail = temp
        # we keep a reference pointer to the node after the partition tail
        actual_after = temp.next

        # Now we have to reverse the linkedlist between the temp_head and temp_tail
        # let's consider the partition as a separate list and apply logic for reversing
        # a complete linked list
        before = None
        temp = actual_before.next
        after = temp.next
        for _ in range(start, end+1):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        # Now we have a reveres partition of the linked list
        # we now need to join it to the main list
        actual_before.next = temp_tail
        temp_head.next = actual_after
        print(f'Actual_before: {actual_before.value} -> start: {temp_head.value} ------ end: {temp_tail.value} -> actual_end: {actual_after.value}')


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# # Reverse a sublist within the linked list
# linked_list.reverse_between(1, 3)
# print("Reversed sublist (1, 3): ")
# linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# # Reverse a sublist of length 1 within the linked list
# linked_list.reverse_between(3, 3)
# print("Reversed sublist of length 1 (3, 3): ")
# linked_list.print_list()
#
# # Reverse an empty linked list
# empty_list = LinkedList(0)
# empty_list.make_empty
# empty_list.reverse_between(0, 0)
# print("Reversed empty linked list: ")
# empty_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None

"""
