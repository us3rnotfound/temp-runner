import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

b,g,r,a = 0,255,0,0

class Video_output():
    
    def __init__(self):
        self.img_file = 'dark_1024.jpg'
        self.font = ImageFont.truetype("DejaVuSans.ttf", 32)

    def _clear_img(self):
        img = cv2.imread(self.img_file)
        self.img_pil = Image.fromarray(img)

        self.draw = ImageDraw.Draw(self.img_pil)

    def _write_temps(self, temps):
        n = 1
        print(temps)
        for temp in temps:
            self.draw.text((50, 80+(n*40)),  "Sensor " + str(n) +": {:0.2f}°F".format(temp), font = self.font, fill = (b, g, r, a))
            n += 1

    def update_temps(self, temps):
        self._clear_img()
        self._write_temps(temps)

        img_np = np.array(self.img_pil)
        cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)          
        cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("img", img_np)

        cv2.waitKey(500)

    def destroy_video(self):
        cv2.destroyAllWindows() 
