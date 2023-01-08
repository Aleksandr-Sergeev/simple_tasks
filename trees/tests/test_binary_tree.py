from trees.core.binary_tree import BalancedTree
import pytest


@pytest.fixture(scope='module')
def setup_random_balanced_tree():
    return BalancedTree.generate_random_balanced_tree()


def test_balanced_tree_inorder_traversals(setup_random_balanced_tree):
    setup_random_balanced_tree.generate_inorder_traversal_iteratively()
    list_inorder_traversal_iteratively = setup_random_balanced_tree.inorder_traversal_list.copy()
    setup_random_balanced_tree.generate_inorder_traversal_recursive()
    assert list_inorder_traversal_iteratively == setup_random_balanced_tree.inorder_traversal_list
