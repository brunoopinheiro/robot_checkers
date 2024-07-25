from model import YOLOModels
from ultralytics import YOLO


class UntrainedModel:

    def __init__(self) -> None:
        self.__model = YOLO(YOLOModels.NANO_PRETRAINED.value)
        self.__model.train(
            data='datasets/data.yaml',
            epochs=1,  # change to 5 after validating proccess
            imgsz=640,
        )
        metrics = self.__model.val()
        print(metrics)
        results = self.__model(r'datasets\valid\images\WIN_20240717_13_54_08_Pro-2-_jpg.rf.7dd8f770b7cf930dec722daedda42ae3.jpg')
        print(results)
        path = self.__model.export(format='onnx')
        print(path)


if __name__ == '__main__':
    model = UntrainedModel()
