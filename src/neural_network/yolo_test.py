from model import Model
import cv2

def main():
    model = Model()
    img_path = 'images/image_2.png'
    img_read = cv2.imread(img_path)
    img = cv2.rotate(img_read, cv2.ROTATE_90_CLOCKWISE)
    return model.predict_from_opencv(img)


if __name__ == '__main__':
    main()
