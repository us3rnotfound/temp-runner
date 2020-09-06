import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

b,g,r,a = 0,255,0,0

class Video_output():
    
    def __init__(self):
        self.img_file = 'dark_1024.jpg'
        self.font = ImageFont.truetype("DejaVuSans.ttf", 32)
        self._clear_img()

        img = np.array(self.img_pil)

        cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)          
        cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("img", img)

    def _clear_img(self):
        print ('clear screen')
        img = cv2.imread(self.img_file)
        self.img_pil = Image.fromarray(img)
        self.draw = ImageDraw.Draw(self.img_pil)

    def _write_temps(self, temps):
        print ('write temps')
        shutdown_screen = 0
        n = 1
        for temp in temps:
            print(temp)
            self.draw.text((50, 80+(n*40)),  "Sensor " + str(n) +": {:0.2f}°F".format(temp), font = self.font, fill = (b, g, r, a))
            n += 1
        
        key=cv2.waitKey(500)
        if key==27:
            print ('not here')
            self.destroy_video()
            shutdown_screen = 1
        
        return shutdown_screen

    def update_temps(self, temps):
        self._clear_img()
        if self._write_temps(temps):
            return 1
        
        img = np.array(self.img_pil)

        #cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)          
        #cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("img", img)   
        print ('showing')
        return 0

    def destroy_video(self):
        cv2.destroyAllWindows() 
