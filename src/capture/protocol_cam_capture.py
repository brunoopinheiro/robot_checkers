import os
import cv2
from typing import Optional
from time import sleep


class Capture:
    def __init__(self, camera_index=0):
        # Pode mudar a câmera a partir do índice
        self.camera_index = camera_index
        self.video_capture = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
        self.output_dir = 'images'
        os.makedirs(self.output_dir, exist_ok=True)
        if not self.video_capture.isOpened():
            raise SystemError("Cannot open camera")

    def capture_image(
            self,
            interval: int = 1,
            photo_count: Optional[int] = None,
    ) -> None:
        if photo_count is None:
            photo_count = int(input('Quantidade de imagens: '))
        photo_id = 0
        sleep(2)
        _stop = False
        try:
            while photo_id < photo_count and _stop is False:
                ret, frame = self.video_capture.read()
                if ret:
                    basename = f'image_{photo_id+1}.png'
                    photo_filename = os.path.join(self.output_dir, basename)
                    flipped = cv2.flip(frame, 1)
                    cv2.imshow('RobotCam', flipped)
                    key = cv2.waitKey(interval * 1000)
                    if key == ord('q'):
                        _stop = True
                    else:
                        cv2.imwrite(photo_filename, frame)
                        print(f"Photo saved as {photo_filename}")
                        photo_id += 1

                else:
                    print("Failed to grab frame")
        except KeyboardInterrupt:
            print("Interrupted by user")
        finally:
            self.video_capture.release()
            cv2.destroyAllWindows()
