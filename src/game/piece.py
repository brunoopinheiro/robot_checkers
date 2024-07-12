from collections import namedtuple
from abc import ABC, abstractmethod


Coordinates = namedtuple('Coordinates', ['col', 'row'])


class Piece(ABC):

    def __init__(
        self,
        coordinates: Coordinates,
        color: str,
        icon: str,
    ) -> None:
        self.__color = color
        self.__icon = icon
        self.__coordinates = coordinates

    @property
    def color(self) -> str:
        """String representing the piece color."""
        return self.__color

    @property
    def icon(self) -> str:
        """String representing the piece in a board."""
        return self.__icon

    @property
    def coordinates(self) -> Coordinates:
        """The actual piece coordinates."""
        return self.__coordinates

    @abstractmethod
    def move(self, new_coordinate: Coordinates) -> None:
        """Updates the piece coordinates given a new
        coordinate reference."""
        raise NotImplementedError

    @property
    @abstractmethod
    def move_length(self) -> int:
        """Returns how many squares the piece can move
        in a normal movement."""
        raise NotImplementedError
