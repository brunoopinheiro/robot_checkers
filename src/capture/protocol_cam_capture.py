import cv2
import time
import os

class Capture:
    def __init__(self, camera_index=1):
        # Pode mudar a câmera a partir do índice
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        self.output_dir = 'images'

        os.makedirs(self.output_dir, exist_ok=True) 

        if not self.capture.isOpened():
            raise ValueError("Cannot open camera")

    def capture_image(self, interval=5, photo_count=0):
        photo_count = int(input('Quantidade de imagens: '))
        photo_id = 0

        time.sleep(2)

        try:
            while photo_id < photo_count:
                ret, frame = self.capture.read()

                if ret:
                    photo_filename = os.path.join(self.output_dir, f'image_{photo_id+1}.png')  
                    write = cv2.imwrite(photo_filename, frame)
                    flipped = cv2.flip(write, 1)
                    print(f"Photo saved as {photo_filename}")
                    photo_id += 1
                    cv2.imshow('RobotCam', flipped)

                    key = cv2.waitKey(interval * 2000)
                    if key == ord('q'):
                         break
                else:
                    print("Failed to grab frame")
        except KeyboardInterrupt:
            print("Interrupted by user")
        finally:
            self.capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    capture = Capture()
    capture.capture_image()