from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
from enum import Enum
from typing import Optional


class YOLOModels(Enum):

    NANO_PRETRAINED = 'yolov8n.pt'
    SMALL_PRETRAINED = 'yolov8s.pt'
    TRAINED = 'best.pt'


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
        result = self.__model.predict(
            source=image,
            show=True,
            save=True,
            save_txt=True,
        )
        print(result)
