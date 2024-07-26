from model import YOLOModels
from ultralytics import YOLO


class UntrainedModel:

    def __init__(self) -> None:
        self.__model = YOLO(YOLOModels.NANO_PRETRAINED.value)
        self.__model.train(
            data='datasets/data.yaml',
            epochs=5,
            imgsz=640,
        )
        metrics = self.__model.val()
        print(metrics)
        results = self.__model(r'\images\test_image.jpg')
        print(results)
        path = self.__model.export(format='onnx')
        print(path)


if __name__ == '__main__':
    model = UntrainedModel()
