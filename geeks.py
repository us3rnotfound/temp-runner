# Python program to explain cv2.putText() method 
    
# importing cv2 
import cv2 
import time
    
'''
cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow("window", img)
'''
# path 
path = r'geeks.png'
    
# Reading an image in default mode 
image = cv2.imread(path) 
    
# Window name in which image is displayed 
window_name = 'Image'
  
# text 
text = 'GeeksforGeeks'
  
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (00, 185) 
  
# fontScale 
fontScale = 1
   
# Red color in BGR 
color = (0, 0, 255) 
  
# Line thickness of 2 px 
thickness = 2
i = 0
while True:
    i += 1
    text = "Random: " + str(i)
    # Using cv2.putText() method 
    image = cv2.putText(image, text, org, font, fontScale,  
                    color, thickness, cv2.LINE_AA, False) 
    
    # Using cv2.putText() method 
    #image = cv2.putText(image, text, org, font, fontScale, 
    #                color, thickness, cv2.LINE_AA, True)  
    time.sleep(1)
    # Displaying the image 
    cv2.imshow(window_name, image)  
    if cv2.waitKey(0):
        break