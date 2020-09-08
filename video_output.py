import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import tkinter

b,g,r,a = 0,255,0,0

class Video_output():
    
    def __init__(self):
        #self.img_file = 'dark_1024.jpg'
        self.font = ImageFont.truetype("DejaVuSans.ttf", 32)

        try:
            root = tkinter.Tk()
            w, h = root.winfo_screenwidth(), root.winfo_screenheight()
            print(w,h)
            self.background_img = np.zeros((h,w,3), np.uint8)
        except:
            self.background_img = np.zeros((1024,768,3), np.uint8)

    def _clear_img(self):
        #img = cv2.imread(self.background_img)
        #self.img_pil = Image.fromarray(img)
        self.img_pil = Image.fromarray(self.background_img)
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
        #img_np_fullscreen = img_np.resize(1600,900)
        cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE )         
        cv2.setWindowProperty("img", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("img", img_np)

        cv2.waitKey(500)

    def destroy_video(self):
        print('DESTROY VIDEO')
        cv2.destroyAllWindows()
