from neural_network.model import Model
from capture.capture_module import CaptureModule
from pprint import pprint


def main():
    cap = CaptureModule(0)
    img = cap.capture_opencv()

    model = Model()
    resdict = model.predict_from_opencv(img)
    pprint(resdict)


if __name__ == '__main__':
    main()
