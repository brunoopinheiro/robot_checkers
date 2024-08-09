import cv2
from neural_network.coords_parser import CoordsParser


def main():
    imgpath = 'images/board_onepiece.jpg'
    matlikeimg = cv2.imread(imgpath)
    CoordsParser.detect_checkboard(matlikeimg, True)


if __name__ == '__main__':
    main()
