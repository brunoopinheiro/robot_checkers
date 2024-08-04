from __future__ import annotations
from typing import Optional, List, Tuple
from enum import Enum
from game.board import Board
from game.piece import Coordinates, Piece
from game.pawn import Pawn
from game.queen import Queen
from proto.messages import Board as ProtoBoard


OUT_OF_BOUNDS = "You've tried to go out of the board."


class MovementTypes(Enum):

    MOVE = 1
    JUMP = 2


class Checkers:
    # "⬛" for filled spaced
    # "⬜" for blank space
    # "🟣" for Purple pieces
    # "🟢" for Green pieces

    __instance = None
    __colmap: dict[str, int] = {val: idx
                                for idx, val in enumerate(Board.columns)}

    @property
    def rounds(self) -> int:
        return (self.__plays // 2) + 1

    @property
    def winner(self) -> Optional[int]:
        return self.__winner

    @property
    def is_finished(self) -> bool:
        return self.__isfinished

    @property
    def p1_promote_row(self) -> int:
        return 8

    @property
    def p2_promote_row(self) -> int:
        return 1

    def __new__(cls, *args, **kwargs) -> Checkers:
        if Checkers.__instance is None:
            Checkers.__instance = super(Checkers, cls).__new__(cls)
        return Checkers.__instance

    def __init__(
            self,
            first_player: int,
            player1_color: str,
            player2_color: str,
    ) -> None:
        self._board = Board()
        self.p1_pieces: list[Piece] = []
        self.p1_queens = 0
        self.p2_pieces: list[Piece] = []
        self.p2_queens = 0
        self.__plays = 0
        self.__draw_count = 0
        self.__isfinished = False
        self._p1c = player1_color.lower()
        self._p2c = player2_color.lower()
        self.__winner = None

    def _geticon(self, color, queen=False) -> str:
        green = ('green', 'g', 'verde', 'v')
        if not queen:
            if color.lower() in green:
                return '🟢'
            return '🟣'
        if color.lower() in green:
            return '❇️'
        return '⚛️'

    def _getpromote(self, color: str) -> int:
        if color == self._p1c:
            return self.p1_promote_row
        if color == self._p2c:
            return self.p2_promote_row

    def _getpiece_by_color(self, color: str) -> list[Piece]:
        if color == self._p1c:
            return self.p1_pieces
        if color == self._p2c:
            return self.p2_pieces

    def __initial_pieces(self) -> None:
        cols = Board.columns
        p1icon = self._geticon(self._p1c)
        p2icon = self._geticon(self._p2c)
        for i, c in enumerate(cols):
            if i % 2 == 0:
                pg1 = Pawn(
                    coordinates=Coordinates(c, 1),
                    color=self._p1c,
                    icon=p1icon,
                    promote_row=8,
                )
                pg2 = Pawn(
                    coordinates=Coordinates(c, 3),
                    color=self._p1c,
                    icon=p1icon,
                    promote_row=8,
                )
                self.p1_pieces.append(pg1)
                self.p1_pieces.append(pg2)
                pp1 = Pawn(
                    coordinates=Coordinates(c, 7),
                    color=self._p2c,
                    icon=p2icon,
                    promote_row=1,
                )
                self.p2_pieces.append(pp1)
            else:
                pg1 = Pawn(
                    coordinates=Coordinates(c, 2),
                    color=self._p1c,
                    icon=p1icon,
                    promote_row=8,
                )
                self.p1_pieces.append(pg1)
                pp1 = Pawn(
                    coordinates=Coordinates(c, 6),
                    color=self._p2c,
                    icon=p2icon,
                    promote_row=1,
                )
                pp2 = Pawn(
                    coordinates=Coordinates(c, 8),
                    color=self._p2c,
                    icon=p2icon,
                    promote_row=1,
                )
                self.p2_pieces.append(pp1)
                self.p2_pieces.append(pp2)

    def __distance(self, origin: Coordinates, destiny: Coordinates) -> int:
        o_col, o_row = origin
        d_col, d_row = destiny
        a: tuple[int, int] = (Checkers.__colmap[o_col], o_row)
        b: tuple[int, int] = (Checkers.__colmap[d_col], d_row)
        c = (abs(a[0] - b[0]), abs(a[1] - b[1]))
        return max(c)

    def check_endgame(self) -> None:
        if len(self.p1_pieces) == 0:
            self.__isfinished = True
            self.__winner = 2
        if len(self.p2_pieces) == 0:
            self.__isfinished = True
            self.__winner = 1
        if self.__draw_count == 5:
            self.is_finished = True
            self.__winner = None

    def _update_draw_count(self) -> None:
        self.__plays += 1
        cond_list = [
            # Duas damas contra duas damas;
            (self.p1_queens == 2 and self.p2_queens == 2),
            # Duas damas contra uma;
            # Uma dama contra uma dama e uma pedra.
            (self.p1_queens == 2 and self.p2_queens == 1),
            (self.p2_queens == 1 and self.p2_queens == 2),
            # Duas damas contra uma dama e uma pedra;
            (self.p1_queens == 2 and self.p2_pieces == 2),
            (self.p1_pieces == 2 and self.p1_queens == 2),
            # Uma dama contra uma dama;
            (self.p1_queens == 1 and self.p2_queens == 1),
        ]
        if any(cond_list):
            self.__draw_count += 1
        else:
            self.__draw_count = 0

    def _place_piece(
            self,
            piece: Piece,
            old_coords: Coordinates,
    ) -> None:
        self._board.place_piece(piece, piece.coordinates, old_coords)
        if (isinstance(piece, Pawn)
                and piece.promote_row == piece.coordinates.row):
            self._promote_piece(piece.coordinates)

    def _check_valid_move(
            self,
            piece: Piece,
            destiny: Coordinates,
    ) -> bool:
        try:
            if self.__distance(piece.coordinates, destiny) > piece.move_length:
                return False
            return True
        except KeyError:
            print(OUT_OF_BOUNDS)
            return False

    def _check_valid_jump(
            self,
            piece: Piece,
            destiny: Coordinates,
    ) -> bool:
        try:
            if self.__distance(piece.coordinates, destiny) > piece.jump_length:
                print('Your jump is too long')
                return False
            return True
        except KeyError:
            print(OUT_OF_BOUNDS)
            return False

    def start_game(self) -> None:
        self.__initial_pieces()
        for piece1, piece2 in zip(self.p1_pieces, self.p2_pieces):
            self._place_piece(piece1, piece1.coordinates)
            self._place_piece(piece2, piece2.coordinates)

    def board_state(self) -> None:
        self._board.board_state()

    def proto_board(self) -> ProtoBoard:
        return self._board.to_proto()

    def get_piece_by_coord(self, coord: Coordinates) -> Piece | None:
        for piece in self.p1_pieces:
            if piece.coordinates == coord:
                return piece
        for piece in self.p2_pieces:
            if piece.coordinates == coord:
                return piece
        return None

    def __remove_piece(self, piece_coordinates: Coordinates) -> bool:
        self._board.remove_piece(piece_coordinates)
        for idx, piece in enumerate(self.p1_pieces):
            if piece.coordinates == piece_coordinates:
                self.p1_pieces.pop(idx)
                if isinstance(piece, Queen):
                    self.p1_queens -= 1
        for idx, piece in enumerate(self.p2_pieces):
            if piece.coordinates == piece_coordinates:
                self.p2_pieces.pop(idx)
                if isinstance(piece, Queen):
                    self.p2_queens -= 1

    def move_piece(self, origin: Coordinates, destiny: Coordinates) -> bool:
        try:
            if self._board.is_empty(origin):
                return False
            if not self._board.is_empty(destiny):
                return False
            piece = self.get_piece_by_coord(origin)
            if self._check_valid_move(piece, destiny) is False:
                return False
            piece.move(destiny)
            self._place_piece(piece, origin)
            self._update_draw_count()
            return True
        except KeyError:
            print(OUT_OF_BOUNDS)
            return False

    def jump_piece(
            self,
            origin: Coordinates,
            destiny: Coordinates,
            target_piece: Coordinates,
    ) -> bool:
        if self._board.is_empty(origin):
            return False
        if not self._board.is_empty(destiny):
            return False
        piece = self.get_piece_by_coord(origin)
        middle_piece = self.get_piece_by_coord(target_piece)
        if middle_piece is None:
            return False
        if piece.color == middle_piece.color:
            return False
        if self._check_valid_jump(piece, destiny) is False:
            return False
        piece.move(destiny)
        self._place_piece(piece, origin)
        self.__remove_piece(middle_piece.coordinates)
        self._update_draw_count()
        return True

    def jump_multiple(
            self,
            origin: Coordinates,
            jumps: List[Tuple[Coordinates, Coordinates]],
    ) -> bool:
        # TODO: A pedra que durante o lance de captura
        # de várias peças, apenas passe por qualquer
        # casa de coroação, sem lá parar, não será promovida à dama.
        if self._board.is_empty(origin):
            return False
        piece = self.get_piece_by_coord(origin)
        for jump in jumps:
            old_coords = piece.coordinates
            target, destiny = jump
            if not self._board.is_empty(destiny):
                # jump target occupied
                return False
            mid_piece = self.get_piece_by_coord(target)
            if mid_piece is None:
                return False
            if piece.color == mid_piece.color:
                # cannot jump over a piece of the same color
                return False
            if self._check_valid_jump(piece, destiny) is False:
                return False
            piece.move(destiny)
            self._place_piece(piece, old_coords)
            self.__remove_piece(mid_piece.coordinates)
        self._update_draw_count()
        return True

    def _promote_piece(
            self,
            coordinates: Coordinates,
    ) -> Queen:
        piece = self.get_piece_by_coord(coordinates)
        icon = self._geticon(
            piece.color,
            True,
        )
        queen = Queen(
            coordinates=piece.coordinates,
            color=piece.color,
            icon=icon,
        )
        self.__remove_piece(piece.coordinates)
        if piece.color == self._p1c:
            self.p1_pieces.append(queen)
            self.p1_queens += 1
        else:
            self.p2_pieces.append(queen)
            self.p2_queens += 1
        self._place_piece(queen, queen.coordinates)

    def overwrite_board(
            self,
            pieces_list: List[Piece],  # filtered by GameAI
    ):
        p1_pieces = []
        p2_pieces = []
        self.p1_queens = 0
        self.p2_queens = 0
        for piece in pieces_list:
            if piece.color == self._p1c:
                p1_pieces.append(piece)
                if isinstance(piece, Queen):
                    self.p1_queens += 1
            else:
                p2_pieces.append(piece)
                if isinstance(piece, Queen):
                    self.p2_queens += 1
        self._board.overwrite_board(pieces_list)
        self.p1_pieces = p1_pieces
        self.p2_pieces = p2_pieces
        self._update_draw_count()
