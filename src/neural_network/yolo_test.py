from model import Model


def main():
    model = Model()
    img_path = 'images/test_image.jpg'
    model.predict(image_path=img_path)


if __name__ == '__main__':
    main()
