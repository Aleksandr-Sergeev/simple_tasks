import random
from ..core.binary_tree import BalancedTree


def check_if_binary_trees_equal(first: BalancedTree, second: BalancedTree):
    first_stack, second_stack = [], []
    first_current, second_current = first.graph_tree, second.graph_tree
    first_hight, second_hight = 0, 0
    while (first_stack and second_stack) or (first_current and second_current):
        while first_current or second_current:
            if first_current and second_current:
                first_stack.append(first_current)
                second_stack.append(second_current)
                first_hight += 1 if first else 0
                second_hight += 1 if first else 0
                first_current = first_current.left
                second_current = second_current.left
            elif not (first_current and second_current):
                pass
            else:
                return False
        first_current, second_current = first_stack.pop(), second_stack.pop()
        if first_current.value != second_current.value or abs(first_hight - second_hight) > 1:
            return False
        first_hight, second_hight = 0, 0
        first_current, second_current = first_current.right, second_current.right
    return True


if __name__ == '__main__':
    tree_one = BalancedTree.generate_random_balanced_tree()
    tree_one.generate_inorder_traversal_iteratively()
    tree_one.is_balanced()
    tree_two = BalancedTree.generate_random_balanced_tree()
    binary_trees_not_equal = check_if_binary_trees_equal(tree_one, tree_two)
    binary_trees_equal = check_if_binary_trees_equal(tree_one, tree_one)


