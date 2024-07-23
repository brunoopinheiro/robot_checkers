from checkers import Checkers
from piece import Coordinates


def main():
    game = Checkers()
    game.start_game()
    print('=== CHECKERS ===')
    game.move_piece(
        origin=Coordinates('a', 3),
        destiny=Coordinates('b', 4)
    )
    game.move_piece(
        origin=Coordinates('b', 6),
        destiny=Coordinates('c', 5)
    )
    game.jump_piece(
        origin=Coordinates('c', 5),
        destiny=Coordinates('a', 3),
        target_piece=Coordinates('b', 4),
    )
    game.move_piece(
        origin=Coordinates('c', 3),
        destiny=Coordinates('b', 4),
    )
    game.jump_piece(
        origin=Coordinates('a', 3),
        destiny=Coordinates('c', 5),
        target_piece=Coordinates('b', 4),
    )
    game.move_piece(
        origin=Coordinates('e', 3),
        destiny=Coordinates('d', 4),
    )
    game.jump_piece(
        origin=Coordinates('c', 5),
        destiny=Coordinates('e', 3),
        target_piece=Coordinates('d', 4),
    )
    game.jump_piece(
        origin=Coordinates('f', 2),
        destiny=Coordinates('d', 4),
        target_piece=Coordinates('e', 3),
    )
    game.move_piece(
        origin=Coordinates('f', 6),
        destiny=Coordinates('e', 5),
    )
    game.jump_piece(
        origin=Coordinates('e', 5),
        destiny=Coordinates('c', 3),
        target_piece=Coordinates('d', 4),
    )
    game.jump_piece(
        origin=Coordinates('b', 2),
        destiny=Coordinates('d', 4),
        target_piece=Coordinates('c', 3),
    )
    game.move_piece(
        origin=Coordinates('d', 6),
        destiny=Coordinates('c', 5),
    )
    game.jump_piece(
        origin=Coordinates('d', 4),
        destiny=Coordinates('b', 6),
        target_piece=Coordinates('c', 5),
    )
    game.jump_piece(
        origin=Coordinates('a', 7),
        destiny=Coordinates('c', 5),
        target_piece=Coordinates('b', 6),
    )
    game.move_piece(
        origin=Coordinates('g', 1),
        destiny=Coordinates('f', 2),
    )
    game.move_piece(
        origin=Coordinates('c', 5),
        destiny=Coordinates('d', 4),
    )
    game.move_piece(
        origin=Coordinates('f', 2),
        destiny=Coordinates('e', 3),
    )
    game.jump_piece(
        origin=Coordinates('d', 4),
        destiny=Coordinates('f', 2),
        target_piece=Coordinates('e', 3),
    )
    game.move_piece(
        origin=Coordinates('f', 2),
        destiny=Coordinates('g', 1)
    )
    game._promote_piece(Coordinates('g', 1))
    game._promote_piece(Coordinates('h', 2))
    game.board_state()


if __name__ == '__main__':
    main()
