from neural_network.model import Model
from neural_network.coords_parser import CoordsParser, RefferenceDict
import cv2


def main():
    model = Model()
    img_path = 'images/image0.jpg'
    img_read = cv2.imread(img_path)
    dict_yolo = model.predict_from_opencv(img_read)
    mapping = CoordsParser.map_pieces(
        dict_yolo,
        RefferenceDict.KINOVA,
    )
    print(mapping)
    print(f'LEN: {len(mapping)}')


if __name__ == '__main__':
    main()
