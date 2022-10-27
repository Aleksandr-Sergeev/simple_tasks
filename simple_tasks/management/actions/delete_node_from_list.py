class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class ListNodes:
    def __init__(self, vals):
        self.head = None
        self.add_vals(vals[::-1])
        self.found_node = None

    def add_vals(self, vals):
        for val in vals:
            new_val = ListNode(val)
            new_val.next = self.head
            self.head = new_val

    def find_node(self, current, target_value):
        if target_value == current.val:
            self.found_node = current
        else:
            self.find_node(current.next, target_value)


test_list = [4, 5, 1, 9]
val_to_del = 5
linked_list = ListNodes(test_list)


class Solution:
    def delete_node(self):
        linked_list.find_node(linked_list.head, val_to_del)
        linked_list.found_node.val = linked_list.found_node.next
        linked_list.found_node.next = linked_list.found_node.next.next