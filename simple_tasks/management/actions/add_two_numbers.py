class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class ListNodes:
    def __init__(self, vals):
        self.head = None
        self.add_vals(vals[::-1])
        self.reversed_int = None

    def add_vals(self, vals):
        for val in vals:
            new_val = ListNode(val)
            new_val.next = self.head
            self.head = new_val

    def get_reversed_int(self, current):
        if not self.reversed_int:
            self.reversed_int = [current.val]
        else:
            self.reversed_int += [current.val]
        if current.next:
            self.get_reversed_int(current.next)
        else:
            self.reversed_int.reverse()
            self.reversed_int = sum(val * 10**index for index, val in enumerate(self.reversed_int[::-1]))
            return self.reversed_int
        return self.reversed_int


# class ListNodes:
#     def __init__(self, vals):
#         self.add_vals(vals[::-1])
#         self.reversed_int = None
#
#     def add_vals(self, vals):
#         for index, val in enumerate(vals):
#             new_val = ListNode(val)
#             try:
#                 new_val.next = vals[index+1]
#             except IndexError:
#                 new_val.next = None


list1 = [2, 4, 3]
list2 = [5, 6, 4]
linked_list_1 = ListNodes(list1)
linked_list_2 = ListNodes(list2)
expected = ListNodes([7, 0, 8])


class Solution:
    def add_two_numbers(self):
        sum = linked_list_1.get_reversed_int(linked_list_1.head) + linked_list_2.get_reversed_int(linked_list_2.head)
        res = [int(x) for x in str(sum)]
        res.reverse()
        res = ListNodes(res)