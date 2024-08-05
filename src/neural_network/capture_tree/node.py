from __future__ import annotations
from typing import Optional, List


class Node:

    @property
    def is_leaf(self) -> bool:
        return len(self.children) == 0

    @property
    def is_root(self) -> bool:
        return self.parent is None

    def __init__(
            self,
            target: str,
            destiny: str,
            has_queen: bool = False,
            parent: Optional[Node] = None,
            depth: int = 0
    ) -> None:
        self.parent = parent
        self.target = target
        self.destiny = destiny
        self.depth = depth
        self.has_queen = has_queen
        self.children: List[Node] = []

    def __str__(self) -> str:
        base_str = f'd:{self.depth}, t:{self.target} d:{self.destiny}'
        queen = '*' if self.has_queen else ''
        return f'Node({base_str} {queen})'

    def append_child(
            self,
            target: str,
            destiny: str,
            has_queen: bool = False,
    ) -> Node:
        child = Node(
            target=target,
            destiny=destiny,
            has_queen=has_queen,
            parent=self,
            depth=self.depth + 1,
        )
        self.children.append(child)
        return child
