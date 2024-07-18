import cv2
import os

cwd = os.getcwd()


path = 'src/visao/video'
path_video = (os.path.join(path, (os.listdir(path)[0]))).replace('\\', '/')


path_images = 'src/visao/extracted_frames'



captured_video = cv2.VideoCapture(path_video)
count = 0
i = 1
success = True
while success:
    success,image = captured_video.read()
    if count%15 == 0 :
            print(f'Processing frame {i} - sucessso: {success}')
            cv2.imwrite(os.path.join(path_images, f'picture{i}.jpg'), image)
            i += 1
    count += 1
    
