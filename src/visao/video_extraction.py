import cv2
import os



path = 'src/visao/dataset_week_2/video2/'
path_video = (os.path.join(path, (os.listdir(path)[0]))).replace('\\', '/')


path_images = 'src/visao/dataset_week_2/extracted_frames2'



captured_video = cv2.VideoCapture(path_video)
count = 0
i = 1
success = True
while success:
    success,image = captured_video.read()
    if count%20 == 0 :
            print(f'Processing frame {i} - sucessso: {success}')
            cv2.imwrite(os.path.join(path_images, f'picture{i}.jpg'), image)
            i += 1
    count += 1
    
