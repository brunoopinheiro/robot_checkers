from game.checkers import Checkers
from game.coordinates import Coordinates
from game.mocks.mock_init import FIRST_MOVE, THIRD_MOVE
from neural_network.game_ai import GameAI, GameAIResult, GameAIResultType

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


def play_move(game_ai_result: GameAIResult, game: Checkers):
    if game_ai_result.result_type == GameAIResultType.MOVE:
        game.move_piece(
            game_ai_result.origin,
            game_ai_result.destiny,
        )
    if game_ai_result.result_type == GameAIResultType.JUMP:
        game.jump_multiple(
            game_ai_result.origin,
            game_ai_result.target,
        )


def game_read():
    game = Checkers(
        first_player=0,
        player1_color='green',
        player2_color='purple'
    )
    game.start_game()
    last_play = GameAI.detect_play(
        game._board,
        game.p1_pieces,
        game.p2_pieces,
        FIRST_MOVE,
    )
    play_move(last_play, game)
    game.move_piece(
        Coordinates('d', 6),
        Coordinates('c', 5),
    )
    last_play = GameAI.detect_play(
        game._board,
        game.p1_pieces,
        game.p2_pieces,
        THIRD_MOVE,
    )
    print(last_play)
    play_move(last_play, game)
    game.board_state()


if __name__ == '__main__':
    game_read()
