import cv2
from neural_network.coords_parser import CoordsParser
from game.checkers import Checkers
from neural_network.model import Model
from neural_network.game_ai import GameAI


def main():
    imgpath = 'images/board_onepiece.jpg'
    matlikeimg = cv2.imread(imgpath)
    CoordsParser.detect_checkboard(matlikeimg, True)


def last_stretch():
    game = Checkers(1, 'purple', 'green')
    impath = 'images/board_onepiece.jpg'
    # impath = 'images/test_detection.jpg'
    matlikeimg = cv2.imread(impath)
    model = Model()
    predict_list = model.predict_from_opencv(matlikeimg)
    pieces_list = GameAI.detection_to_gamepieces(
        predict_list,
        game,
    )
    game.overwrite_board(pieces_list)
    game.board_state()


if __name__ == '__main__':
    last_stretch()
