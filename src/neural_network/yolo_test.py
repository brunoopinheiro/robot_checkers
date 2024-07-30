from model import Model
import cv2

def main():
    model = Model()
    img_path = 'images/images_extra_4-20240729T115001Z-001/images_extra_4/image_2.png'
    img_read = cv2.imread(img_path)
    img = cv2.flip(img_read, -1)
    return model.predict_from_opencv(img)


if __name__ == '__main__':
    main()
