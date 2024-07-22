from checkers import Checkers
from piece import Coordinates


def main():
    game = Checkers()
    game.start_game()
    print('=== CHECKERS ===')
    game.board_state()
    print()
    game.move_piece(
        origin=Coordinates('a', 3),
        destiny=Coordinates('b', 4)
    )
    game.board_state()
    print()
    game.move_piece(
        origin=Coordinates('h', 6),
        destiny=Coordinates('g', 5)
    )
    game.board_state()
    result = game.move_piece(
        origin=Coordinates('e', 3),
        destiny=Coordinates('c', 5)
    )
    print(result)


if __name__ == '__main__':
    main()
