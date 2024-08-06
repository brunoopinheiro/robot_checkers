from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, List
from game.coordinates import Coordinates


class GameAIResultType(Enum):

    MOVEMENT = auto()
    CAPTURE = auto()


@dataclass
class Jump:

    target: Coordinates
    destiny: Coordinates


@dataclass
class GameAIResult:

    play_type: GameAIResultType
    origin: Coordinates
    jumps: Optional[List[Jump]]
    destiny: Optional[Coordinates]
