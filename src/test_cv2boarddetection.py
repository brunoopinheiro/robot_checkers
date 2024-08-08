import cv2
from neural_network.coords_parser import CoordsParser


def main():
    imgpath = 'images/board_onepiece.jpg'
    matlikeimg = cv2.imread(imgpath)
    result = CoordsParser.detect_checkboard(matlikeimg, True)
    print(result.shape)


if __name__ == '__main__':
    main()
