from game.checkers import Checkers
from game.coordinates import Coordinates
from game.mocks.mock_init import FIRST_MOVE, THIRD_MOVE
from neural_network.game_ai import GameAI
from neural_network.capture_tree.tree import Tree, Node
# This file should be deleted


def next_player(player):
    if player == 1:
        return 2
    return 1


def main():
    game = Checkers(
        first_player=0,
        player1_color='purple',
        player2_color='green'
    )
    game.start_game()

    parser_opt = {
        'move': game.move_piece,
        'jump': game.jump_multiple,
    }

    plays = [
        # roxo
        {
            'play': 'move',
            'args': [Coordinates('a', 3), Coordinates('b', 4)],
        },
        # verde
        {
            'play': 'move',
            'args': [Coordinates('d', 6), Coordinates('c', 5)],
        },
        # roxo
        {
            'play': 'jump',
            'args': [
                Coordinates('b', 4),
                [
                    (
                        Coordinates('c', 5),
                        Coordinates('d', 6),
                    ),
                ],
            ],
        },
        # verde
        {
            'play': 'jump',
            'args': [
                Coordinates('c', 7),
                [
                    (
                        Coordinates('d', 6),
                        Coordinates('e', 5),
                    ),
                ],
            ],
        },
        # roxo
        {
            'play': 'move',
            'args': [Coordinates('e', 3), Coordinates('f', 4)],
        },
        # verde
        {
            'play': 'move',
            'args': [Coordinates('b', 8), Coordinates('c', 7)],
        },
        # roxo
        {
            'play': 'jump',
            'args': [
                Coordinates('f', 4),
                [
                    (
                        Coordinates('e', 5),
                        Coordinates('d', 6),
                    ),
                    (
                        Coordinates('c', 7),
                        Coordinates('b', 8),
                    ),
                ],
            ],
        },
    ]
    player = 1
    for play in plays:
        opt = play['play']
        act_function = parser_opt.get(opt)
        act_function(*play['args'])
        print(f'Rodadas {game.rounds}')
        game.board_state()
        game.check_endgame()
        player = next_player(player)
        if game.is_finished:
            print('Winner: Player ', game.winner)


def game_read():
    game = Checkers(
        first_player=0,
        player1_color='green',
        player2_color='purple'
    )
    game.start_game()
    pieces_list = GameAI.detection_to_gamepieces(FIRST_MOVE, game)
    game.overwrite_board(pieces_list)
    game.board_state()
    pieces_list = GameAI.detection_to_gamepieces(THIRD_MOVE, game)
    game.overwrite_board(pieces_list)
    game.board_state()
    gameai = GameAI('green', 'purple')
    gameai.evaluate_moves(game, True)
    print('Rounds: ', game.rounds)
    print('Finished: ', game.is_finished)
    print('Winnder: ', game.winner)
    print('P1 Queens: ', game.p1_queens)
    print('P2 Queens: ', game.p2_queens)


def test_moves():
    available_moves = GameAI.move_left('e3', 7, backwards=True)
    print(available_moves)


def test_tree():
    tree = Tree('d4')
    c1 = tree.root.append_child('c3', 'b2')
    c2 = tree.root.append_child('e3', 'g2', True)
    c3 = tree.root.append_child('c5', 'b6')
    d1 = c3.append_child('c7', 'd8')
    d2 = c3.append_child('a1', 'c2')
    e1 = d1.append_child('e7', 'h6')
    e2 = d2.append_child('d8', 's5', True)
    deepest = tree.depth_search()
    print('Deepest: ', deepest)
    parents = tree.trace_back(deepest)
    for idx, p in enumerate(parents):
        print(idx, p)


if __name__ == '__main__':
    # main()
    # game_read()
    # test_moves()
    test_tree()
