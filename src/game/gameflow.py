from checkers import Checkers
from coordinates import Coordinates


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

    player = 1
    while not game.is_finished:
        # do something
        print(f'== Player {player} | Rodada {game.rounds} ==')
        game.board_state()
        print('What do you want to do?')
        print('[1] Move Piece')
        print('[2] Jump Piece')
        opt = int(input('>> '))
        if opt == 1:
            origin = input('Origin: ')
            or_cd = Coordinates(
                col=origin[0],
                row=int(origin[1]),
            )
            destiny = input('Destiny: ')
            dt_cd = Coordinates(
                col=destiny[0],
                row=int(destiny[1]),
            )
            game.move_piece(
                origin=or_cd,
                destiny=dt_cd,
            )
        if opt == 2:
            origin = input('Origin: ')
            or_cd = Coordinates(
                col=origin[0],
                row=int(origin[1]),
            )
            destiny = input('Destiny: ')
            dt_cd = Coordinates(
                col=destiny[0],
                row=int(destiny[1]),
            )
            target = input('Target: ')
            tg_cd = Coordinates(
                col=target[0],
                row=int(target[1]),
            )
            game.jump_piece(
                origin=or_cd,
                destiny=dt_cd,
                target_piece=tg_cd,
            )
        game.check_endgame()
        player = next_player(player)
        if game.is_finished:
            print('Winner: Player ', game.winner)


if __name__ == '__main__':
    main()
