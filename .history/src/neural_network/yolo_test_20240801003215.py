from model import Model
import cv2

def main():
    model = Model()
    img_path = 'images/image_2.png'
    img_read = cv2.imread(img_path)
    dict_yolo = model.predict_from_opencv(img_read)
    print(dict_yolo)


if __name__ == '__main__':
    main()
