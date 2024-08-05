from neural_network.capture_tree.node import Node


class Tree:

    def __init__(
            self,
            origin: str
    ) -> None:
        self.root = Node(origin, origin)

    def depth_search(
            self,
            node: Node = None,
            deeper_node: Node = None,
            visited: set = None,
    ):
        if visited is None:
            visited = set()
        if node is None:
            node = self.root
        if deeper_node is None:
            deeper_node = node
        print('Actual: ', node)
        print('Current Deeper: ', deeper_node)
        if node not in visited:
            visited.add(node)
            if (
                node.depth > deeper_node.depth
            ) or (
                node.depth == deeper_node.depth and node.has_queen
            ):
                deeper_node = node
            for child in node.children:
                deeper = self.depth_search(child, deeper_node, visited)
                print('Child Deeper: ', deeper)
                if (
                    deeper.depth > deeper_node.depth
                ) or (
                    deeper.depth == deeper_node.depth and deeper.has_queen
                ):
                    deeper_node = deeper
                print('---------')
        return deeper_node

    def trace_back(self, node: Node):
        parent_list = [None] * (node.depth + 1)
        i = node.depth
        leaf = node
        while i >= 0:
            parent_list[i] = leaf
            leaf = leaf.parent
            i -= 1
        return parent_list
