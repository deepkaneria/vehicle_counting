import cv2
import os

if not os.path.exists('frames'):
    os.makedirs('frames')

vidcap = cv2.VideoCapture('video/video.mp4')  # Input Video
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("frames/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
