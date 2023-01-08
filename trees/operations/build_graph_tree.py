from typing import List, Tuple, Dict, Union

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


# TODO: разобраться как работают указатели в этой функции
def to_tree(source):
    result = {}
    branches = {}
    for parent_id, child_id in source:
        # для начальных узлов указываем место записи - result
        if parent_id is None:
            branch_pointer = result
        # для вложенных узлов указываем место записи - к parent в branches
        else:
            branch_pointer = branches.setdefault(parent_id, {})  # выставляем указатель на начало графа
        branch_pointer[child_id] = branches.setdefault(child_id, {})
    return result


assert to_tree(source) == expected

