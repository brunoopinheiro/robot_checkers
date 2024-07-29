from neural_network.model import Model
# from capture.capture_module import CaptureModule
import cv2
from pprint import pprint


def main():
    # cap = CaptureModule(0)
    # img = cap.capture_opencv()
    rawimg = cv2.imread('images/test_image.jpg')
    img = cv2.flip(rawimg, 1)

    model = Model()
    resdict = model.predict_from_opencv(img)
    pprint(resdict)


if __name__ == '__main__':
    main()
