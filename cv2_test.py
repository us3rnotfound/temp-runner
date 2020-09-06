'''
import cv2
import numpy as np

width = 1280
height = 720
FPS = 24
seconds = 10

camera = cv2.VideoCapture(0)
while cv2.waitKey(30) < 0:
    rv, frame = camera.read()
    if rv:
        cv2.putText(frame, 'Hello World!', (50, 50), cv2.FONT_ITALIC, 0.8, 255)
        cv2.imshow('Video', frame)
'''
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, imshow, putText, FONT_ITALIC

width = 1280
height = 720
FPS = 24
seconds = 10

fourcc = VideoWriter_fourcc(*'MP42')
video = VideoWriter('./noise.avi', fourcc, float(FPS), (width, height))

for _ in range(FPS*seconds):
    frame = np.random.randint(0, 256, 
                              (height, width, 3), 
                              dtype=np.uint8)
    putText(frame, 'Hello World!', (50, 50), FONT_ITALIC, 0.8, 255)
    video.write(frame)
video.release()