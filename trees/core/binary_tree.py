import random


class TreeNode(object):
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.value}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree(object):
    def __init__(self, initial_list: list[int] | None):
        self.initial_list = initial_list
        self.graph_tree = None

    def is_balanced(self):
        def _get_hight(node):
            if node is None:
                return 0
            return 1 + (max(_get_hight(node.left), _get_hight(node.right)))

        def _is_balanced(node: TreeNode) -> bool:
            if node is None:
                return True
            return _is_balanced(node.left) \
                   and _is_balanced(node.right) \
                   and abs(_get_hight(node.left) - _get_hight(node.right)) <= 1

        return _is_balanced(self.graph_tree)


class BalancedTree(BinaryTree):
    def __init__(self, initial_list: list[int] | None):
        super(BalancedTree, self).__init__(initial_list)
        if isinstance(self.initial_list, list):
            self.initial_list.sort()
            self._create_graph_tree_from_array()

    @staticmethod
    def generate_random_balanced_tree():
        sample_list_generator = [random.randint(-500, 500) for i in range(100)]
        return BalancedTree(sample_list_generator)

    def _create_graph_tree_from_array(self):
        def __create_graph_node_instance(index: int) -> TreeNode | None:
            if index >= initial_list_len or initial_list[index] is None:
                return None
            node = TreeNode(initial_list[index])
            node.left = __create_graph_node_instance(index=2 * index + 1)
            node.right = __create_graph_node_instance(index=2 * index + 2)
            return node

        initial_list = self.initial_list
        initial_list_len = len(initial_list)
        self.graph_tree = __create_graph_node_instance(index=0)

    def generate_inorder_traversal_recursive(self):
        self.inorder_traversal_list = list()
        self._return_node_values_recursive(self.graph_tree)

    def _return_node_values_recursive(self, node: TreeNode):
        if node is None:
            return
        self._return_node_values_recursive(node.left)
        self.inorder_traversal_list.append(node.value)
        self._return_node_values_recursive(node.right)

    def generate_inorder_traversal_iteratively(self):
        current = self.graph_tree
        stack = []
        result = []
        while current or stack:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        self.inorder_traversal_list = result