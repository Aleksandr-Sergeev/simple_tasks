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


def to_tree(source_info: List[Tuple[Union[str, None]]]) -> Dict:
    def get_edges(current_graph_edge: str) -> Dict:
        deeper_edges = dict()
        # deeper_edge = dict()
        for current_graph_verge in graph:
            if current_graph_edge == current_graph_verge[0]:
                deeper_edge = get_edges(current_graph_verge[1])
                if deeper_edge in deeper_edges.items():
                    deeper_edges[deeper_edge] += deeper_edge
                else:
                    deeper_edges.update(deeper_edge)
        return {current_graph_edge: deeper_edges}

    graph = source_info.copy()
    to_pop = list()
    result_tree = dict()
    for graph_verge_num, graph_verge in enumerate(graph):
        if not graph_verge[0]:
            result_tree[graph_verge[1]] = {}
            to_pop += [graph_verge_num]
    graph = [graph_verge for index, graph_verge in enumerate(graph) if index not in to_pop]
    for start_edge in result_tree:
        result_tree.update(get_edges(current_graph_edge=start_edge))
    return result_tree


assert to_tree(source) == expected

