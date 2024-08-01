from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
from enum import Enum
from typing import Optional
from json import loads
from neural_network.coords_parser import CoordsParser


class YOLOModels(Enum):

    NANO_PRETRAINED = 'yolov8n.pt'
    SMALL_PRETRAINED = 'yolov8s.pt'
    TRAINED = 'src/neural_network/best.pt'


class Model:

    def __init__(self) -> None:
        self.__model = YOLO(YOLOModels.TRAINED.value)

    def predict(self, image_path: Optional[str] = None) -> None:
        # This may cause memory leak if using webcam
        image = '0'  # '0' means webcam prediction
        if image_path is not None:
            try:
                img_file = Image.open(image_path)
                image = img_file
            except (
                FileNotFoundError,
                UnidentifiedImageError,
                ValueError,
                TypeError,
            ) as err:
                print(err)
                print('Using webcam image')
        results = self.__model.predict(
            source=image,
            show=True,
            save=True,
            save_txt=True,
        )
        for r in results:
            boxes = r.boxes
            print('Boxes: ', boxes)
            masks = r.masks
            print('Masks: ', masks)
            keypoints = r.keypoints
            print('Keypoints: ', keypoints)
            probs = r.probs
            print('Probs: ', probs)
            obb = r.obb
            print('Or Obj Boxes: ', obb)
            r.show()
            jsonr = r.tojson()
            print(jsonr)

    def predict_from_opencv(self, cv_image, robot_ref: int):
        # res will always be a list with one element
        res = self.__model.predict(
            source=cv_image,
            show=True,
            save=True,
            save_txt=True,
        )
        r = res[0]
        jsonr = r.tojson()
        reslist = loads(jsonr)
        mapped_pieces = CoordsParser.map_pieces(reslist, robot_ref)
        return mapped_pieces
