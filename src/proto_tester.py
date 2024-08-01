import requests
from proto.messages import Board

# Sample proto conversion from bytes to proto


def main():
    try:
        requests.get('http://localhost:5000/game/start/1/green/purple')
        requests.get('http://localhost:5000/game/move_piece/a3/b4')
    except Exception:
        print('Belezinha')
    response = requests.get('http://localhost:5000/game/game_state')
    rescont = response.content
    board = Board().parse(rescont)
    print(len(board.rows))
    for bt_row in board.rows:
        for sqr in bt_row.squares:
            print(sqr.content)


if __name__ == '__main__':
    main()
