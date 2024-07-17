from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Joint:
    """Representes a robot joint pose, with its values
    from j1 to j6 in float values."""

    j1: float
    j2: float
    j3: float
    j4: float
    j5: float
    j6: float

    @property
    def to_dict(self) -> dict[str, float]:
        return self.__dict__

    @property
    def to_list(self) -> list[float]:
        return [
            self.j1,
            self.j2,
            self.j3,
            self.j4,
            self.j5,
            self.j6,
        ]

    def __add__(self, other: Joint):
        self.j1 = self.j1 + other.j1
        self.j2 = self.j2 + other.j2
        self.j3 = self.j3 + other.j3
        self.j4 = self.j4 + other.j4
        self.j5 = self.j5 + other.j5
        self.j6 = self.j6 + other.j6
        return self
