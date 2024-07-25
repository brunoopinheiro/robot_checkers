from neural_network.model import Model
from capture.capture_module import CaptureModule


def main():
    cap = CaptureModule(0)
    img = cap.capture_opencv()

    model = Model()
    resdict = model.predict_from_opencv(img)
    print(resdict)


if __name__ == '__main__':
    main()
