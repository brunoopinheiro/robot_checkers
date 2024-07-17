from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Pose:
    """Represents a robot pose with its
    x, y, z, roll, pitch and yaw values."""

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

    @property
    def to_dict(self) -> dict[str, float]:
        return self.__dict__

    @property
    def to_list(self) -> list[float]:
        return [
            self.x,
            self.y,
            self.z,
            self.roll,
            self.pitch,
            self.yaw,
        ]
