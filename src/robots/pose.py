from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pose:

    x: float
    y: float
    z: float
    roll: float
    pitch: float
    yaw: float

    def __add__(self, other: Pose) -> Pose:
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        self.roll = self.roll + other.roll
        self.pitch = self.pitch + other.pitch
        self.yaw = self.yaw + other.yaw
        return self

    def to_dict(self) -> dict[str, float]:
        return self.__dict__
